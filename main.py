import streamlit as st
import pandas as pd


st.set_page_config(page_title="Abbas' App2", page_icon=":penguin:",
                    layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Muhammad Abbas Bukhari")
    st.write("hey I am a student who is try to learn python to create awesome apps and make a lt of money of these apps")

df = pd. read_csv("data.csv", sep=";")

col3 , empty_col, col4 = st.columns([2,0.5,2])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")



        


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

