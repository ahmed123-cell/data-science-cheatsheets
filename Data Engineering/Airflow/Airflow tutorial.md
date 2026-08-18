# 🌸 Apache Airflow

### Apache Airflow is an open-source platform designed to programmatically create, schedule, and monitor workflows, espcially data pipelines. It is widely used in data engineering and and machine learning projects because it allows complex workflows to be expressed as Python code and executed reliably as scale

---

## 🗝️ How to Manage Airflow using docker compose

- ```docker compose up -d```: Start the Airflow system and build containers

- ```docker compose down```: Stop the Airflow completely and remove containers

- ```docker compose start```: Restart the Containers

- ```docker compose down```: Stop the Containers without deleting them

- ```docker ps```: Shows all the Containers

- ```docker ps -a```: Show all the entire Containers

- ```docker compose down -v```: Stop the Airflow compleltely and remove Containers and volumes

- After that go to the browser and write ```http://localhost:8080/``` the username and password is: airflow

---

## ♻️ What a DAG is?

### A **DAG** stands for Directed Acyclic Graph. Each connection between tasks has a direction, showing the order of execution. No cycles are allowed -- meaning a task cannot depend on itself, directly or indirectly. This prevents infinite loops.

- A **DAG** defines the workflow structure: Which tasks run, in what order and under what conditions
- It is written in python code, making it dynamic and flexible.
- Each DAG has:
    - **Tasks** (unit of work, like running scripts or querying the database)
    - **Dependencies** (rules about which tasks must finish before others start)
    - **Schedule**  (when the DAG should run, e.g., daily at midnight)

---

## ⭕ What is Action Operators?

### They executes a specific action in your workflow. Each operator is a wrapper around a type of work, so you do not have rienvent the wheel every time

### 📓 Common Action Operators

1. **PythonOperator**
    - Runs a Python fucntion that you define.
    - Best for custome logic, data transformations, or calling APIs.

2. **BashOperator**
    - Executes a Bash command or script.
    - Useful for shell scripts,
    - command-line tools, or system tasks

3. **EmailOperator**
    - Sends emails from within a DAG.
    - Often used for alerts, notifications, or reporting

4. **EmpptyOperator**
    - very simple operator that does nothing when exectuted
    - It's essentially a placeholder or a structural tool used to organize workflows

---
# 🫰 Cron Syntax

#### Cron syntax is a way to define schedules for automated tasks in Unix/Linux systems. It uses five time fields (minute, hour, day of month, month, day of week) followed by the command to run. Special shortcuts like @daily or @weekly make common schedules easier. 

📘 Cron Syntax Structure
A cron expression has five fields plus the command:

```code
* * * * * command_to_run
│ │ │ │ │
│ │ │ │ └── Day of week (0–6, Sunday=0)
│ │ │ └──── Month (1–12)
│ │ └────── Day of month (1–31)
│ └──────── Hour (0–23)
└────────── Minute (0–59)
```

`*` (asterisk) → means “every possible value” for that field.

`,` (comma) → separates multiple values.

`-` (dash) → defines a range.

`/` (slash) → defines step values (e.g., every 5 minutes).

⏰ Examples of Cron Syntax
| Expression   | Meaning                                   |
|--------------|-------------------------------------------|
| `0 0 * * *`  | Run every day at midnight                 |
| `*/5 * * * *`| Run every 5 minutes                       |
| `0 9 * * 1`  | Run every Monday at 9:00 AM               |
| `30 14 1 * *`| Run at 2:30 PM on the 1st of every month  |
| `0 */2 * * *`| Run every 2 hours                         |

⚡ Special Strings (Shortcuts)
Instead of writing full expressions, cron supports keywords:

@hourly → Run at the start of every hour.

@daily → Run once a day at midnight.

@weekly → Run once a week (Sunday midnight).

@monthly → Run once a month (1st day midnight).

@yearly or @annually` → Run once a year (Jan 1 midnight). 

✅ Bottom Line
Cron syntax is a powerful scheduling language for automating tasks. It’s widely used in Linux, Unix, and tools like Apache Airflow (which uses cron-like expressions for DAG scheduling).

---

## 📨 Sensors

#### A **Sensors** is a special type of operator that waits for a condition to be met before allowing the workflow to continue. Unlike action operator (which performs tasks immediatly), sensorsare about **Pausing execution until something happens** -- for example, waiting for a file to arrive, a database query to return results, or another task to finish.

### 📓 Types of Sensors in Airflow
1. **DateTimeSensor** -> Waits until a specific date and time

2. **FileSensor** -> Waits for a file to appear in a directory

3. **ExternalTaskSensor** -> Waits for a task in another DAG to complete

4. **HttpSensor** -> Request a web URL and check for content

5. **SqlSensor** -> Runs a SQL query to check for content

---

## 🤚 SLAs

- An SLA stands for Service Level Agreement. Within Airflow, the amount of time a taskor a DAG should require to run. 

- An SLA Miss is any time the task / DAG does not meet the expected timing

- If an SLA is missed, an email is sent out and log is stored

- Can view SLA misses in the web UI

---

## 🕍 Templates

#### Templates are a way to make tasks dynamic by substituting values at runtime. Instead of hardcoding parameters (like file paths, dates, or SQL queries), you can jinja templating to insert variables that automatically resolves when the task runs.

### 🔑 What Templates Do
- Allow dynamic values in operators (e.g., `bash_command`, `sql`, `file`, `paths`).
- Use **Jinja2 syntax** (`{{ ... }}`) to reference Airflow variables, macros, or parameters.
- Enable workflows to adapt to different execution dates, environments, or configurations

### 📓 Common Templates Fields
Many operators have fiels that support templating. For example:
- **BashOperator** -> `bash_command`
- **PythonOperator** -> `op_args`, `op_kwargs`
- **SqlOperator** -> `sql`

---

### Templated BashOperator Example
```python
templated_command = """
    echo "Reading {{ params.filename }}"
"""

t1 = BashOperator(task_id='template_task',
                  bash_command=templated_command,
                  params={'filename': 'file1.txt'}
                  dag=example_dag)
```

---

### Another example
```python
templated_command = """
{% for filename in params.filenames %}
    echo "Reading {{ filename }}"
"""

t1 = BashOperator(task_id='template_task',
                  bash_command=templated_command,
                  params={'filenames': ['file1.txt', 'file2.txt']}
                  dag=example_dag)
```

---

### Useful Built-in Macros
- `{{ ds }}` -> Execution date (YYYY-MM-DD).
- `{{ ds_nodash }}` -> Execution date without dashses (YYYYMMDD)
- `{{ prev_ds }}`-> Previous execution date.
- `{{ next_ds }}` -> Next execution data.

---

## 🌿 Branching

#### Branching is the technique of making a workflow follow different paths depending on a condition. Instead of always running tasks in a fixed order, branching let's you decide which tasks should run and which be skipped at runtime 

### 🔑 How Branching Works
- Implemented using the BranchPythonOperator.  
- You define a Python function that returns the task_id(s) of the next task(s) to run.  
- Airflow will execute only the chosen branch and skip the others.  
- After branching, you can merge paths back together using an EmptyOperator (or other tasks).

---

```python 
from airflow import DAG
from airflow.operators.python import BranchPythonOperator, PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

def choose_branch():
    # Example condition: run task_a if today is Monday, else task_b
    import datetime
    if datetime.datetime.today().weekday() == 0:
        return "task_a"
    else:
        return "task_b"

with DAG(
    dag_id="branching_example",
    start_date=datetime(2026, 3, 17),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    branch = BranchPythonOperator(
        task_id="branching",
        python_callable=choose_branch
    )

    task_a = PythonOperator(
        task_id="task_a",
        python_callable=lambda: print("Running branch A")
    )

    task_b = PythonOperator(
        task_id="task_b",
        python_callable=lambda: print("Running branch B")
    )

    end = EmptyOperator(task_id="end")

    branch >> [task_a, task_b]  # branch chooses one
    task_a >> end
    task_b >> end
```

---