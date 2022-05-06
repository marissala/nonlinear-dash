import streamlit as st
import pandas as pd

df = pd.read_csv("podcasts-2015-05-01_to_2022-05-05.csv")

st.write("Hello")
st.line_chart(df.followers)

st.write(df.tail())

