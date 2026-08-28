# Streamlit Explained

## What is Streamlit?

**Streamlit** is an open-source Python library that allows you to create beautiful, interactive web applications for data science, machine learning, and data visualization with just a few lines of Python code.

It turns Python scripts into shareable web apps in minutes — no front-end (HTML, CSS, JavaScript) knowledge required.

**Ideal for**: Quickly building ML model demos, data dashboards, and interactive tools.

---

## Main Streamlit Functions

Here are the most commonly used Streamlit commands:

### Display Elements

```python
import streamlit as st

st.title("My App Title")                    # Main title
st.header("Header")                         # Section header
st.subheader("Subheader")                   # Smaller header
st.text("Plain text")                       # Simple text
st.markdown("**Bold** and *italic* text")   # Markdown support
st.latex(r"\int_a^b f(x) dx")               # LaTeX math
st.code("print('Hello')", language="python") # Code block
```

### Data Display

```python
st.dataframe(df)          # Interactive table
st.table(df)              # Static table
st.json(data)             # Display JSON
st.metric("Accuracy", "92%", "↑ 3%")  # KPI metric
```

### Input Widgets

```python
name = st.text_input("Enter your name")
age = st.number_input("Age", min_value=0, max_value=100)
option = st.selectbox("Choose model", ["RandomForest", "XGBoost", "SVM"])
date = st.date_input("Select date")
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if st.button("Predict"):          # Button
    st.success("Prediction done!")
```

### Layout

```python
st.sidebar.title("Settings")           # Sidebar
col1, col2 = st.columns(2)             # Two columns
with col1:
    st.write("Left column")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])  # Tabs
with tab1:
    st.write("Content 1")
```

### Media & Charts

```python
st.image("image.png")
st.audio("audio.mp3")
st.video("video.mp4")

st.line_chart(data)
st.bar_chart(data)
st.scatter_chart(data)
st.map(df)                     # For geospatial data
```

### Status & Progress

```python
st.spinner("Loading model...")     # Loading spinner

with st.spinner("Training..."):
    # your code

st.progress(75)                    # Progress bar

st.success("Success message")
st.error("Error message")
st.warning("Warning message")
st.info("Info message")
```

### Caching (Very Important for ML)

```python
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

@st.cache_data
def load_data():
    return pd.read_csv("data.csv")
```

---

**Run the app:**
```bash
streamlit run app.py
```