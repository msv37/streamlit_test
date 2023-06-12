import streamlit as st
import pandas as pd 
import numpy as np


st.title("Salaries Dataframe")


df= pd.read_csv("Salary_Data.csv")

st.dataframe(df)

df_max = df.groupby(['Job Title','Years of Experience'])['Salary'].max()
st.dataframe(df_max)

st.write("Salaries in order from greatest to lowest")

df_max2 = df.groupby(['Job Title'])['Salary'].max()
df_max2 = df.sort_values(by=['Salary'], ascending=False)
st.dataframe(df_max2)
