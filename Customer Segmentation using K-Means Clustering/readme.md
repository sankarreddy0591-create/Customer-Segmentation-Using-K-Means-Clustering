

# 👥 Customer Segmentation Using K-Means Clustering

## 1. Project Overview

Customer segmentation is the process of dividing customers into groups based on similar characteristics and behaviors.

This project uses **K-Means Clustering**, an unsupervised machine learning algorithm, to segment customers based on:

* Annual Income
* Spending Score

The goal is to identify different customer groups that can help businesses understand customer behavior and support better marketing and business decisions.

---

## 🎯 2. Project Objective

The main objectives of this project are:

* Analyze customer information.
* Explore customer income and spending behavior.
* Identify suitable customer groups using K-Means Clustering.
* Determine the optimal number of clusters using the Elbow Method.
* Visualize customer segments and cluster centroids.
* Evaluate the clustering quality using Silhouette Score.
* Save the trained K-Means model for future predictions.
* Build a Streamlit application for customer segmentation.

---

## 📊 3. Dataset

### Dataset Name

**Mall Customers Dataset**

### Dataset File

`Mall_Customers.csv`

### Main Columns

| Column                 | Description                           |
| ---------------------- | ------------------------------------- |
| CustomerID             | Unique customer identifier            |
| Gender                 | Customer gender                       |
| Age                    | Customer age                          |
| Annual Income (k$)     | Annual income in thousands of dollars |
| Spending Score (1-100) | Customer spending score               |

### Features Used for Clustering

The main clustering analysis uses:

* **Annual Income (k$)**
* **Spending Score (1-100)**

Age is also explored as an optional additional feature for extended clustering analysis.

---

## 🧠 4. Machine Learning Approach

### Algorithm

**K-Means Clustering**

K-Means is an unsupervised machine learning algorithm that groups data points into a predefined number of clusters.

In this project:

* Number of clusters: **5**
* Initialization: **K-Means++**
* Random state: **42**
* Number of initializations: **10**

---

# 🔄 5. Project Workflow

The project follows an end-to-end Data Science workflow:

```text
Dataset
   ↓
Data Loading
   ↓
Data Understanding
   ↓
Data Quality Checking
   ↓
Feature Selection
   ↓
Exploratory Data Analysis
   ↓
Determine Optimal Number of Clusters
   ↓
Elbow Method
   ↓
K-Means Model Training
   ↓
Cluster Assignment
   ↓
Cluster Visualization
   ↓
Cluster Interpretation
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
Streamlit Application
   ↓
Customer Segment Prediction
```

---

# 6. Step-by-Step Workflow

## Step 1: Data Loading

The Mall Customers dataset is loaded into a Pandas DataFrame.

The dataset is then inspected to understand its structure and available information.

---

## Step 2: Data Understanding

The following checks are performed:

* First few records
* Last few records
* Number of rows and columns
* Dataset information
* Statistical summary
* Column names
* Data types

This helps understand the dataset before applying machine learning.

---

## Step 3: Data Quality Checking

The dataset is checked for:

* Missing values
* Data quality issues
* Duplicate records
* Invalid or unexpected values

The selected clustering features are checked before model training.

---

## Step 4: Feature Selection

Two important customer behavior features are selected:

**Annual Income (k$)**

and

**Spending Score (1-100)**

These features are used because they provide useful information about customer purchasing behavior.

---

## Step 5: Exploratory Data Analysis

Customer distribution is visualized using a scatter plot.

The visualization helps understand the relationship between:

* Annual Income
* Spending Score

This provides an initial view of possible customer groups.

---

# 7. Finding the Optimal Number of Clusters

## Elbow Method

The **Within-Cluster Sum of Squares (WCSS)** is calculated for different numbers of clusters.

The project evaluates cluster values from:

**1 to 10**

The WCSS value generally decreases as the number of clusters increases.

The **Elbow Method** is used to identify the point where adding more clusters provides relatively less improvement.

### Selected Number of Clusters

**5 clusters**

---

# 8. K-Means Model Training

After selecting the optimal number of clusters, the K-Means model is trained using:

* Annual Income
* Spending Score

Each customer is assigned to one of the five clusters.

The cluster label is then added to the dataset.

---

# 9. Customer Segmentation

The five customer groups are interpreted based on their income and spending behavior.

| Customer Group      | Income | Spending | Interpretation                              |
| ------------------- | ------ | -------- | ------------------------------------------- |
| Premium Customers   | High   | High     | Customers with high purchasing activity     |
| Careful Customers   | High   | Low      | High-income customers with lower spending   |
| Impulsive Customers | Low    | High     | Lower-income customers with high spending   |
| Low Value Customers | Low    | Low      | Customers with lower income and spending    |
| Average Customers   | Medium | Medium   | Customers with moderate income and spending |

> Note: K-Means cluster numbers are assigned automatically by the algorithm. The business names above are interpretations based on the cluster characteristics, not fixed cluster numbers.

---

# 10. Cluster Visualization

The customer clusters are visualized using a scatter plot.

The visualization displays:

* Individual customers
* Different customer clusters
* Cluster centroids

This makes the customer segments easier to understand.

---

# 11. Optional Age-Based Clustering

An additional clustering analysis is performed using:

* Age
* Annual Income
* Spending Score

The selected features are standardized before applying K-Means.

This provides an extended view of customer segmentation by including customer age.

This analysis is treated as an optional extension of the main two-feature clustering model.

---

# 📈 12. Model Evaluation

Since K-Means is an **unsupervised learning algorithm**, traditional classification accuracy is not appropriate.

Instead, the project uses the:

## Silhouette Score

The Silhouette Score measures how well each customer fits within its assigned cluster compared with other clusters.

The score generally ranges from:

**-1 to +1**

| Score       | Interpretation                |
| ----------- | ----------------------------- |
| Close to +1 | Well-separated clusters       |
| Around 0    | Overlapping clusters          |
| Below 0     | Possible incorrect clustering |

A higher Silhouette Score generally indicates better-separated and more meaningful clusters.

---

# 💾 13. Model Saving

After training and evaluation, the trained K-Means model is saved as a Pickle file.

### Saved Model

`kmeans_customer_segmentation.pkl`

The selected feature names are also saved for future use.

### Model Files

```text
model/
├── kmeans_customer_segmentation.pkl
└── cluster_features.pkl
```

---

# 🌐 14. Streamlit Application

A Streamlit application is created to make the project interactive.

The application allows a user to enter:

* Annual Income
* Spending Score

The saved K-Means model then predicts the customer's cluster.

### Application Workflow

```text
User Input
    ↓
Annual Income
    +
Spending Score
    ↓
Saved K-Means Model
    ↓
Cluster Prediction
    ↓
Customer Segment
```

---

# 15. Project Structure

```text
Customer Segmentation using K-Means Clustering/
│
├── Data/
│   └── Mall_Customers.csv
│
├── model/
│   ├── kmeans_customer_segmentation.pkl
│   └── cluster_features.pkl
│
├── notebook/
│   ├── Customer Segmentation Using K-Mean Clusering with python.ipyng
├── model/
│     ├──Images 
│           ├── Customer Segmentation Using K_Means.png
│           ├── Customers Distribution.png
│           ├── The Elbow Point Graph.png
├── app.py
├── README.md
├── requirements.txt
├── train_model.py
```

---

# 16. Technologies Used

### Programming Language

* Python

### Libraries

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Pickle

### Machine Learning

* K-Means Clustering
* Elbow Method
* Silhouette Score
* StandardScaler for optional extended analysis

### Application

* Streamlit

### Development Tools

* Jupyter Notebook
* VS Code

---

# 17. Business Applications

Customer segmentation can be useful for:

* Targeted marketing
* Customer profiling
* Personalized promotions
* Customer retention
* Campaign planning
* Product recommendations
* Identifying high-value customers
* Improving customer engagement

---

# 18. Key Learnings

Through this project, the following concepts were practiced:

* Data loading and exploration
* Data quality checking
* Feature selection
* Exploratory Data Analysis
* Unsupervised Machine Learning
* K-Means Clustering
* Elbow Method
* WCSS
* Cluster interpretation
* Cluster visualization
* Silhouette Score
* Model serialization using Pickle
* Streamlit application development

---

# 19. Conclusion

This project demonstrates an end-to-end **Customer Segmentation system using K-Means Clustering**.

Customers are grouped based on their annual income and spending behavior. The Elbow Method is used to determine five clusters, while the Silhouette Score is used to evaluate the quality of the clustering.

The trained model is saved and integrated into a Streamlit application, allowing users to enter customer information and obtain a customer segment prediction.

The project demonstrates how unsupervised machine learning can transform customer data into meaningful business insights.

---

# 🚀 20. Future Improvements

Possible future improvements include:

* Add Age to the main segmentation model.
* Compare different clustering algorithms.
* Perform hyperparameter experimentation.
* Add interactive cluster visualizations.
* Add customer segment recommendations.
* Add a Power BI dashboard.
* Deploy the Streamlit application online.
* Use a larger real-world customer dataset.

---


