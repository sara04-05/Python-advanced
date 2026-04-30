import streamlit as st
import pandas as pd
import plotly.express as px


books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("Bestselling Book Analysis")
st.write("This app analyzes the Amazon Top Selling books from 2009 to 2022")


st.subheader("Summary Statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1, col2, col3, col4  = st.columns(4)
col1.metric("")