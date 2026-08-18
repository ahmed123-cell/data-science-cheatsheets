# 🏗️ Databases & SQL for Data Analytics and Data Engineering

# 📚 Table of Contents

1. Introduction to Databases
2. Database vs Data Warehouse
3. What is an RDBMS?
4. Database Objects
5. SQL Fundamentals
6. DDL, DML, DQL, DCL, TCL
7. Keys and Relationships
8. Constraints
9. Indexes
10. Views
11. Stored Procedures
12. Triggers
13. ACID Properties
14. Normalization
15. OLTP vs OLAP
16. Common Databases in Industry
17. Data Analytics & Data Engineering Perspective
18. Interview Cheat Sheet

---

# 🎯 Introduction to Databases

A database is a structured system used to store, organize, manage, and retrieve data efficiently.

Examples:

- Banking systems
- E-commerce platforms
- Social media applications
- Healthcare systems
- Business intelligence platforms

Without databases, modern software would not be able to manage large volumes of data reliably.

---

# 🏢 Database vs Data Warehouse

## Database (OLTP)

Designed for day-to-day operations.

Examples:

- Creating orders
- Updating customer information
- Processing transactions

Characteristics:

- Frequent inserts and updates
- Small transactions
- Highly normalized

---

## Data Warehouse (OLAP)

Designed for analytics and reporting.

Examples:

- Sales dashboards
- Business reports
- Trend analysis

Characteristics:

- Large analytical queries
- Historical data
- Aggregations
- Denormalized structures

---

# 🗄️ What is an RDBMS?

RDBMS = Relational Database Management System

Data is stored in tables:

| CustomerID | Name |
|------------|------|
| 1 | Ahmed |
| 2 | Sara |

Relationships are created between tables using keys.

Popular RDBMS systems:

- PostgreSQL
- MySQL
- SQL Server
- Oracle
- SQLite

---

# 🧱 Database Objects

Common database objects:

| Object | Purpose |
|----------|----------|
| Table | Store data |
| View | Virtual table |
| Index | Speed up queries |
| Stored Procedure | Reusable SQL program |
| Trigger | Automatic execution |
| Schema | Logical organization |
| Function | Return values from calculations |

---

# 💻 What is SQL?

SQL = Structured Query Language

SQL is used to:

- Create structures
- Insert records
- Update records
- Delete records
- Query data
- Manage permissions

Example:

```sql
SELECT *
FROM Customers;
```

---

# ⚙️ SQL Categories

## DDL (Data Definition Language)

Used to define structures.

Commands:

```sql
CREATE
ALTER
DROP
TRUNCATE
```

Example:

```sql
CREATE TABLE Customers(
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100)
);
```

---

## ✏️ DML (Data Manipulation Language)

Used to manipulate records.

Commands:

```sql
INSERT
UPDATE
DELETE
```

---

## 🔍 DQL (Data Query Language)

Used to retrieve data.

Command:

```sql
SELECT
```

---

## 🔒 DCL (Data Control Language)

Controls permissions.

Commands:

```sql
GRANT
REVOKE
```

---

## 🔄 TCL (Transaction Control Language)

Controls transactions.

Commands:

```sql
COMMIT
ROLLBACK
SAVEPOINT
```

---

# 🔑 Keys and Relationships

## Primary Key

Uniquely identifies each row.

```sql
CustomerID
```

Properties:

- Unique
- Cannot be NULL

---

## Foreign Key

Creates relationships between tables.

Example:

Orders table references Customers table.

```sql
CustomerID
```

---

## Relationship Types

### One-to-One (1:1)

One employee ↔ one badge

### One-to-Many (1:N)

One customer ↔ many orders

### Many-to-Many (M:N)

Many students ↔ many courses

---

# 🛡️ Constraints

Constraints improve data quality.

Common constraints:

```sql
PRIMARY KEY
FOREIGN KEY
UNIQUE
NOT NULL
CHECK
DEFAULT
```

Example:

```sql
Age INT CHECK(Age >= 18)
```

---

# 🚀 Indexes

Indexes improve query performance.

Without index:

```text
Full Table Scan
```

With index:

```text
Direct Lookup
```

Example:

```sql
CREATE INDEX idx_customer_name
ON Customers(Name);
```

Benefits:

- Faster filtering
- Faster joins
- Faster sorting

Trade-off:

- Additional storage
- Slower writes

---

# 👀 Views

A view is a virtual table generated from a query.

Example:

```sql
CREATE VIEW ActiveCustomers AS
SELECT *
FROM Customers
WHERE Status = 'Active';
```

Advantages:

- Security
- Simplicity
- Reusability

---

# ⚙️ Stored Procedures

Reusable SQL programs stored inside the database.

Example:

```sql
CREATE PROCEDURE GetCustomers
AS
BEGIN
    SELECT *
    FROM Customers;
END;
```

Benefits:

- Reusable logic
- Better security
- Easier maintenance

---

# 🔔 Triggers

Triggers execute automatically when an event occurs.

Events:

```sql
INSERT
UPDATE
DELETE
```

Common uses:

- Audit logs
- Data validation
- Business rules

---

# 🔒 ACID Properties

Transactions in relational databases follow ACID.

## A — Atomicity

All operations succeed or none succeed.

## C — Consistency

Database remains valid.

## I — Isolation

Transactions do not interfere.

## D — Durability

Committed data is permanently saved.

---

# 📏 Normalization

Normalization reduces redundancy.

## 1NF

- No repeating groups
- Atomic values

## 2NF

- Remove partial dependencies

## 3NF

- Remove transitive dependencies

Example:

Bad:

```text
CustomerID | CustomerName | CityName
```

Better:

```text
Customers Table
Cities Table
```

Benefits:

- Less duplication
- Better consistency

Trade-off:

- More joins

---

# 📊 OLTP vs OLAP

| Feature | OLTP | OLAP |
|----------|----------|----------|
| Purpose | Operations | Analytics |
| Queries | Small | Complex |
| Updates | Frequent | Rare |
| Data | Current | Historical |
| Design | Normalized | Denormalized |

Examples:

OLTP:
- Banking
- E-commerce

OLAP:
- Power BI
- Data Warehouses

---

# 🏆 Common Databases in Industry

## PostgreSQL

✅ Strong SQL compliance

✅ Excellent for analytics

✅ Advanced features

---

## MySQL

✅ Easy to learn

✅ Popular in web applications

---

## SQL Server

✅ Strong Microsoft ecosystem

✅ Widely used in enterprises

---

# 📈 Data Analytics Perspective

A Data Analyst commonly:

- Writes SQL queries
- Creates reports
- Builds dashboards
- Performs aggregations

Most common SQL skills:

```sql
SELECT
WHERE
GROUP BY
ORDER BY
HAVING
JOIN
CASE WHEN
WINDOW FUNCTIONS
```

---

# ⚡ Data Engineering Perspective

A Data Engineer commonly:

- Builds pipelines
- Designs schemas
- Optimizes performance
- Creates ETL/ELT processes

Important concepts:

- Partitioning
- Indexing
- Data Warehousing
- Query Optimization
- Star Schema
- Snowflake Schema

---

# 🎓 Interview Cheat Sheet

| Concept | Key Point |
|----------|------------|
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

# 🚀 Final Advice

For Data Analytics and Data Engineering roles, focus on mastering:

1. SQL fundamentals
2. Joins
3. Aggregations
4. Window Functions
5. Indexes
6. Transactions
7. Data Warehousing Concepts
8. Query Optimization

These topics appear frequently in real projects and technical interviews.
---

## 📚 Resources

- [PostgreSQL Tutorial — W3Schools](https://www.w3schools.com/postgresql/index.php)