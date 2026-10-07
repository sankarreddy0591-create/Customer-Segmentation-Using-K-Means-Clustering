
# import libraries
import pickle

import pandas as pd 


from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# load the dataset
data = pd.read_csv('Data/Mall_Customers.csv')
print(data.columns)

# check for missing values
print(data.isnull().sum())

# feature selection
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

print(X)

# train the KMeans model
kmeans_model = KMeans(
    n_clusters=5, 
    init='k-means++',
    random_state=42,
    n_init=10
)

cluster_labels = kmeans_model.fit_predict(X)

# Add the cluster labels 
data['Cluster'] = cluster_labels

# Evaluate the model using silhouette score
silhouette = silhouette_score(
    X,
    cluster_labels
)

print("K-Means model trained successfully!")
print("----------------------------------------------  ")

print("Number of clusters: ", 5)
print("Features:", X.columns.tolist())
print("Silhouette Score: ", silhouette)

# display the cluster centers
print("Cluster Centers: ", kmeans_model.cluster_centers_)


# Save the trained model
import os
import pickle

# Create the model directory if it doesn't exist
os.makedirs("../model", exist_ok=True)

with open("../model/kmeans_customer_segmentation.pkl", "wb") as f:
    pickle.dump(kmeans_model, f)

print("Model saved successfully!")

