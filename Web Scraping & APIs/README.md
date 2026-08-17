# APIs & Web Scraping

A notebook covering how to fetch and extract data from the web using **Requests** (for calling APIs and downloading pages) and **BeautifulSoup (bs4)** (for parsing and scraping HTML content).

## 📖 Overview

This folder focuses on two core skills for collecting data from the internet:
- **Working with APIs** — sending HTTP requests, handling responses, and parsing JSON data.
- **Web Scraping** — fetching raw HTML pages and extracting specific data (text, links, tables, etc.) using BeautifulSoup.

## 📂 Contents

| File | Overview |
|---|---|
| `APIs & web scraping.ipynb` | Hands-on notebook with code examples for making API requests and scraping web pages. |
| `APIs & web scraping.md` | Notes/summary explaining the concepts, functions, and workflow covered in the notebook. |

## 🧠 What You'll Find

- **Requests** — sending `GET`/`POST` requests, passing parameters/headers, handling status codes, and working with JSON responses.
- **BeautifulSoup (bs4)** — parsing HTML, selecting elements with tags/classes/ids, and extracting text, attributes, and links.
- Practical examples combining both: fetching a page or API endpoint, then parsing/structuring the returned data.

## ▶️ How to Run

1. **Install the required libraries**:
   ```bash
   pip install requests beautifulsoup4 jupyter
   ```

2. **Launch Jupyter Notebook** from this folder:
   ```bash
   jupyter notebook
   ```

3. Open `APIs & web scraping.ipynb` and run the cells (`Shift + Enter`) to see the requests and scraping results.

> 💡 Tip: Check `APIs & web scraping.md` for a quick conceptual summary before diving into the notebook code.

## 📚 Resources

- [Requests Documentation](https://requests.readthedocs.io/en/latest/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

---
*This README will be updated as more scraping/API examples are added to the folder.*
