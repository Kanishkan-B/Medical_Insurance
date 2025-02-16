import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Medical Insurance Data Analysis")

# Load Data
@st.cache_data
def load_data():
    try:
        return pd.read_csv("Medical_insurance.csv")
    except FileNotFoundError:
        st.error("Error: Medical_insurance.csv file not found.")
        return None

data = load_data()

if data is not None:
    # Show Data
    st.subheader("First Five Rows of the Dataset")
    st.write(data.head())

    # Basic Statistics
    st.subheader("Dataset Summary")
    st.write(data.describe())

    # Data Visualization
    st.subheader("Age Distribution")
    fig, ax = plt.subplots()
    sns.histplot(data['age'], bins=20, kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("Charges Distribution")
    fig, ax = plt.subplots()
    sns.histplot(data['charges'], bins=20, kde=True, ax=ax)
    st.pyplot(fig)
else:
    st.warning("No data available to display.")
