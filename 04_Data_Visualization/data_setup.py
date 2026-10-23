import numpy as np
from datetime import datetime, timedelta

def plot_data():
    np.random.seed(42)
    x = np.linspace(0, 10, 50)

    y1 = np.sin(x) + np.random.normal(0, 0.1, 50)
    y2 = np.cos(x) + np.random.normal(0, 0.15, 50)
    y3 = np.sin(x + np.pi / 4) * 0.8 + np.random.normal(0, 0.1, 50)

    return x, y1, y2, y3

def bar_data(categories):
    np.random.seed(7)
    x = np.arange(len(categories))

    # Data
    y1 = np.random.randint(30, 100, len(categories))
    y2 = np.random.randint(30, 100, len(categories))
    y3 = np.random.randint(30, 100, len(categories))

    return x, y1, y2, y3

def barh_data():
    np.random.seed(7)

    categories = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
    values = np.random.randint(30, 100, len(categories))

    return categories, values

def pie_data():
    np.random.seed(21)

    labels  = ['Python', 'JavaScript', 'Java', 'C++', 'Rust', 'Go']
    x       = np.random.randint(15, 35, len(labels)).astype(float)
    colors  = ['#3498DB', '#F1C40F', '#E74C3C', '#2ECC71', '#9B59B6', '#E67E22']
    explode = [0.08, 0, 0, 0, 0, 0]

    return labels, x, colors, explode

def stack_data():
    np.random.seed(13)

    x      = np.arange(2015, 2025)
    python = np.random.randint(20, 35, 10).astype(float)
    js     = np.random.randint(15, 30, 10).astype(float)
    java   = np.random.randint(10, 25, 10).astype(float)
    cpp    = np.random.randint(8,  20, 10).astype(float)
    rust   = np.random.randint(3,  12, 10).astype(float)

    # ===== Set The Parameters ===== # 
    labels = ['Python', 'JavaScript', 'Java', 'C++', 'Rust']
    colors = ['#3498DB', '#F1C40F', '#E74C3C', '#2ECC71', '#9B59B6']

    return x, python, js, java, cpp, rust, labels, colors

def area_data():
    np.random.seed(5)

    x  = np.linspace(0, 10, 300)
    y1 = np.sin(x) + np.random.normal(0, 0.08, 300)        # signal A
    y2 = np.cos(x) * 0.8 + np.random.normal(0, 0.08, 300)  # signal B

    return x, y1, y2

def histogram_data():
    np.random.seed(42)
    x = np.random.normal(loc=170, scale=10, size=1000)

    mean = x.mean()
    std  = x.std()

    return x, mean, std

def scatter_data1():
    np.random.seed(42)
    x = np.random.rand(100)
    y = np.random.rand(100)
    s = np.random.rand(100) * 200
    c = np.random.rand(100)

    return x, y, s, c

def scatter_data2():
    np.random.seed(7)

    x = np.arange(1, 51)
    y = 2 * x + np.random.normal(0, 10, len(x))
    c = np.random.rand(len(x))

    return x, y, c

def box_data():
    np.random.seed(42)
    data = [
        np.random.normal(0, 1, 100),      # Group 1
        np.random.normal(2, 1.5, 100),    # Group 2  
        np.random.normal(1, 1.2, 100),    # Group 3
        np.random.normal(3, 0.8, 100)     # Group 4
    ]

    labels = ['Group A', 'Group B', 'Group C', 'Group D']

    return data, labels

def time_series_data():
    np.random.seed(42)
    start_date = datetime(2025, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(90)]

    # More random large values (in millions scale)
    values = np.cumsum(np.random.randn(90) * 0.8) * 1_200_000 + 25_000_000

    return dates, values