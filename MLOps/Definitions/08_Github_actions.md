# GitHub Actions Explained

A clear guide to the core components of GitHub Actions.

---

## What is GitHub Actions?

**GitHub Actions** is GitHub’s built-in CI/CD and automation platform.  
It lets you automate software workflows directly in your repository — building, testing, deploying, labeling issues, releasing packages, and much more.

Workflows are defined as **YAML files** stored in:

```
.github/workflows/
```

---

## Core Components Overview

| Component     | Description                                      |
|---------------|--------------------------------------------------|
| **Workflow**  | The entire automated process (YAML file)         |
| **Event**     | What triggers the workflow to run                |
| **Job**       | A set of steps that run on the same runner       |
| **Runner**    | The machine (VM or container) that executes a job|
| **Step**      | An individual task inside a job                  |
| **Action**    | A reusable piece of code that performs a task    |

---

## 1. Workflows

A **workflow** is a configurable automated process made up of one or more jobs.

- Defined in YAML files under `.github/workflows/`
- A repository can have many workflows
- Each workflow can be triggered independently

**Example structure:**

```yaml
name: CI Pipeline          # Optional display name

on:                        # Events that trigger the workflow
  push:
    branches: [main]

jobs:                      # One or more jobs
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm test
```

---

## 2. Events (Triggers)

An **event** is an activity that triggers a workflow run.

Common events:

| Event              | Description                              |
|--------------------|------------------------------------------|
| `push`             | Code is pushed to a branch               |
| `pull_request`     | A pull request is opened or updated      |
| `schedule`         | Runs on a cron schedule                  |
| `workflow_dispatch`| Manually triggered from the GitHub UI    |
| `release`          | A release is published                   |
| `issues`           | An issue is created or modified          |

**Example:**

```yaml
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 2 * * 1'   # Every Monday at 02:00 UTC
  workflow_dispatch:      # Allows manual runs
```

---

## 3. Jobs

A **job** is a collection of **steps** that execute on the **same runner**.

Key characteristics:

- Jobs run **in parallel** by default
- You can make jobs run sequentially using `needs`
- Each job gets a fresh virtual machine (or container)
- Jobs can share data through **artifacts** or **caches**

**Example with dependencies:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run build

  test:
    needs: build              # Waits for the build job to finish
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm test
```

### Matrix Jobs

You can run the same job with different configurations using a **matrix**:

```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node-version: [18, 20, 22]
```

---

## 4. Runners

A **runner** is the server (or virtual machine) that executes a job.

### Types of Runners

| Type                  | Description                                      | Best for                     |
|-----------------------|--------------------------------------------------|------------------------------|
| **GitHub-hosted**     | Managed by GitHub (Ubuntu, Windows, macOS)       | Most projects                |
| **Larger runners**    | More powerful GitHub-hosted machines             | Heavy builds / more CPU/RAM  |
| **Self-hosted**       | Your own machines registered with GitHub         | Special hardware, private networks, cost control |

**Common labels for GitHub-hosted runners:**

- `ubuntu-latest`
- `windows-latest`
- `macos-latest`

```yaml
jobs:
  build:
    runs-on: ubuntu-latest   # Specifies the runner
```

> Each runner can only run **one job at a time**.  
> After the job finishes, the runner environment is discarded (for GitHub-hosted runners).

---

## 5. Steps

A **step** is an individual task inside a job.

Steps:

- Run **sequentially** (one after another)
- Share the same filesystem and environment
- Can be either:
  - A shell command (`run:`)
  - An action (`uses:`)

**Example:**

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v4

  - name: Setup Node.js
    uses: actions/setup-node@v4
    with:
      node-version: '20'

  - name: Install dependencies
    run: npm ci

  - name: Run tests
    run: npm test
```

---

## 6. Actions

An **action** is a reusable unit of code that performs a specific task.

You can:

- Use official actions from GitHub
- Use community actions from the [GitHub Marketplace](https://github.com/marketplace?type=actions)
- Write your own custom actions

**Common official actions:**

| Action                        | Purpose                        |
|-------------------------------|--------------------------------|
| `actions/checkout`            | Checks out your repository     |
| `actions/setup-node`          | Sets up a Node.js environment  |
| `actions/setup-python`        | Sets up a Python environment   |
| `actions/cache`               | Caches dependencies            |
| `actions/upload-artifact`     | Uploads build artifacts        |
| `actions/download-artifact`   | Downloads artifacts            |

**Example of using an action:**

```yaml
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'
```

---

## Putting It All Together

Here is a complete, realistic example:

```yaml
name: Node.js CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18, 20, 22]

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test

      - name: Upload coverage
        if: success()
        uses: actions/upload-artifact@v4
        with:
          name: coverage-report
          path: coverage/
```

---

## Quick Reference: Component Hierarchy

```
Workflow (YAML file)
│
├── Event (on:)               ← What triggers the workflow
│
└── Jobs
    │
    ├── Job 1
    │   ├── Runner (runs-on:)
    │   └── Steps
    │       ├── Step 1 (action or script)
    │       ├── Step 2
    │       └── Step 3
    │
    └── Job 2 (can depend on Job 1 via needs:)
        ├── Runner
        └── Steps
```

---

## Useful Links

- [Official GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Understanding GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Events that Trigger Workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)
- [GitHub Marketplace – Actions](https://github.com/marketplace?type=actions)

---
