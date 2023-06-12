import streamlit as st
import pandas as pd 
import numpy as np


st.write("Hello World")

df= pd.DataFrame({"Name": "Maria", "Age": 15, "School": "Rosenberg"})
st.dataframe(df)
