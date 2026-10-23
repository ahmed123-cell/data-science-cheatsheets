# Unsupervised Learning

A structured guide to dimensionality reduction and clustering algorithms.

## Contents

- [Dimension Reduction in Machine Learning 📉](#dimension-reduction-in-machine-learning-)
- [K-Means Clustering in Machine Learning 🔀](#k-means-clustering-in-machine-learning-)
- [Hierarchical Clustering in Machine Learning 🌳](#hierarchical-clustering-in-machine-learning-)
- [DBSCAN in Machine Learning 🟢](#dbscan-in-machine-learning-)

---

## Dimension Reduction in Machine Learning 📉

**Dimensionality Reduction** refers to techniques that reduce the number of input features (dimensions) while preserving as much important information as possible. It helps with the **Curse of Dimensionality**, improves model performance, reduces computation time, and enables visualization of high-dimensional data.

---

### Principal Component Analysis (PCA) 🔄

**PCA** is the most popular linear dimensionality reduction technique. It transforms the original features into a new set of **uncorrelated variables** called **Principal Components**, ordered by the amount of variance they explain.

#### How PCA Works (Linear Algebra Perspective) 🧮

1. **Standardize the Data**: Center the data (subtract mean) so each feature has zero mean. (Optional: scale to unit variance).

2. **Compute the Covariance Matrix**:
   $$
   \Sigma = \frac{1}{n-1} X^T X
   $$
   This matrix captures how features vary together.

3. **Eigen Decomposition**:
   - Find the **eigenvectors** and **eigenvalues** of the covariance matrix.
   - Eigenvectors represent the directions (new axes) of maximum variance.
   - Eigenvalues represent the amount of variance explained by each eigenvector.

4. **Select Principal Components**:
   - Sort eigenvectors by their eigenvalues (largest to smallest).
   - Choose the top $k$ eigenvectors (where $k$ is the desired number of dimensions).

5. **Project the Data**:
   $$
   X_{\text{new}} = X \cdot W
   $$
   Where $W$ is the matrix of selected eigenvectors.

**Key Concepts**:
- Principal components are **orthogonal** (perpendicular) to each other.
- The first principal component captures the **maximum variance**.
- The second captures the next highest variance while being orthogonal to the first, and so on.

**Advantages** ✅:
- Unsupervised (no need for labels)
- Linear and computationally efficient
- Reduces noise and redundancy

**Limitations** ❌:
- Linear only (cannot capture complex non-linear manifolds)
- Hard to interpret the new components

---

### Other Dimensionality Reduction Algorithms

#### t-SNE (t-Distributed Stochastic Neighbor Embedding) 🌀
**t-SNE** is a **non-linear** technique primarily used for **visualization** (reducing to 2D or 3D).

- It models similarities between points using probability distributions.
- In high dimensions: Uses Gaussian distribution.
- In low dimensions: Uses Student’s t-distribution (heavier tails to avoid crowding).
- Minimizes the difference between these two distributions (using Kullback-Leibler divergence).

**Best for**: Exploring clusters and manifolds in data.  
**Drawbacks**: Not great for new data (no explicit mapping), computationally expensive, and results can vary between runs.

#### UMAP (Uniform Manifold Approximation and Projection) 🌌
**UMAP** is a modern, fast, and scalable **non-linear** technique that often produces better visualizations than t-SNE while preserving more global structure.

- Based on **manifold learning** and topological data analysis.
- Constructs a high-dimensional graph of nearest neighbors, then optimizes a low-dimensional representation.
- Faster and more scalable than t-SNE.
- Supports both supervised and unsupervised modes.

**Strengths**: Better at preserving both local and global structure, faster, and consistent.

#### LDA (Linear Discriminant Analysis) 🎯
**LDA** is a **supervised** dimensionality reduction technique.

- Unlike PCA (which maximizes variance), LDA maximizes **class separability**.
- Finds linear combinations of features that best separate multiple classes.
- Uses both within-class and between-class scatter matrices.
- Commonly used for classification preprocessing and face recognition (Fisherfaces).

**Best when**: You have labeled data and want to maximize discrimination between classes.

#### LLE (Locally Linear Embedding) 🔗
**LLE** is a **non-linear** manifold learning method.

- Assumes data lies on a lower-dimensional manifold.
- For each point, it finds its nearest neighbors and reconstructs the point as a weighted linear combination of those neighbors.
- Then finds a low-dimensional embedding that preserves these local linear relationships.

**Strengths**: Good at unfolding manifolds (e.g., Swiss roll dataset).  
**Weaknesses**: Sensitive to noise and parameter choices.

---

### Quick Comparison

| Technique | Type       | Supervised | Best For                  | Speed     |
|-----------|------------|------------|---------------------------|-----------|
| PCA       | Linear     | No         | General reduction         | Very Fast |
| t-SNE     | Non-linear | No         | 2D/3D Visualization       | Slow      |
| UMAP      | Non-linear | Optional   | Visualization + Reduction | Fast      |
| LDA       | Linear     | Yes        | Classification            | Fast      |
| LLE       | Non-linear | No         | Manifold unfolding        | Medium    |

---

### When to Use Dimensionality Reduction? 💡
- Before training complex models on high-dimensional data
- For data visualization
- To remove noise and multicollinearity
- As a preprocessing step for distance-based algorithms (like KNN)

---

## K-Means Clustering in Machine Learning 🔀

### What is K-Means? 🤖

**K-Means** is one of the simplest and most popular **unsupervised** machine learning algorithms used for **clustering**. 

It groups similar data points together into **K clusters** (where K is a number you choose in advance) based on their feature similarity. The goal is to minimize the variance (spread) within each cluster while maximizing the separation between different clusters.

#### Common Use Cases:
- Customer segmentation (grouping customers by behavior) 👥
- Image compression (reducing color palette) 🖼️
- Document clustering (grouping similar news/articles) 📄
- Anomaly detection (points far from any cluster center)
- Market segmentation and recommendation systems

---

### How Does K-Means Work? ⚙️

K-Means is an **iterative algorithm** that follows these steps:

#### Step-by-Step Process:

1. **Choose K**: Decide the number of clusters you want (e.g., K=3).

2. **Initialize Centroids**: Randomly place K cluster centers (centroids) in the feature space.

3. **Assignment Step**:
   - For each data point, calculate its distance to all centroids.
   - Assign the point to the **nearest centroid** (usually using Euclidean distance).

4. **Update Step**:
   - For each cluster, recalculate the **centroid** as the **mean** (average) of all points assigned to that cluster.

5. **Repeat**:
   - Repeat steps 3 and 4 until one of the following happens:
     - Centroids stop moving (convergence)
     - Maximum number of iterations is reached
     - Assignments no longer change

The algorithm tries to **minimize the Within-Cluster Sum of Squares (WCSS)**, also known as **inertia**:

$$
\text{WCSS} = \sum_{i=1}^{K} \sum_{x \in C_i} \| x - \mu_i \|^2
$$

Where $\mu_i$ is the centroid of cluster $C_i$.

---

### Important Considerations ⚠️

- **Choosing the right K**: Use the **Elbow Method** (plot WCSS vs K and look for the "elbow" point) or **Silhouette Score**.
- **Sensitive to Initialization**: Bad initial centroids can lead to poor clusters. Use **K-Means++** (smart initialization) to improve results.
- **Assumptions**:
  - Clusters are roughly spherical and equally sized
  - Features should be scaled (standardization is important)
- **Hard Clustering**: Each point belongs to exactly one cluster.

---

### Advantages ✅
- Simple and easy to understand
- Very fast and scalable to large datasets
- Easy to implement and interpret

### Disadvantages ❌
- Must specify K in advance
- Sensitive to outliers (they can pull centroids)
- Assumes clusters are convex and isotropic
- Can get stuck in local optima
- Not suitable for non-spherical or varying density clusters

---

### Quick Summary 🎯

**K-Means** is a fast, intuitive clustering algorithm that partitions data into K groups by iteratively assigning points to the nearest centroid and updating centroids to the cluster mean. While simple, it remains a go-to algorithm for many real-world clustering tasks and serves as a strong baseline.

---

## Hierarchical Clustering in Machine Learning 🌳

### What is Hierarchical Clustering? 🤝

**Hierarchical Clustering** is an **unsupervised** machine learning algorithm that builds a hierarchy of clusters. Unlike K-Means, it does **not require** you to specify the number of clusters in advance. 

Instead, it creates a tree-like structure called a **dendrogram**, which shows how clusters are merged (or split) at different levels. You can then "cut" the dendrogram at a desired height to get the number of clusters you want.

#### Common Use Cases:
- Customer segmentation 👥
- Gene expression analysis in biology 🧬
- Document and text clustering 📚
- Social network analysis
- Image segmentation 🖼️

---

### How Does Hierarchical Clustering Work? 🔄

There are two main approaches:

#### 1. Agglomerative (Bottom-Up) Clustering — Most Common
- Starts with each data point as its own individual cluster.
- Repeatedly **merges** the two closest clusters until only one big cluster remains.
- This creates a hierarchy from small clusters to large ones.

#### 2. Divisive (Top-Down) Clustering
- Starts with all data points in one single cluster.
- Repeatedly **splits** the most heterogeneous cluster into smaller ones until each point is in its own cluster.

**Agglomerative** is far more popular due to its simplicity and efficiency.

---

### The Merging Process (Linkage Criteria)

The key decision in hierarchical clustering is **how to measure the distance between two clusters** (not just individual points). Common linkage methods include:

- **Single Linkage** (Minimum distance): Distance between the closest points of two clusters.  
  → Can create long, chain-like clusters.

- **Complete Linkage** (Maximum distance): Distance between the farthest points of two clusters.  
  → Creates compact, spherical clusters.

- **Average Linkage**: Average distance between all pairs of points from the two clusters.  
  → Balanced approach.

- **Ward’s Linkage** (Most Popular): Minimizes the increase in **total within-cluster variance** after merging.  
  → Often produces the best and most balanced clusters.

---

### Dendrogram Visualization 📊

The result of hierarchical clustering is a **dendrogram** — a tree diagram that shows:
- Which clusters were merged at each step
- The distance (or dissimilarity) at which merges happened

You can cut the dendrogram horizontally at any height to obtain a specific number of clusters.

---

### Advantages ✅
- No need to specify number of clusters beforehand
- Provides a complete hierarchy (great for interpretation)
- Works with any distance metric
- Can reveal nested structures in data

### Disadvantages ❌
- Computationally expensive (usually $O(n^3)$ or $O(n^2)$ time) → not ideal for very large datasets
- Once a merge is done, it cannot be undone (greedy algorithm)
- Sensitive to outliers and noise
- Requires choosing a linkage method and distance metric carefully

---

### Quick Summary 🎯

**Hierarchical Clustering** builds a tree of clusters either by merging smaller ones (agglomerative) or splitting larger ones (divisive). It gives you maximum flexibility through the dendrogram and is excellent when you want to explore the natural grouping structure of your data at multiple levels of granularity.

It pairs very well with K-Means — you can use hierarchical clustering to decide the optimal number of clusters for K-Means.

---

## DBSCAN in Machine Learning 🟢

### What is DBSCAN? 🔍

**DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) is a powerful **unsupervised** clustering algorithm that groups data points based on **density**.

Unlike K-Means or Hierarchical Clustering, DBSCAN:
- Does **not** require you to specify the number of clusters in advance
- Can discover clusters of **arbitrary shapes** (not just spherical)
- Automatically identifies and marks **outliers/noise** points

#### Common Use Cases:
- Anomaly/outlier detection 🔍
- Spatial data analysis (geographical clustering) 🗺️
- Image segmentation
- Finding patterns in noisy real-world data
- Customer behavior clustering with irregular groups

---

### How Does DBSCAN Work? ⚙️

DBSCAN works by analyzing the **local density** of points. It classifies each point into one of three categories:

#### Key Concepts:

1. **Core Point**:
   - A point that has at least **MinPts** (minimum points) neighbors within a radius **ε** (epsilon).
   - These are the "dense" centers of clusters.

2. **Border Point**:
   - A point that is within ε of a core point but has fewer than MinPts neighbors itself.
   - These lie on the edge of a cluster.

3. **Noise Point (Outlier)**:
   - A point that is neither a core point nor a border point.
   - These are ignored and not assigned to any cluster.

#### The Clustering Process:

1. Pick an unvisited point from the dataset.
2. Check if it is a **core point** (has enough neighbors within ε).
3. If yes, start a new cluster and expand it by adding all **density-reachable** points.
4. **Density-Reachable**: You can travel from one core point to another by jumping through overlapping ε-neighborhoods.
5. **Density-Connected**: Points that are mutually reachable through core points belong to the same cluster.
6. Repeat until all points are visited.

The algorithm grows clusters by connecting dense regions and marks sparse areas as noise.

---

### Parameters ⚙️

- **ε (epsilon)**: The maximum distance between two points to be considered neighbors.
- **MinPts**: The minimum number of points required to form a dense region.

**Tips for choosing parameters**:
- Use **k-distance plot** (sort distances to k-th nearest neighbor) to find a good ε
- MinPts is often set to `2 * number_of_features` or higher

---

### Advantages ✅
- Excellent at handling **noise and outliers**
- Can find clusters with **complex, non-convex shapes**
- No need to specify number of clusters
- Works well with varying density (to some extent)

### Disadvantages ❌
- Sensitive to the choice of ε and MinPts
- Struggles with clusters of **vastly different densities**
- Not very scalable to extremely large high-dimensional datasets (though faster variants exist)
- Requires careful parameter tuning

---

### Quick Comparison with Other Clustering Algorithms

| Algorithm      | Needs K? | Shape     | Handles Noise | Arbitrary Shapes |
|----------------|----------|-----------|---------------|------------------|
| K-Means        | Yes      | Spherical | Poor          | No               |
| Hierarchical   | No       | Varies    | Moderate      | Moderate         |
| DBSCAN         | No       | Any       | Excellent     | Yes              |
