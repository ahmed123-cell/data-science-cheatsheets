# 🔍 Unsupervised Learning

A structured guide to dimensionality reduction and clustering algorithms: methods that find structure in **unlabeled data**, with no target variable to predict.

<a id="contents"></a>
## 📚 Contents

**Part 1: Dimensionality Reduction**

1. [Dimension Reduction 📉](#dr)
   - [What is Dimensionality Reduction? 🤔](#dr-what-is-dimensionality-reduction)
   - [Principal Component Analysis (PCA) 🔄](#dr-principal-component-analysis-pca)
   - [Other Dimensionality Reduction Algorithms](#dr-other-dimensionality-reduction-algorithms)
      - [t-SNE (t-Distributed Stochastic Neighbor Embedding) 🌀](#dr-t-sne-t-distributed-stochastic-neighbor-embedding)
      - [UMAP (Uniform Manifold Approximation and Projection) 🌌](#dr-umap-uniform-manifold-approximation-and-projection)
      - [LDA (Linear Discriminant Analysis) 🎯](#dr-lda-linear-discriminant-analysis)
      - [LLE (Locally Linear Embedding) 🔗](#dr-lle-locally-linear-embedding)
   - [Quick Comparison](#dr-quick-comparison)
   - [When to Use Dimensionality Reduction? 💡](#dr-when-to-use-dimensionality-reduction)

**Part 2: Clustering**

2. [K-Means Clustering 🔀](#kmeans)
   - [What is K-Means? 🤖](#kmeans-what-is-k-means)
   - [How Does K-Means Work? ⚙️](#kmeans-how-does-k-means-work)
   - [Important Considerations ⚠️](#kmeans-important-considerations)
   - [Advantages ✅](#kmeans-advantages)
   - [Disadvantages ❌](#kmeans-disadvantages)
   - [Quick Summary 🎯](#kmeans-quick-summary)

3. [Hierarchical Clustering 🌳](#hc)
   - [What is Hierarchical Clustering? 🤝](#hc-what-is-hierarchical-clustering)
   - [How Does Hierarchical Clustering Work? 🔄](#hc-how-does-hierarchical-clustering-work)
   - [The Merging Process (Linkage Criteria)](#hc-the-merging-process-linkage-criteria)
   - [Dendrogram Visualization 📊](#hc-dendrogram-visualization)
   - [Advantages ✅](#hc-advantages)
   - [Disadvantages ❌](#hc-disadvantages)
   - [Quick Summary 🎯](#hc-quick-summary)

4. [DBSCAN 🟢](#dbscan)
   - [What is DBSCAN? 🔍](#dbscan-what-is-dbscan)
   - [How Does DBSCAN Work? ⚙️](#dbscan-how-does-dbscan-work)
   - [Parameters ⚙️](#dbscan-parameters)
   - [Advantages ✅](#dbscan-advantages)
   - [Disadvantages ❌](#dbscan-disadvantages)
   - [Quick Comparison with Other Clustering Algorithms](#dbscan-quick-comparison-with-other-clustering-algorithms)

---

## 🧭 Algorithms at a Glance

| # | Algorithm | Family | Core idea | Typical use |
|---|-----------|--------|-----------|-------------|
| 1 | [Dimension Reduction](#dr) (PCA, t-SNE, UMAP, LDA, LLE) | Dimensionality reduction | Cut the number of features while preserving as much important information as possible | Visualization, removing noise, preprocessing for other models |
| 2 | [K-Means](#kmeans) | Clustering (centroid-based) | Assign points to the nearest of K centroids, then update centroids to the cluster mean | Customer segmentation, image compression |
| 3 | [Hierarchical Clustering](#hc) | Clustering (hierarchical) | Build a tree of clusters by merging or splitting; cut the dendrogram where you want | Gene expression analysis, document clustering |
| 4 | [DBSCAN](#dbscan) | Clustering (density-based) | Grow clusters from dense regions and mark sparse points as noise | Anomaly detection, spatial data |

---

<a id="dr"></a>
## 1. Dimension Reduction 📉

<a id="dr-what-is-dimensionality-reduction"></a>
### What is Dimensionality Reduction? 🤔

**Dimensionality Reduction** refers to techniques that reduce the number of input features (dimensions) while preserving as much important information as possible. It helps with the **Curse of Dimensionality**, improves model performance, reduces computation time, and enables visualization of high-dimensional data.

---

<a id="dr-principal-component-analysis-pca"></a>
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

<a id="dr-other-dimensionality-reduction-algorithms"></a>
### Other Dimensionality Reduction Algorithms

<a id="dr-t-sne-t-distributed-stochastic-neighbor-embedding"></a>
#### t-SNE (t-Distributed Stochastic Neighbor Embedding) 🌀
**t-SNE** is a **non-linear** technique primarily used for **visualization** (reducing to 2D or 3D).

- It models similarities between points using probability distributions.
- In high dimensions: Uses Gaussian distribution.
- In low dimensions: Uses Student’s t-distribution (heavier tails to avoid crowding).
- Minimizes the difference between these two distributions (using Kullback-Leibler divergence).

**Best for**: Exploring clusters and manifolds in data.  
**Drawbacks**: Not great for new data (no explicit mapping), computationally expensive, and results can vary between runs.

<a id="dr-umap-uniform-manifold-approximation-and-projection"></a>
#### UMAP (Uniform Manifold Approximation and Projection) 🌌
**UMAP** is a modern, fast, and scalable **non-linear** technique that often produces better visualizations than t-SNE while preserving more global structure.

- Based on **manifold learning** and topological data analysis.
- Constructs a high-dimensional graph of nearest neighbors, then optimizes a low-dimensional representation.
- Faster and more scalable than t-SNE.
- Supports both supervised and unsupervised modes.

**Strengths**: Better at preserving both local and global structure, faster, and consistent.

<a id="dr-lda-linear-discriminant-analysis"></a>
#### LDA (Linear Discriminant Analysis) 🎯
**LDA** is a **supervised** dimensionality reduction technique.

- Unlike PCA (which maximizes variance), LDA maximizes **class separability**.
- Finds linear combinations of features that best separate multiple classes.
- Uses both within-class and between-class scatter matrices.
- Commonly used for classification preprocessing and face recognition (Fisherfaces).

**Best when**: You have labeled data and want to maximize discrimination between classes.

<a id="dr-lle-locally-linear-embedding"></a>
#### LLE (Locally Linear Embedding) 🔗
**LLE** is a **non-linear** manifold learning method.

- Assumes data lies on a lower-dimensional manifold.
- For each point, it finds its nearest neighbors and reconstructs the point as a weighted linear combination of those neighbors.
- Then finds a low-dimensional embedding that preserves these local linear relationships.

**Strengths**: Good at unfolding manifolds (e.g., Swiss roll dataset).  
**Weaknesses**: Sensitive to noise and parameter choices.

---

<a id="dr-quick-comparison"></a>
### Quick Comparison

| Technique | Type       | Supervised | Best For                  | Speed     |
|-----------|------------|------------|---------------------------|-----------|
| PCA       | Linear     | No         | General reduction         | Very Fast |
| t-SNE     | Non-linear | No         | 2D/3D Visualization       | Slow      |
| UMAP      | Non-linear | Optional   | Visualization + Reduction | Fast      |
| LDA       | Linear     | Yes        | Classification            | Fast      |
| LLE       | Non-linear | No         | Manifold unfolding        | Medium    |

---

<a id="dr-when-to-use-dimensionality-reduction"></a>
### When to Use Dimensionality Reduction? 💡
- Before training complex models on high-dimensional data
- For data visualization
- To remove noise and multicollinearity
- As a preprocessing step for distance-based algorithms (like KNN)

[↑ Back to contents](#contents)

---

<a id="kmeans"></a>
## 2. K-Means Clustering 🔀

<a id="kmeans-what-is-k-means"></a>
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

<a id="kmeans-how-does-k-means-work"></a>
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

<a id="kmeans-important-considerations"></a>
### Important Considerations ⚠️

- **Choosing the right K**: Use the **Elbow Method** (plot WCSS vs K and look for the "elbow" point) or **Silhouette Score**.
- **Sensitive to Initialization**: Bad initial centroids can lead to poor clusters. Use **K-Means++** (smart initialization) to improve results.
- **Assumptions**:
  - Clusters are roughly spherical and equally sized
  - Features should be scaled (standardization is important)
- **Hard Clustering**: Each point belongs to exactly one cluster.

---

<a id="kmeans-advantages"></a>
### Advantages ✅
- Simple and easy to understand
- Very fast and scalable to large datasets
- Easy to implement and interpret

<a id="kmeans-disadvantages"></a>
### Disadvantages ❌
- Must specify K in advance
- Sensitive to outliers (they can pull centroids)
- Assumes clusters are convex and isotropic
- Can get stuck in local optima
- Not suitable for non-spherical or varying density clusters

---

<a id="kmeans-quick-summary"></a>
### Quick Summary 🎯

**K-Means** is a fast, intuitive clustering algorithm that partitions data into K groups by iteratively assigning points to the nearest centroid and updating centroids to the cluster mean. While simple, it remains a go-to algorithm for many real-world clustering tasks and serves as a strong baseline.

[↑ Back to contents](#contents)

---

<a id="hc"></a>
## 3. Hierarchical Clustering 🌳

<a id="hc-what-is-hierarchical-clustering"></a>
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

<a id="hc-how-does-hierarchical-clustering-work"></a>
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

<a id="hc-the-merging-process-linkage-criteria"></a>
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

<a id="hc-dendrogram-visualization"></a>
### Dendrogram Visualization 📊

The result of hierarchical clustering is a **dendrogram** — a tree diagram that shows:
- Which clusters were merged at each step
- The distance (or dissimilarity) at which merges happened

You can cut the dendrogram horizontally at any height to obtain a specific number of clusters.

---

<a id="hc-advantages"></a>
### Advantages ✅
- No need to specify number of clusters beforehand
- Provides a complete hierarchy (great for interpretation)
- Works with any distance metric
- Can reveal nested structures in data

<a id="hc-disadvantages"></a>
### Disadvantages ❌
- Computationally expensive (usually $O(n^3)$ or $O(n^2)$ time) → not ideal for very large datasets
- Once a merge is done, it cannot be undone (greedy algorithm)
- Sensitive to outliers and noise
- Requires choosing a linkage method and distance metric carefully

---

<a id="hc-quick-summary"></a>
### Quick Summary 🎯

**Hierarchical Clustering** builds a tree of clusters either by merging smaller ones (agglomerative) or splitting larger ones (divisive). It gives you maximum flexibility through the dendrogram and is excellent when you want to explore the natural grouping structure of your data at multiple levels of granularity.

It pairs very well with K-Means — you can use hierarchical clustering to decide the optimal number of clusters for K-Means.

[↑ Back to contents](#contents)

---

<a id="dbscan"></a>
## 4. DBSCAN 🟢

<a id="dbscan-what-is-dbscan"></a>
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

<a id="dbscan-how-does-dbscan-work"></a>
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

<a id="dbscan-parameters"></a>
### Parameters ⚙️

- **ε (epsilon)**: The maximum distance between two points to be considered neighbors.
- **MinPts**: The minimum number of points required to form a dense region.

**Tips for choosing parameters**:
- Use **k-distance plot** (sort distances to k-th nearest neighbor) to find a good ε
- MinPts is often set to `2 * number_of_features` or higher

---

<a id="dbscan-advantages"></a>
### Advantages ✅
- Excellent at handling **noise and outliers**
- Can find clusters with **complex, non-convex shapes**
- No need to specify number of clusters
- Works well with varying density (to some extent)

<a id="dbscan-disadvantages"></a>
### Disadvantages ❌
- Sensitive to the choice of ε and MinPts
- Struggles with clusters of **vastly different densities**
- Not very scalable to extremely large high-dimensional datasets (though faster variants exist)
- Requires careful parameter tuning

---

<a id="dbscan-quick-comparison-with-other-clustering-algorithms"></a>
### Quick Comparison with Other Clustering Algorithms

| Algorithm      | Needs K? | Shape     | Handles Noise | Arbitrary Shapes |
|----------------|----------|-----------|---------------|------------------|
| K-Means        | Yes      | Spherical | Poor          | No               |
| Hierarchical   | No       | Varies    | Moderate      | Moderate         |
| DBSCAN         | No       | Any       | Excellent     | Yes              |

[↑ Back to contents](#contents)