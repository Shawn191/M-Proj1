import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Visualisations')

csv_file= 'global-plastics-production.csv'
df= pd.read_csv(csv_file)
st.dataframe(df)
st.header('Plastic Pollution Data Visualisations')
st.subheader('Global Plastic Production')
fig = px.line(df, x="Year", y="Global plastics production (million tonnes)", title='Global Plastic Production per Year',height=500,width=700)
fig.show()
