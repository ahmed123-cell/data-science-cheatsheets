# 📊 Big Data Explained

A concise guide to Big Data, Hadoop, and Apache Spark.

## 📑 Table of Contents

1. [What is Big Data?](#1-what-is-big-data)
2. [The 4 Vs of Big Data](#2-the-4-vs-of-big-data)
3. [Hadoop](#3-hadoop)
4. [Apache Spark](#4-apache-spark)
5. [Hadoop vs Spark](#5-hadoop-vs-spark)
6. [Summary](#6-summary)

---

## 1. What is Big Data?

**Big Data** refers to extremely large, complex, and fast-growing datasets that cannot be efficiently processed or analyzed using traditional tools and methods (like Excel or traditional relational databases).

**Common sources:**

- Social media
- Sensors and IoT devices
- Transaction records
- Videos
- Logs

---

## 2. The 4 Vs of Big Data

The core characteristics of Big Data are commonly described using the **4 Vs**:

| V | Meaning | Example |
|---|---------|---------|
| 📦 **Volume** | The sheer amount of data | Petabytes or exabytes |
| ⚡ **Velocity** | The speed at which data is generated and processed | Stock markets, social media feeds, sensors |
| 🧩 **Variety** | The different types and formats of data | Tables, JSON, images, video |
| ✅ **Veracity** | The quality and trustworthiness of data | Noise, bias, missing values |

> 💡 Some people add a 5th V: **Value**, the business value extracted from the data.

### 2.1 Volume
- The **sheer amount of data** being generated.
- Traditional systems struggle to store and process such huge volumes.

### 2.2 Velocity
- The **speed** at which data is generated, collected, and processed.
- Requires systems that can process streaming data quickly.

### 2.3 Variety
- The **different types and formats** of data:
  - **Structured**: tables, CSV
  - **Semi-structured**: JSON, XML
  - **Unstructured**: text, images, videos, audio
- Makes data harder to integrate and analyze.

### 2.4 Veracity
- The **quality, accuracy, and trustworthiness** of the data.
- Includes issues like noise, bias, missing values, and uncertainty.
- Poor veracity can lead to wrong insights and bad decisions.

---

## 3. Hadoop 🐘

**Hadoop** is an open-source framework designed to store and process Big Data in a distributed environment across clusters of computers.

### 3.1 Core Components

| Component | Role |
|-----------|------|
| **HDFS** (Hadoop Distributed File System) | Stores data across multiple machines in a fault-tolerant way. Breaks large files into blocks (default 128 MB) and distributes them. |
| **MapReduce** | The original processing engine. **Map** processes and filters data in parallel; **Reduce** aggregates the results. |
| **YARN** (Yet Another Resource Negotiator) | Manages resources and schedules jobs across the cluster. |
| **Hadoop Common** | Utilities and libraries needed by the other modules. |

### 3.2 How Hadoop Works

1. Data is stored on **HDFS** (distributed storage).
2. When a job runs, **MapReduce** breaks the task into smaller subtasks.
3. Tasks are executed in parallel on different nodes, following the **data locality principle** (process data where it is stored).
4. Results are combined to produce the final output.

### 3.3 Strengths and Weaknesses

| 👍 Strengths | 👎 Weaknesses |
|-------------|---------------|
| Excellent for batch processing of massive datasets | Slow for iterative or real-time processing |

---

## 4. Apache Spark ⚡

**Apache Spark** is a fast, in-memory data processing engine designed for Big Data. It was developed to overcome the limitations of Hadoop MapReduce.

### 4.1 Key Features

- **In-memory computing**: much faster than disk-based MapReduce.
- **One unified engine** for batch, streaming, machine learning, and SQL workloads.
- **Rich ecosystem**: Spark SQL, Spark Streaming, MLlib, GraphX, and more.

### 4.2 Architecture

| Component | Role |
|-----------|------|
| **Driver Program** | The main program that coordinates the execution. |
| **Cluster Manager** | Allocates resources (YARN, Mesos, Kubernetes, or Standalone). |
| **Executors** | Run on worker nodes and execute tasks. |

### 4.3 Data Abstractions

| Abstraction | Description |
|-------------|-------------|
| **RDD** (Resilient Distributed Dataset) | The core data structure: immutable, distributed, fault-tolerant. |
| **DataFrame / Dataset** | Higher-level structured APIs, recommended for most use cases. |

### 4.4 Execution Model

1. Spark builds a **Directed Acyclic Graph (DAG)** of operations.
2. It optimizes the execution plan (**lazy evaluation**).
3. Data is processed in parallel across many executors.
4. Intermediate results can be kept in memory (**caching**), making iterative algorithms like machine learning very fast.

---

## 5. Hadoop vs Spark ⚖️

| Aspect      | Hadoop (MapReduce) | Apache Spark                  |
|-------------|--------------------|-------------------------------|
| Processing  | Disk-based         | In-memory (can spill to disk) |
| Speed       | Slower             | 10x–100x faster               |
| Use case    | Batch processing   | Batch + Streaming + ML        |
| Ease of use | More complex       | Easier (high-level APIs)      |
| Real-time   | Not suitable       | Excellent (Spark Streaming)   |

---

## 6. Summary 📝

- **Big Data** is defined by the 4 Vs: Volume, Velocity, Variety, and Veracity.
- **Hadoop** revolutionized Big Data storage and batch processing.
- **Spark** improved on it with speed, ease of use, and support for modern workloads such as streaming and ML.

---

*Document created as part of learning Big Data technologies.*