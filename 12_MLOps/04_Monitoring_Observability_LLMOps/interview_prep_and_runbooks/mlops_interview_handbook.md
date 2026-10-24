# MLOps Engineering Interview Handbook: 12 Core Questions & Deep Answers

> **Core Theme:** Architecture · Operations · Tooling · LLM Systems · Judgement · Rapid-Fire Q&A  
> **Source Session:** MLOps Engineering Session 4 of 5 (Chapter 6 & Appendices)

---

### Q1: What is the difference between Data Drift, Concept Drift, Prediction Drift, and Upstream Data Quality Drift?
- **Data Drift ($P(X)$ changes, $P(Y|X)$ constant):** The distribution of input features shifts, but the underlying law mapping input to output remains identical.
  - *Example:* A fraud detection model trained on Egyptian traffic suddenly sees $40\%$ of requests coming from Saudi Arabia with different transaction currencies and IP address blocks.
- **Concept Drift ($P(Y|X)$ changes, $P(X)$ constant or varying):** The true relationship between input features and the target label shifts.
  - *Example:* Due to sudden inflation or policy change, customers with a \\$50,000 salary who previously had a $2\%$ loan default rate now experience an $8\%$ default rate. The same input requires a different prediction.
- **Prediction Drift ($P(\hat{Y})$ changes):** The distribution of model outputs shifts.
  - *Importance:* Can be detected **immediately in real time** without waiting for ground truth labels. If an approval model normally approves $15\%$ of applications but suddenly approves $45\%$, prediction drift fires an instant alert.
- **Upstream Data Quality Drift:** Technical bugs in upstream pipelines (e.g. missing columns, timezone misalignments, sensor calibration failure, default fallbacks to 0).

---

### Q2: Why is monitoring model accuracy in production fundamentally difficult, and what proxies do we monitor instead?
- **The Problem:** In software, a 500 error is immediately known. In ML, ground truth labels ($Y$) often arrive with massive delays (weeks or months):
  - In credit risk, you only know if a borrower defaults 12–24 months later.
  - In churn prediction, you only know a customer churned after 30 days of inactivity.
- **The Solution (Monitoring Proxies):**
  1. **Prediction Distribution Drift:** Monitor histogram buckets and percentiles of model outputs ($\hat{Y}$).
  2. **Feature Input Drift (PSI / KS-test):** Track if incoming feature distributions differ significantly from the training baseline ($P(X)$).
  3. **Data Quality Metrics:** Missing value ratios, feature range violations, null rates.
  4. **Short-Term Business Proxies:** Immediate click-through rates, instant customer support complaint volume, early cancellations.

---

### Q3: What is the Population Stability Index (PSI), how is it calculated, and what are its operational thresholds?
- **Formula:**
  $$\text{PSI} = \sum_{i=1}^k \left(\text{Actual}_i - \text{Expected}_i\right) \times \ln\left(\frac{\text{Actual}_i}{\text{Expected}_i}\right)$$
- **Methodology:** Divide the reference baseline distribution into $k$ quantile buckets (typically 10 deciles, each holding $10\%$ of baseline data). Count the percentage of current production data falling into each bucket.
- **Standard Thresholds:**
  - $\text{PSI} < 0.10$: **Stable distribution.** No action required.
  - $0.10 \le \text{PSI} < 0.20$: **Moderate shift.** Log warning, investigate feature contributions, prepare retraining data.
  - $\text{PSI} \ge 0.20$: **Significant drift.** Trigger urgent alert; execute automated retraining or fallback to heuristic champion.

---

### Q4: When should you use the Kolmogorov-Smirnov (KS) test vs. Chi-Square test vs. Wasserstein Distance?
- **Two-Sample KS Test:** Best for **continuous, 1-dimensional features** (e.g. trip distance, income, latency). Non-parametric; measures the maximum vertical distance $D$ between two empirical cumulative distribution functions (CDFs).
- **Chi-Square Goodness-of-Fit Test ($\chi^2$):** Best for **discrete, categorical features** (e.g. payment method, device type, TLC zone IDs). Compares observed category counts against expected baseline proportions.
- **Wasserstein Distance (Earth Mover's Distance):** Measures the minimum "work" required to transform one probability distribution into another. Unlike KS which only looks at the maximum peak difference, Wasserstein measures the overall magnitude of the physical shift in feature units (e.g., "trip distance shifted by an average of 2.4 miles").

---

### Q5: In a RAG application, explain the difference between Faithfulness and Context Precision. Which component does each blame?
- **Faithfulness (Blames the LLM Generator):**
  - Measures whether every factual claim in the generated answer is directly substantiated by the retrieved context chunks.
  - Formula: $\frac{\text{Supported Claims}}{\text{Total Claims}}$.
  - If low, the LLM is **hallucinating** facts not present in the reference documents.
- **Context Precision (Blames the Vector Retriever / Reranker):**
  - Evaluates whether the most relevant, ground-truth chunks were placed at the **top ranks** of the context window (using Mean Average Precision).
  - If low, the retriever is burying critical facts under irrelevant noise chunks, degrading generator attention.

---

### Q6: How does vLLM achieve $2–4\times$ higher throughput than standard Hugging Face Transformers serving?
1. **PagedAttention:**
   - Traditional serving allocates contiguous GPU VRAM for each request's Key-Value (KV) cache based on maximum sequence length. Because sequence length is variable, 60–80% of GPU memory is wasted on fragmentation and over-reservation.
   - PagedAttention partitions the KV cache into fixed-size physical memory pages (like virtual memory in operating systems). Pages are allocated dynamically on-demand, achieving near-zero memory waste.
2. **Continuous (Iteration-Level) Batching:**
   - Traditional batching locks all requests in a batch together until the longest sequence completes generation.
   - Continuous batching operates at the token iteration level: requests that hit `<EOS>` are evicted immediately, and new queued requests are injected on the next iteration.

---

### Q7: Why is `pickle.loads` dangerous for production serving, and what should be used instead?
- **Vulnerability:** Python's `pickle` serialization format is a bytecode execution machine. Deserializing an untrusted payload using `pickle.loads()` allows arbitrary code execution (RCE) via `__reduce__` exploit payloads, compromising the entire host or container.
- **Production Standard:**
  - For external HTTP requests: Strict **Pydantic / JSON validation**.
  - For model graphs: **ONNX (Open Neural Network Exchange)** or **Safetensors**. ONNX defines a static computational graph without arbitrary Python execution capabilities, making it secure and cross-language interoperable (C++, Java, Go).

---

### Q8: What is the difference between Blue/Green deployment and Canary deployment?
- **Blue/Green Deployment:**
  - Deploys full new version (Green) alongside active version (Blue). Router switches $100\%$ of traffic instantly once Green passes smoke tests.
  - *Best For:* When breaking database schema changes or incompatible API payload structures require an immediate hard cutover.
- **Canary Deployment:**
  - Gradually shifts a tiny fraction of live traffic (e.g. $5\%$) to the candidate model while $95\%$ remains on baseline.
  - Telemetry (error rate, latency, PSI drift) is monitored for hours before stepping up traffic ($25\% \to 50\% \to 100\%$).
  - *Best For:* ML models where subtle behavioral flaws or prediction drift cannot be detected by standard unit health checks.

---

### Q9: How does Shadow Mode (Dark Launch) work, and why is it essential for high-risk ML?
- **Mechanism:** The API router handles incoming user requests by forwarding to the active production model and returning that prediction immediately to the client. In an asynchronous, non-blocking background task, the router duplicates the identical request payload to the candidate model.
- **Advantage:** Candidate model outputs are logged side-by-side with production outputs to verify latency, stability, and prediction drift under genuine production load **without any risk to end users or business revenue**.

---

### Q10: How do you prevent Airflow Scheduler latency when authoring DAGs?
- Keep task callables self-contained and **place heavy imports (PyTorch, TensorFlow, Scikit-Learn) inside the function definition**, not at top-level module scope.
- Airflow's scheduler parses every file in `dags/` every 30 seconds. Top-level heavy imports cause the scheduler CPU to spike and introduce task scheduling delays.

---

### Q11: What is the purpose of Correlation IDs (`X-Request-ID`) in MLOps microservices?
- In microservice architectures, a single user click travels across an API Gateway, an Auth Service, a Feature Store, an Inference Engine, and a Database.
- A Correlation ID is attached to the request header upon entry. Every log statement across all services includes this ID, enabling engineers to filter distributed logs in Datadog/ELK and reconstruct the exact execution trace of any single prediction.

---

### Q12: Walk through the first 15 minutes of an MLOps silent failure incident.
1. **Minute 0–3 (Acknowledge & Protect):** Check prediction drift alerts. If severe, toggle router to fallback champion model or rule-based heuristic. Protect customer experience first.
2. **Minute 3–7 (Inspect Upstream Data):** Verify incoming feature schemas. Check for null values, format changes, or ETL job failures. Remember: 80% of ML failures originate in data pipelines, not weights.
3. **Minute 7–11 (Inspect Environment & Infra):** Check container restarts, memory limits (OOM), and dependency versions.
4. **Minute 11–15 (Model Analysis & RCA):** Run statistical drift tests (PSI, KS-test) on individual features to isolate which input shifted. Initiate retraining or dataset recalibration.
