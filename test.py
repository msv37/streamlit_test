import streamlit as st
import pandas as pd 
import numpy as np


st.title("Salaries Dataframe")


df= pd.read_csv("Salary_Data.csv")

st.dataframe(df)

df_max = df.groupby(['Job Title','Years of Experience'])['Salary'].max()
st.dataframe(df_max)
