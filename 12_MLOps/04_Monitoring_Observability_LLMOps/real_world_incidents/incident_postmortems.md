# Production Incident Postmortems: What Actually Goes Wrong

> **Core Theme:** 4 Real-World Case Studies · Symptom · Evidence · Root Cause · Remediation · Prevention  
> **Source Session:** MLOps Engineering Session 4 of 5 (Chapter 3)

---

## The Golden Rule of MLOps Incident Investigation
```
When a model misbehaves, investigate in this exact order:
1. Upstream Data Pipeline (Schema, missing values, timezone shifts)
2. Environment & Dependencies (Library versions, CUDA drivers)
3. Infrastructure & Networking (Timeouts, payload truncation)
4. THE MODEL ITSELF (Retrain only when 1, 2, and 3 are proven healthy)
```

---

## Incident 01: Banking Credit Scoring (Concept Drift)

### 1. The Symptom
A major retail bank noticed default rates on personal loans tripled over a 4-month period. The credit risk model was green on dashboards, latency was 28 ms, and HTTP error rate was 0.00%.

### 2. Timeline & Discovery
- **Month 1:** Government enacts emergency pandemic loan moratoriums and direct stimulus deposits.
- **Month 2:** Model continues approving loans based on high bank account balances and lack of recent delinquencies.
- **Month 4:** Moratorium expires. Defaults spike catastrophically. The business discovers the issue via quarterly accounting reviews (4-month detection lag).

### 3. Root Cause: Concept Drift ($P(Y|X)$ changed)
- The relationship between inputs $X$ (account balance, recent credit score) and target $Y$ (probability of default) was severed by macroeconomic intervention.
- High checking balances no longer indicated high earned income—they indicated temporary government subsidies.

### 4. Remediation & Prevention
- **Immediate Fix:** Fallback to strict rule-based heuristic underwriting; suspended the model's automated approval threshold.
- **Permanent Solution:**
  1. Instrumented **Population Stability Index (PSI)** on output predictions. The score had drifted to $0.38$ in Month 1, which should have triggered an alert immediately.
  2. Integrated macroeconomic indicators (interest rates, unemployment rates) into feature store.
  3. Deployed challenger models in **Shadow Mode** to benchmark performance before restoring automated authority.

---

## Incident 02: Computer Vision Defect Detection (Data Drift)

### 1. The Symptom
A manufacturing assembly line defect detection model suddenly experienced a $65\%$ surge in false positive defect alerts, shutting down production lines multiple times a day.

### 2. Timeline & Evidence
- **Day 0:** Maintenance crew replaced burnt-out overhead fluorescent tubes with high-efficiency 5000K LED industrial fixtures during weekend maintenance.
- **Monday Morning:** Camera feeds began reporting micro-cracks on flawless metal sheets.
- **Inspection of Embeddings:** UMAP visualization of camera image embeddings showed an immediate cluster shift away from the training distribution.

### 3. Root Cause: Data Drift ($P(X)$ changed, $P(Y|X)$ constant)
- The physical relationship between true metal flaws and surface texture was unchanged.
- However, the input pixel distribution changed drastically due to higher Kelvin color temperature, sharper shadows, and specular glare.

### 4. Remediation & Prevention
- **Immediate Fix:** Replaced camera lens exposure settings and added a polarizing filter to mitigate specular glare.
- **Permanent Solution:**
  1. Implemented **Evidently AI / KS-test drift detection** on average image histogram brightness and contrast channels.
  2. Retrained model using heavy photometric data augmentations (random brightness $\pm 40\%$, contrast jitter, color temperature shifts).
  3. Added an automated daily test set benchmark validating camera calibration against a physical Macbeth color chart on the assembly line.

---

## Incident 03: RAG Customer Support Assistant (Retrieval & Knowledge Drift)

### 1. The Symptom
An enterprise customer support RAG assistant began giving contradictory, hallucinated answers regarding refund policies and enterprise SLA terms.

### 2. Evidence
- Customers were promised 90-day no-questions-asked refunds, even though the official policy was updated to 14 days.
- Traces in **Langfuse** revealed high LLM generation confidence, but the retrieved context chunks contained contradictory excerpts.

### 3. Root Cause: Knowledge & Retrieval Drift
- The legal team uploaded a new PDF (`Refund_Policy_2026_v2.pdf`) to SharePoint.
- The ETL vector ingestion pipeline was triggered, embedding the new chunks.
- However, **old chunks from `Refund_Policy_2024.pdf` were never purged from the Pinecone vector database!**
- The vector similarity search returned both the 2024 and 2026 paragraphs with high cosine similarity, confusing the LLM generator.

### 4. Remediation & Prevention
- **Immediate Fix:** Executed namespace purge in vector database; re-indexed only active, approved documents.
- **Permanent Solution:**
  1. Implemented **document-level versioning and TTL metadata filtering** (`where: {"doc_version": "active"}`).
  2. Automated daily **RAGAS evaluation suite**: Faithfulness and Context Precision monitored on a golden regression test suite.
  3. Prompts updated with strict conflict resolution directives ("If two retrieved passages contradict, obey the one with the latest timestamp").

---

## Incident 04: Retail Demand Forecasting (Upstream Schema Drift)

### 1. The Symptom
On Black Friday week, a national retailer's automated replenishment model under-ordered popular electronics by $80\%$, leading to massive stockouts and millions in lost revenue.

### 2. Root Cause: Upstream Data Pipeline / Schema Drift
- Two weeks prior, the data engineering team migrated the promotion table in Snowflake, renaming the column `is_holiday_promoted` to `promo_flag_active`.
- The feature pipeline did not throw an error because it utilized `.get("is_holiday_promoted", 0)` with a default fallback to 0.
- The model silently assumed **every product on Black Friday was unpromoted**, predicting standard weekday sales volumes.

### 3. Remediation & Prevention
- **Immediate Fix:** Replaced missing column mapping in feature view; issued emergency manual stock replenishment orders.
- **Permanent Solution:**
  1. Replaced silent default fallbacks with strict **Pydantic / Great Expectations data contracts** that fail loudly on missing features.
  2. Implemented **Prediction Distribution Alerts**: An alert should have fired when median predicted unit demand fell below the historical 3-year Black Friday average.
  3. Added cross-functional CI/CD schema validation contracts between Data Engineering and MLOps teams.
