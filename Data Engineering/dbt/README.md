# dbt (Data Build Tool)

#### ⚙️dbt is an open-source framework that helps teams transorm raw data in their warehouses into clean reliable, and well-documentated datasets using SQL and sofrware engineering best practices. It focuses on the "T" in ETL, making transformation modular, testable, and version controlled.

---

## 🧩Components of dbt 

##### 📳1. Models: SQL files that define transformations, dbt compiles these sql files into queries that run in your warehouse, creating tables or views

##### 🌱2. Seeds: Static CSV files you include in your project. Useful for small reference datasets that don't change often. dbt loads theses CSVs into the warehouse as tables

##### 🧪3. Tests: Assertions that defined to check data quality. They catch issues early insuring trust in the data .there are two types:
- **Generic tests**: Built-in checks like (unique, not_null, accepted_values)
- **Custom tests**: SQL queries that written to validate specific conditions

##### 📷4. Snapshots: A way to track changes in data over time. If you want to see how a record evolves, snapshots capture historical versions. dbt compares current data with previous run and stores differences.

##### 📠5. Macros: Reusable SQL snippets written in jinja (a pythonic templating language). Automate repetitive logic, parameterize queries, and make transformations more flexible.

--- 

## ✨Popular dbt commands

#### ⛏️Setup & Debugging
- ```dbt init < project_name >```: Creates a new dbt project with the standard folder structure
- ```dbt debug```: Checks the connection to the data warehouse and validates configurations

#### ✅ Testing
- ``` dbt test ```: Runs all tests defined in the project (data quality checks)
- ```dbt test --select <model_name>```: Runs tests only for the specified model

#### ▶️ Running Models
- ```dbt run```: Executes all models (SQL transformations) in the project
- ```dbt run -f```: Forces dbt to rebuild models even if they already exist

#### 📂 Seeds
- ```dbt seed```: Loads CSV files from the ```seeds/``` directory into teh warehouse as tables

#### 📖 Documentation
- ```dbt docs```: General command for documentation tasks
- ```dbt docs generate```: Build documentation and lineage graph from the project
- ```dbt docs serve```: Spins up a local web server to view the docs in a browser.

#### 🕒 Snapshots
- ```dbt snapshot```: Runs all snapshot definitions (track historical changes in data)
- ```dbt snapshot -s <snapshot_name>```: Runs a specific snapshot only.

#### 🏗️ Build (All-in-One)
- ```dbt build```: Runs models, seeds, snapshots, and tests together in one command
- ```dbt build --select <object>```: Builds only the specified object (model, seed, snapshot)
- ```dbt build -d```: Dry run mode -- shows what would be built without executing 
- ```dbt build --exclude <object>```: Builds everyting except the specified object

#### 📝 Compilation
- ```dbt compile```: Compiles SQL models into raw SQL files without running them
- ```dbt compile -s <modelname>```: Compiles only the specified model

#### 🧹Cleaning
- ```dbt clean```: Deletes temporary fiels, logs, artifacts created by dbt (like ```target/```)

---

## 🥊dbt_project.yml VS Profiles.yml

##### 📂 ```dbt_project.yml```: Defines the structure and behavior of the dbt project itself. It contains project name, version and configuration, Folder Paths (where models, seeds, snapshots, test live), model-specific settings (materializations, tags, configs), Dependencies (packages). The purpose is telling dbt what to do with SQL files and how to organize them

##### 🔑 ```profiles.yml```: Defines connection details to the data warehouse. The contents are Credentials (user, password, key), the target enviroment(dev, prod, staging). Warehouse-specific settings (schema, threads, timeout). The purpose is telling dbt where to run the SQL transformations dedined in the project

---

## 🧰ref() VS source() 

##### 🔑```ref()``` is used to reference another model in the project, It ensures proper dependency management and ordering. dbt builds models in the correct sequence based on these references
```sql
    SELECT * FROM {{ ref('orders') }}  --> This tells dbt: "Use the compiled version of the 'orders' model"
```

##### 🗝️```source()``` is used to reference raw table in the warehouse (not dbt models). You define sources in YAML, then call them in SQL. This makes lineage clear and allows testing raw data. Cand find the defining the sources YAML in ```models/source.yml```
```sql
    SELECT * FROM {{ source('raw', 'customers') }} --> This tells dbt: "Use the raw 'customers' table defined in my sources"
```
##### ❗Can find the defining the seeds YAML in ```seeds/seeds.yaml```

---

## 📃 dbt testing setup

#### Generic Tests: Built in dbt function tests: [unique, not_null, accepted_values, relationships]: Can find the apply in ```models/schema.yml```

#### Singular Tests: Custom SQL queries stored in ```tests/``` folder. They should return **0 rows** if the rests passes. can find the apply in ```tests/no_future_orders.sql```

#### Reusable Custome Tests: Defined as macros in ```macros/``` folder, then referenced in ```schema.yml```. Can find the apply in ```macros/test_positive_values.sql```

---

## 🎥 dbt snapshot setup
- **target_schema**: where the snapshot table will be stored
- **unique_key**: identifies each record uniquely
- **strategy**: how dbt detects changes: 
    - *timestamp*: uses an *updated_at* column
    - *check*: compares selected fields for changes
    - *updated_at*: column used to detect when a record was last modified
- **SQL query**: Defines the source data wanted to snapshot

##### 🎥Can find apply of snapshots in ```snapshots\orders_snapshot.sql```

--- 

## 🧩 What is Jinja?

##### - **Jinja** is a templating language (originally for python) that dbt uses to make SQL dynamic and reusable.
##### - It lets you embed logic (variables, loops, conditionals) inside you SQL models, macros and tests.
##### - Syntax uses `{% ... %}` for statements and ```{{ ... }}``` for expressions. Can find the apply of jinja in ```models/marts/jinja_example.sql```

---

## Ⓜ️ dbt macro setup

##### Can find the apply of macro in ```macro/calculate_customer_revenue```
----

## 📚 Resources

- [dbt](https://youtu.be/us1rf2iynOY?si=jyRr8H6H7HFgJqYk)