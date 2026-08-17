# Data Visualization

A collection of notebooks and scripts covering data visualization in Python using **Matplotlib** and **Seaborn** — the two most widely used plotting libraries for exploring and presenting data.

## 📖 Overview

This folder focuses on learning how to create clear, styled, and informative charts — from basic line and bar plots to statistical visualizations like violin plots, KDE plots, and heatmaps. Each notebook includes a short docstring above every plot explaining its key parameters, followed by a simplified example so you can quickly copy, adapt, and reuse the code.

## 📂 Contents

| File | Overview |
|---|---|
| `data_setup.py` | Generates/loads the datasets (random data + built-in datasets like `tips`, `iris`, `penguins`) used across both notebooks. Run this first before the tutorials. |
| `matplotlib_tutorial.ipynb` | Core Matplotlib plots — line charts, bar charts, pie charts, stack plots, fill_between, histograms, scatter plots, box plots, violin plots, and heatmaps. |
| `seaborn_tutorial.ipynb` | Core Seaborn plots — line, bar, scatter, histogram, KDE, box, violin, strip/swarm, heatmap, and regression (`lmplot`) plots, with built-in styling and statistical features. |

## ▶️ How to Run

1. **Install the required libraries**:
   ```bash
   pip install matplotlib seaborn pandas numpy jupyter notebook
   ```

4. Open `matplotlib_tutorial.ipynb` or `seaborn_tutorial.ipynb` and run the cells (`Shift + Enter`) to see each plot rendered instantly.

## 🧠 What You'll Find in Each Notebook

- A short `"""docstring"""` above each plot type explaining its most useful parameters.
- A simplified, minimal version of the plot — enough to understand and reuse without memorizing every parameter.
- Consistent styling patterns (titles, labels, legends, grids) across chart types.

> 💡 Tip: You don't need to memorize every parameter. Use an AI tool (ChatGPT, Claude, etc.) to explain any parameter or line of code you're unsure about, and treat these notebooks as a quick reference whenever you want to plot something.

## 📚 Resources

- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)

---
*This README will be updated as more visualization notebooks or scripts are added to the folder.*
