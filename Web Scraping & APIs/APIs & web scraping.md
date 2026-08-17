# 🚀 Understanding APIs, REST, Status Codes & Web Scraping

A beginner-friendly guide to key web technologies.

## What is an API? 📡

**API** stands for **Application Programming Interface**.

An API is a set of rules and protocols that allows different software applications to communicate with each other. Think of it as a **menu in a restaurant**: you (the client) order food (request data/functionality) through the waiter (API), and the kitchen (server) prepares and sends it back.

### Key Benefits:
- **Reusability**: Build once, use everywhere
- **Integration**: Connect different systems easily
- **Abstraction**: Hide complex implementation details
- **Security**: Control what external apps can access

**Example**: When your weather app shows today's forecast, it's using an API from a weather service.

---

## What is a REST API? 🛠️

**REST** stands for **Representational State Transfer**.

A REST API is a specific architectural style for designing networked applications. It uses standard HTTP methods and is stateless, scalable, and widely used.

### Core Principles of REST:
1. **Client-Server Architecture**
2. **Stateless** (each request contains all info needed)
3. **Cacheable** responses
4. **Uniform Interface** (resources identified by URLs)
5. **Layered System**

### Common HTTP Methods in REST:
- `GET` → Retrieve data
- `POST` → Create new resource
- `PUT` → Update/replace resource
- `DELETE` → Remove resource
- `PATCH` → Partial update

**Example URL**: `https://api.example.com/users/123`

---

## Popular HTTP Status Codes ✅

HTTP status codes are the server's way of telling you how the request went. They're grouped into classes:

- **200 OK** — Success 🎉. Everything worked perfectly.
- **404 Not Found** — Error ❌. Resource doesn't exist
- **401 Unauthorized** — Error ❌. Authentication required
- **500 Internal Server Error** — Server Errors 💥. Something broke on the server
---


## What is Web Scraping? 🕸️

**Web Scraping** is the process of automatically extracting data from websites.

Instead of manually copying information, a program visits web pages, parses the HTML, and pulls out the data you want (prices, headlines, product info, etc.).

### How It Works:
1. Send HTTP request to a webpage
2. Download the HTML content
3. Parse the HTML (using libraries like BeautifulSoup in Python)
4. Extract specific elements (by tags, classes, IDs)
5. Save or process the data

### Common Use Cases:
- Price comparison
- Market research
- News aggregation
- Data collection for ML

### ⚠️ Important Notes:
- Respect `robots.txt`
- Don't overload servers (use delays)
- Check legal/terms of service
- Many sites provide official APIs instead (preferred)

**Popular Tools**: Python (Requests + BeautifulSoup/Scrapy), Selenium (for dynamic sites).

---

## Summary 🎯

- **API**: Contract for software communication
- **REST API**: Popular, HTTP-based API style
- **Status Codes**: Universal language for request results
- **Web Scraping**: Automated data extraction from websites

**Pro Tip**: Always prefer official APIs over scraping when available! 

---

### 🔑 Params vs Headers

- **Query Params**: Key-value pairs added to the **URL** after `?` to filter, search, or pass data to the server (e.g., `?page=1&limit=10`).
- **Headers**: Metadata sent in the **request/response** envelope (not in URL) for authentication, content type, authorization, etc. (e.g., `Authorization: Bearer token`).

- **Main Difference**: Params are **part of the URL** (visible, cacheable, for filtering data); Headers are **separate** (hidden from URL, used for control & security).
- **When to use Params**: For filtering, pagination, or search queries.
- **When to use Headers**: For authentication, API keys, content negotiation, and custom metadata.