
# Customer Service App.py

# import necessary libraries
import streamlit as st
import pickle
import os
import numpy as np



# page configuration
st.set_page_config(
    page_title="Customer Segmentation App",

)

# title
st.title("Customer Segmentation using K-Means Clustering")
st.write("Predict the customer segment based on Annual Income and Spending Score.")


# load the dataset

model_path=os.path.join(
    os.path.dirname(__file__),
    "model",
    "kmeans_customer_segmentation.pkl"

)

# load the trained KMeans model
with open(model_path, "rb") as f:
    kmeans_model = pickle.load(f)

# user inputs
st.subheader("Enter Customer Details:")

annual_income = st.number_input(
    "Annual Income (k$)",
    min_value=0.0,
    max_value=200.0, 
    value=50.0,
    step=1.0
)

spending_score = st.number_input(
    "Spending Score (1-100)",
    min_value=1.0,
    max_value=100.0,
    value=50.0,
    step=1.0
)

# prediction button
if st.button("Predict Customer Segment"):

    # create input data
    customer_input = np.array([
        [annual_income, spending_score]
    ])
      
    # predict the cluster
    cluster=kmeans_model.predict(customer_input)[0]


# # Cluster interpretation
# cluster_names = {
#     0: "Premium Customers",
#     1: "Careful Customers",
#     2: "Impulse Customers",
#     3: "Low Customers",
#     4: "Average Customers"
# }

# customer_type = cluster_names.get(cluster, "Cluster segment")

# display the result   
st.success(f"Customer belongs to Cluster {cluster + 1}")

st.write("### Customer Details:")

st.write(f"Annual Income (k$): {annual_income} k$")
st.write(f"Spending Score: {spending_score}")