import streamlit as st
import pandas as pd 
import numpy as np


st.write("Hello World")

df= pd.read_csv("Salary_Data.csv")

st.dataframe(df)
