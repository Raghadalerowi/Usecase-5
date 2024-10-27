import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
import plotly.express as px
import sweetviz as sv
import ydata
import dtale
import streamlit as st

# Load the dataset
CJA = pd.read_csv('Cleaned.csv')  # Make sure the file is in the same directory or provide the full path

# Title of the app
st.title("Job Search Data Analysis")

# Display the data overview
st.subheader("Data Overview")
st.dataframe(CJA)

# Example visualization: Salary distribution (assuming 'Salary' is a column in the dataset)
if 'Salary' in CJA.columns:  # Ensure 'Salary' column exists
    if st.checkbox('Show Salary Histogram'):
        st.subheader('Salary Distribution')
        st.bar_chart(CJA['Salary'])
else:
    st.error("The 'Salary' column is not present in the dataset.")

# Example visualization: Company types
if 'comp_type' in CJA.columns:  # Ensure 'comp_type' column exists
    if st.checkbox('Show Company Type Distribution'):
        st.subheader('Company Type Distribution')
        company_counts = CJA['comp_type'].value_counts()
        st.bar_chart(company_counts)
else:
    st.error("The 'comp_type' column is not present in the dataset.")

# Example visualization: Gender distribution
if 'gender' in CJA.columns:  # Ensure 'gender' column exists
    if st.checkbox('Show Gender Distribution'):
        st.subheader('Gender Distribution')
        gender_counts = CJA['gender'].value_counts()
        st.bar_chart(gender_counts)
else:
    st.error("The 'gender' column is not present in the dataset.")
