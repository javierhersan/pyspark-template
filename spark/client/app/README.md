# PySpark Job Execution in a Cluster

## Overview

This document explains how a PySpark job runs in a distributed Spark cluster with **one master node and two worker nodes**.

## Cluster Setup

The cluster consists of:

- **1 Spark Master** (schedules tasks)
- **2 Spark Workers** (execute tasks)
- **1 Spark Client** (submits the job via `docker run`)

## Execution Steps

### 1. Spark Application Initialization

```python
spark = SparkSession.builder.appName("PySparkApp").getOrCreate()
```

- A **SparkSession** is created, initializing a Spark application.
- The **driver program** (running inside `spark-client`) registers with the **Spark master**.

### 2. DataFrame Creation

```python
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)
```

- A DataFrame is created and logically divided into **partitions**.
- Spark distributes partitions across available workers.

### 3. Data Processing (Triggering Execution)

```python
df.show()
```

- The `show()` action triggers execution.
- The **Spark master assigns tasks** to worker nodes.
- Workers process the data and send results back to the driver.

### 4. Writing Data in Parallel

```python
df.write.mode("overwrite").csv("/opt/spark-data/output")
```

- Data is **written in parallel** as multiple `part-xxxxx.csv` files.
- Each partition gets its own output file inside `/opt/spark-data/output/`.

**Example Output (Distributed Write):**

```
/data/output/
├── part-00000-xxxxxxxx.csv
├── part-00001-xxxxxxxx.csv
├── _SUCCESS
```

### 5. Coalesce: Merging Data into a Single File

```python
df.coalesce(1).write.mode("overwrite").csv("/opt/spark-data/output", header=True)
```

- `coalesce(1)` **reduces the number of partitions to 1**.
- A **single worker** writes the final CSV file.

**Example Output (Single File):**

```
/data/output/
├── part-00000-xxxxxxxx.csv  # Only ONE file now
├── _SUCCESS
```

## How the Cluster Processes the Job

| Step                                  | Master                           | Worker A                    | Worker B                    |
| ------------------------------------- | -------------------------------- | --------------------------- | --------------------------- |
| **1. Job Submission**                 | Receives job from `spark-client` | -                           | -                           |
| **2. Task Scheduling**                | Assigns tasks to workers         | Receives task (if needed)   | Receives task (if needed)   |
| **3. Data Processing (`show()`)**     | Gathers results                  | Processes part of DataFrame | Processes part of DataFrame |
| **4. Writing CSV (Parallel)**         | Coordinates output               | Writes part of CSV          | Writes part of CSV          |
| **5. Coalesce (Single Worker Write)** | Assigns single worker            | 📝 Writes full CSV          | -                           |
