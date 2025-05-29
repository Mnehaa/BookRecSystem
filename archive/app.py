# import the librareis 
import streamlit as st 
import pickle 
import numpy as np 
import pandas as pd 

st.set_page_config(layout="wide")

st.header("Book Recommender System")

st.markdown('''
            ##### The site usinging colaborative filtering suggests books from our catalog. 
            ##### We recommend top 50 books for every one as well. 
            ''')
# import our models : 

popular = pickle.load(open('popular.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb')) 

# Top 50 Books : 

st.sidebar.title("Top 50 Books")

if st.sidebar.button("SHOW"):
    cols_per_row = 5 
    num_rows = 10 
    for row in range(num_rows): 
        cols = st.columns(cols_per_row)
        for col in range(cols_per_row): 
            book_idx = row * cols_per_row + col
            if book_idx < len(popular):
                with cols[col]:
                    st.image(popular.iloc[book_idx]['Image-URL-M']) # Displays the image
                    st.text(popular.iloc[book_idx]['Book-Title']) # Displays the Book Title
                    st.text(popular.iloc[book_idx]['Book-Author']) # Display the Author name

