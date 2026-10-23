# 🏗️ Databases & SQL for Data Analytics and Data Engineering

A structured study guide covering database fundamentals, SQL, and the concepts that matter most for data analyst and data engineer roles.

---

## 📚 Table of Contents

**Part 1: Foundations**
1. [Introduction to Databases](#intro)
2. [Database vs Data Warehouse](#db-vs-dw)
3. [What is an RDBMS?](#rdbms)
4. [Database Objects](#objects)

**Part 2: SQL**
5. [SQL Fundamentals](#sql)
6. [SQL Categories: DDL, DML, DQL, DCL, TCL](#categories)

**Part 3: Data Modeling & Integrity**
7. [Keys and Relationships](#keys)
8. [Constraints](#constraints)
9. [Normalization](#normalization)

**Part 4: Database Objects in Depth**
10. [Indexes](#indexes)
11. [Views](#views)
12. [Stored Procedures](#procedures)
13. [Triggers](#triggers)

**Part 5: Reliability & Workloads**
14. [ACID Properties](#acid)
15. [OLTP vs OLAP](#oltp-olap)

**Part 6: Industry & Career**
16. [Common Databases in Industry](#industry)
17. [Data Analytics & Data Engineering Perspective](#perspective)
18. [Interview Cheat Sheet](#cheatsheet)
19. [Final Advice](#advice)
20. [Resources](#resources)

---

# Part 1: Foundations

<a id="intro"></a>
## 1. 🎯 Introduction to Databases

A **database** is a structured system used to store, organize, manage, and retrieve data efficiently.

**Where databases are used:**

- Banking systems
- E-commerce platforms
- Social media applications
- Healthcare systems
- Business intelligence platforms

> Without databases, modern software could not manage large volumes of data reliably.

---

<a id="db-vs-dw"></a>
## 2. 🏢 Database vs Data Warehouse

| | Database (OLTP) | Data Warehouse (OLAP) |
|---|---|---|
| **Purpose** | Day-to-day operations | Analytics and reporting |
| **Typical tasks** | Creating orders, updating customer info, processing transactions | Sales dashboards, business reports, trend analysis |
| **Workload** | Frequent inserts and updates, small transactions | Large analytical queries, aggregations |
| **Data** | Current | Historical |
| **Design** | Highly normalized | Denormalized |

See also: [OLTP vs OLAP](#oltp-olap).

---

<a id="rdbms"></a>
## 3. 🗄️ What is an RDBMS?

**RDBMS** = Relational Database Management System.

Data is stored in **tables**, and relationships between tables are created using **keys**.

| CustomerID | Name |
|------------|------|
| 1 | Ahmed |
| 2 | Sara |

**Popular RDBMS systems:** PostgreSQL, MySQL, SQL Server, Oracle, SQLite.

---

<a id="objects"></a>
## 4. 🧱 Database Objects

| Object | Purpose |
|--------|---------|
| Table | Store data |
| View | Virtual table |
| Index | Speed up queries |
| Stored Procedure | Reusable SQL program |
| Trigger | Automatic execution |
| Schema | Logical organization |
| Function | Return values from calculations |

Details: [Indexes](#indexes), [Views](#views), [Stored Procedures](#procedures), [Triggers](#triggers).

---

# Part 2: SQL

<a id="sql"></a>
## 5. 💻 SQL Fundamentals

**SQL** = Structured Query Language.

**SQL is used to:**

- Create structures
- Insert records
- Update records
- Delete records
- Query data
- Manage permissions

```sql
SELECT *
FROM Customers;
```

---

<a id="categories"></a>
## 6. ⚙️ SQL Categories

| Category | Full name | Purpose | Commands |
|----------|-----------|---------|----------|
| **DDL** | Data Definition Language | Define structures | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | Data Manipulation Language | Manipulate records | `INSERT`, `UPDATE`, `DELETE` |
| **DQL** | Data Query Language | Retrieve data | `SELECT` |
| **DCL** | Data Control Language | Control permissions | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | Control transactions | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

### 6.1 DDL: Data Definition Language

```sql
CREATE TABLE Customers(
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100)
);
```

### 6.2 ✏️ DML: Data Manipulation Language

```sql
INSERT INTO Customers (CustomerID, Name) VALUES (1, 'Ahmed');
UPDATE Customers SET Name = 'Ahmed Ali' WHERE CustomerID = 1;
DELETE FROM Customers WHERE CustomerID = 1;
```

### 6.3 🔍 DQL: Data Query Language

```sql
SELECT Name FROM Customers WHERE CustomerID = 1;
```

### 6.4 🔒 DCL: Data Control Language

```sql
GRANT SELECT ON Customers TO analyst_role;
REVOKE SELECT ON Customers FROM analyst_role;
```

### 6.5 🔄 TCL: Transaction Control Language

```sql
BEGIN;
UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 1;
UPDATE Accounts SET Balance = Balance + 100 WHERE AccountID = 2;
COMMIT;      -- or ROLLBACK; to undo both changes
```

---

# Part 3: Data Modeling & Integrity

<a id="keys"></a>
## 7. 🔑 Keys and Relationships

### 7.1 Primary Key

Uniquely identifies each row (e.g. `CustomerID`).

- Unique
- Cannot be `NULL`

### 7.2 Foreign Key

Creates a relationship between tables. Example: the Orders table references the Customers table.

```sql
CREATE TABLE Orders(
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
```

### 7.3 Relationship Types

| Type | Meaning | Example |
|------|---------|---------|
| **One-to-One (1:1)** | One row relates to exactly one row | One employee ↔ one badge |
| **One-to-Many (1:N)** | One row relates to many rows | One customer ↔ many orders |
| **Many-to-Many (M:N)** | Many rows relate to many rows | Many students ↔ many courses |

---

<a id="constraints"></a>
## 8. 🛡️ Constraints

Constraints improve **data quality** by enforcing rules at the database level.

| Constraint | Purpose |
|------------|---------|
| `PRIMARY KEY` | Unique, non-null row identifier |
| `FOREIGN KEY` | Links to another table's key |
| `UNIQUE` | No duplicate values in the column |
| `NOT NULL` | Value is required |
| `CHECK` | Value must satisfy a condition |
| `DEFAULT` | Value used when none is supplied |

```sql
Age INT CHECK(Age >= 18)
```

---

<a id="normalization"></a>
## 9. 📏 Normalization

Normalization **reduces redundancy** by organizing data into well-structured tables.

| Normal form | Rule |
|-------------|------|
| **1NF** | No repeating groups; atomic values |
| **2NF** | Remove partial dependencies |
| **3NF** | Remove transitive dependencies |

**Example:**

```text
Bad:     CustomerID | CustomerName | CityName

Better:  Customers Table
         Cities Table
```

| 👍 Benefits | 👎 Trade-off |
|------------|--------------|
| Less duplication, better consistency | More joins |

---

# Part 4: Database Objects in Depth

<a id="indexes"></a>
## 10. 🚀 Indexes

Indexes improve query performance.

| Without index | With index |
|---------------|------------|
| Full table scan | Direct lookup |

```sql
CREATE INDEX idx_customer_name
ON Customers(Name);
```

| 👍 Benefits | 👎 Trade-offs |
|------------|---------------|
| Faster filtering | Additional storage |
| Faster joins | Slower writes |
| Faster sorting | |

---

<a id="views"></a>
## 11. 👀 Views

A **view** is a virtual table generated from a query.

```sql
CREATE VIEW ActiveCustomers AS
SELECT *
FROM Customers
WHERE Status = 'Active';
```

**Advantages:** security, simplicity, reusability.

---

<a id="procedures"></a>
## 12. ⚙️ Stored Procedures

Reusable SQL programs stored inside the database.

```sql
-- SQL Server syntax
CREATE PROCEDURE GetCustomers
AS
BEGIN
    SELECT *
    FROM Customers;
END;
```

**Benefits:** reusable logic, better security, easier maintenance.

> 💡 Syntax varies by database (PostgreSQL and MySQL use different forms).

---

<a id="triggers"></a>
## 13. 🔔 Triggers

Triggers **execute automatically** when an event occurs.

- **Events:** `INSERT`, `UPDATE`, `DELETE`
- **Common uses:** audit logs, data validation, business rules

---

# Part 5: Reliability & Workloads

<a id="acid"></a>
## 14. 🔒 ACID Properties

Transactions in relational databases follow **ACID**.

| Letter | Property | Meaning |
|--------|----------|---------|
| **A** | Atomicity | All operations succeed or none do |
| **C** | Consistency | The database remains valid |
| **I** | Isolation | Transactions do not interfere with each other |
| **D** | Durability | Committed data is permanently saved |

---

<a id="oltp-olap"></a>
## 15. 📊 OLTP vs OLAP

| Feature | OLTP | OLAP |
|---------|------|------|
| Purpose | Operations | Analytics |
| Queries | Small | Complex |
| Updates | Frequent | Rare |
| Data | Current | Historical |
| Design | Normalized | Denormalized |
| **Examples** | Banking, e-commerce | Power BI, data warehouses |

---

# Part 6: Industry & Career

<a id="industry"></a>
## 16. 🏆 Common Databases in Industry

| Database | Strengths |
|----------|-----------|
| **PostgreSQL** | ✅ Strong SQL compliance<br>✅ Excellent for analytics<br>✅ Advanced features |
| **MySQL** | ✅ Easy to learn<br>✅ Popular in web applications |
| **SQL Server** | ✅ Strong Microsoft ecosystem<br>✅ Widely used in enterprises |

---

<a id="perspective"></a>
## 17. 🎭 Data Analytics & Data Engineering Perspective

### 17.1 📈 Data Analyst

**Commonly:**

- Writes SQL queries
- Creates reports
- Builds dashboards
- Performs aggregations

**Most common SQL skills:** `SELECT`, `WHERE`, `GROUP BY`, `ORDER BY`, `HAVING`, `JOIN`, `CASE WHEN`, window functions.

### 17.2 ⚡ Data Engineer

**Commonly:**

- Builds pipelines
- Designs schemas
- Optimizes performance
- Creates ETL/ELT processes

**Important concepts:** partitioning, indexing, data warehousing, query optimization, star schema, snowflake schema.

---

<a id="cheatsheet"></a>
## 18. 🎓 Interview Cheat Sheet

| Concept | Key point |
|---------|-----------|
| Database | Stores data |
| RDBMS | Relational database software |
| SQL | Database language |
| PK | Unique identifier |
| FK | Relationship between tables |
| View | Virtual table |
| Index | Query acceleration |
| Procedure | Reusable SQL program |
| Trigger | Automatic execution |
| ACID | Reliable transactions |
| OLTP | Operational systems |
| OLAP | Analytical systems |
| Normalization | Reduce redundancy |

---

<a id="advice"></a>
## 19. 🚀 Final Advice

For data analytics and data engineering roles, focus on mastering:

1. SQL fundamentals
2. Joins
3. Aggregations
4. Window functions
5. Indexes
6. Transactions
7. Data warehousing concepts
8. Query optimization

These topics appear frequently in real projects and technical interviews.

---

<a id="resources"></a>
## 20. 📚 Resources

- [PostgreSQL Tutorial (W3Schools)](https://www.w3schools.com/postgresql/index.php)