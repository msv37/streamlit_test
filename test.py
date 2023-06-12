import streamlit as st
import pandas as pd 
import numpy as np


st.title("Salaries Dataframe")


df= pd.read_csv("Salary_Data.csv")

st.dataframe(df)

