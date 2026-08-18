# 🗄️ Data Engineering Concepts Explained

## ETL vs ELT ⚖️

- **ETL (Extract, Transform, Load)**: Process where data is **extracted** from sources, **transformed** (cleaned, enriched, aggregated) in a staging area, then **loaded** into the target system (usually a Data Warehouse).
- **ELT (Extract, Load, Transform)**: Data is **extracted** and **loaded** raw into the target (Data Lake/Warehouse), then **transformed** inside the powerful target system.
- **Key Difference**: ETL transforms **before** loading (traditional, good for structured data). ELT loads first then transforms (modern, scalable for big data).

**When to use**:
- ETL: Legacy systems, strict compliance, limited target compute.
- ELT: Cloud data platforms (Snowflake, BigQuery, Databricks) with massive compute power.

---

## Data Storage Architectures 🏗️

- **Data Warehouse**: Centralized repository for **structured, processed data** optimized for analytics and BI reporting. Schema-on-write (highly organized).
- **Data Lake**: Repository for **raw, unstructured/semi-structured data** at scale (schema-on-read). Stores everything cheaply (logs, images, JSON, etc.).
- **Data Lakehouse**: Modern hybrid combining **Data Lake** (cheap storage + variety) + **Data Warehouse** (ACID transactions, schema enforcement, SQL analytics). Examples: Databricks, Delta Lake.

**Summary**: Warehouse = Clean & Fast queries | Lake = Cheap & Flexible | Lakehouse = Best of both.

---

## Data Pipelines & Orchestration 🔄

- **Data Pipeline**: Automated workflow that moves and processes data from source to destination (includes extraction, transformation, loading).
- **Orchestration**: Managing and coordinating multiple pipelines, tasks, and dependencies (e.g., "run this after that succeeds").
- **Scheduling**: Defining **when** pipelines should run (cron jobs, every hour, daily at midnight, event-triggered).

**Popular Tools**:
- Orchestration: Apache Airflow, Dagster, Prefect, Luigi.
- Scheduling: Built into orchestrators or cron, Kubernetes CronJobs.

---

## Data Quality, Lineage & Observability 👀

- **Data Quality**: Ensures data is **accurate, complete, consistent, timely, and valid**. Includes validation rules, monitoring for anomalies, and cleansing.
- **Data Lineage**: Tracks the **full journey** of data — where it came from, how it was transformed, and where it went (like a family tree for data).
- **Observability**: Comprehensive monitoring of pipelines, including logs, metrics, traces, alerts for failures, performance, and data freshness.

**Why they matter**: Prevent "garbage in, garbage out", debug issues faster, and maintain trust in data.

---

## Batch vs Stream Processing ⚡

- **Batch Processing**: Processing data in **large chunks** at scheduled intervals (e.g., hourly or daily jobs). Efficient for high-volume, non-time-sensitive data.
- **Stream Processing**: Processing data **in real-time** as it arrives (event-by-event). Ideal for live analytics, monitoring, and low-latency applications.

**Examples**:
- Batch: Nightly sales reports (Spark, Hadoop).
- Stream: Fraud detection, live dashboards (Kafka + Flink, Spark Streaming).

---

## Data Modeling 🧱

- **Data Modeling**: Designing the structure and relationships of data for efficient storage, querying, and analysis.
  - **Star Schema**: Simple model with a central **Fact Table** (metrics) surrounded by **Dimension Tables** (descriptive context). Easy to understand and fast for queries.
  - **Snowflake Schema**: Normalized version of Star Schema where Dimension Tables are further broken into sub-tables. Saves storage but more complex joins.
  - **Fact & Dimension Tables**: 
    - **Fact Tables**: Contain measurable, quantitative data (e.g., sales amount, quantity).
    - **Dimension Tables**: Contain descriptive attributes (e.g., customer details, product info, time).

---

## Partitioning & Clustering 📂

- **Partitioning**: Dividing large tables into smaller, manageable parts based on a column (e.g., by date or region) to improve query speed and maintenance.
- **Clustering**: Organizing data within partitions based on similar values (e.g., clustering by customer_id) for even better performance on frequent filters.

**Benefit**: Dramatically reduces scanned data in queries (especially in Data Lakes/Lakehouses).

---

## Data Governance & Advanced Concepts 🛡️

- **Data Governance**: Policies, standards, and processes to ensure data is **secure, compliant, high-quality**, and properly managed across the organization.
- **CDC (Change Data Capture)**: Technique to detect and capture changes (inserts, updates, deletes) in source systems in real-time or near real-time.
- **Data Contracts**: Formal agreements defining the schema, semantics, and expectations of data between producers and consumers.
- **Data Mesh**: Decentralized architecture where domain teams own their data products (treat data as a product).
- **Medallion Architecture**: Layered data organization (Bronze → Silver → Gold) in Data Lakes/Lakehouses:
  - **Bronze**: Raw data.
  - **Silver**: Cleaned & enriched.
  - **Gold**: Aggregated & business-ready for consumption.

---