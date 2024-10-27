import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
import plotly.express as px
import dtale
import streamlit as st

# Load the dataset
CJA = pd.read_csv('Cleaned.csv')  # Ensure this file exists in your directory

# Title of the app
st.title("Unveiling the Job Market: Insights for Job Seekers in Saudi Arabia")

# Add an image
st.image('a1.jpg', caption='', use_column_width=True)

# Set Streamlit theme using markdown
st.markdown(
    """
    <style>
    .reportview-container {
        background: #fdf1d7;  /* Background color */
        text-align: right;  /* Align text to the right for Arabic */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Introduction
st.markdown(""" 
In recent years, the job market in Saudi Arabia has witnessed significant changes, particularly affecting job seekers. This analysis draws on data from various job postings to shed light on the challenges and opportunities that characterize the current employment landscape for individuals seeking work.
""")

# Data Overview
st.subheader("Overview of Job Search Data")
st.dataframe(CJA)

# 1. Proportion of Job Postings by Region
if 'region' in CJA.columns:
    st.subheader("Job Opportunities by Region")
    region_counts = CJA['region'].value_counts()
    fig_region = px.pie(region_counts, names=region_counts.index, values=region_counts.values,
                         title="Proportion of Job Postings by Region in Saudi Arabia",
                         color_discrete_sequence=["#a0c8ff", "#4ba3ff", "#1E90FF"])  # Light blue colors
    st.plotly_chart(fig_region)
else:
    st.error("The 'region' column is not present in the dataset.")

# 2. Expected Salary Range
if 'Salary' in CJA.columns:
    st.subheader("Salary Expectations for Job Seekers")
    fig_salary = px.histogram(CJA, x='Salary', title='Salary Distribution for Job Seekers',
                               range_x=[1000, 40000], nbins=20,
                               color_discrete_sequence=["#a0c8ff"])  # Light blue color
    st.plotly_chart(fig_salary)
else:
    st.error("The 'Salary' column is not present in the dataset.")

# 3. Opportunities by Experience Level
if 'exper' in CJA.columns:
    st.subheader("Opportunities by Experience Level")
    experience_counts = CJA['exper'].value_counts().sort_index()
    fig_experience = px.bar(
        x=experience_counts.index, 
        y=experience_counts.values,
        labels={'x': 'Experience Level', 'y': 'Number of Job Postings'},
        title='Job Opportunities by Experience Level',
        color_discrete_sequence=["#a0c8ff", "#4ba3ff"]  # Light blue colors
    )
    st.plotly_chart(fig_experience)
else:
    st.error("The 'exper' column is not present in the dataset.")

# 4. Company Types Hiring
if 'comp_type' in CJA.columns:
    st.subheader("Types of Companies Hiring")
    company_counts = CJA['comp_type'].value_counts()
    fig_company = px.bar(
        x=company_counts.index,
        y=company_counts.values,
        labels={'x': 'Company Type', 'y': 'Number of Job Postings'},
        title='Distribution of Job Postings by Company Type',
        color_discrete_sequence=["#a0c8ff"]
    )
    st.plotly_chart(fig_company)
else:
    st.error("The 'comp_type' column is not present in the dataset.")

# Add an image
st.image('a2.jpg', caption='', use_column_width=True)


# Conclusion
st.markdown("""
### Conclusion
This comprehensive analysis highlights the various dynamics influencing the job market for individuals seeking employment in Saudi Arabia. 
The findings reveal critical insights regarding regional job availability, expected salaries, and the types of companies that are hiring. 
By examining these factors, stakeholders can better understand the pathways available to job seekers and work towards fostering a more inclusive job market.
""")
