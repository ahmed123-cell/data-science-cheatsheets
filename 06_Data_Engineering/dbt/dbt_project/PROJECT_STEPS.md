**Here is the full content of `PROJECT_STEPS.md`**


# dbt Project - Step by Step Guide

This document summarizes all the steps we followed to build a clean and professional dbt project using the Olist Brazilian E-commerce dataset.

## 1. Seed Configuration

- Created `data/` folder and placed all CSV files inside it (`customers.csv`, `orders.csv`, `order_items.csv`, `payments.csv`, `products.csv`).
- Updated `dbt_project.yml` to configure the seed path:

```yaml
seed-paths: ["data"]
```

- Loaded the raw data into the database:
  ```bash
  dbt seed
  ```

## 2. Staging Layer (`models/staging/`)

Created the following staging models:

- `stg_customers.sql`
- `stg_orders.sql`
- `stg_order_items.sql`
- `stg_payments.sql`
- `stg_products.sql`

**Purpose**: Clean raw data, cast data types, and add light transformations.

## 3. Tests (`models/staging/schema.yml`)

- Added standard tests (`unique`, `not_null`)
- Created custom positive values test using macros

## 4. Macros (`macros/utils.sql`)

Created reusable Jinja macros:
- `positive_values()` — Custom test to ensure columns have only positive values
- `calculate_order_metrics()` — Reusable order aggregation logic
- `flag_high_value_order()` — Business flag for high value orders

## 5. Jinja Example (`models/jinja_example.sql`)

Demonstrated advanced Jinja usage:
- Variables with `{% set %}`
- For loops
- If / else conditions
- Dynamic column generation

## 6. Data Marts (`models/marts/`)

Created:
- `fct_orders.sql` — Main fact table with joins, aggregations, and business metrics

## 7. Snapshots (`snapshots/orders_snapshot.sql`)

Created a snapshot on orders using **timestamp strategy** to track historical changes (especially `order_status` and delivery timestamps).

## 8. Project Structure

```
dbt_project/
├── data/                          # CSV seed files
├── models/
│   ├── staging/
│   │   ├── stg_customers.sql
│   │   ├── stg_orders.sql
│   │   ├── stg_order_items.sql
│   │   ├── stg_payments.sql
│   │   ├── stg_products.sql
│   │   └── schema.yml
│   ├── marts/
│   │   └── fct_orders.sql
│   └── jinja_example.sql
├── macros/
│   └── utils.sql
├── snapshots/
│   └── orders_snapshot.sql
├── dbt_project.yml
└── PROJECT_STEPS.md
```

---

## Commands Summary

```bash
dbt seed
dbt run --select staging
dbt run --select fct_orders
dbt run --select jinja_example
dbt snapshot
dbt test
dbt docs generate && dbt docs serve
```

---

**Project follows dbt best practices**: Staging → Marts architecture with proper testing, macros, and Jinja usage.