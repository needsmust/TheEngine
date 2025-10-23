#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import random

# Load the Excel file once
@st.cache_data
def load_data():
    df = pd.read_excel(
        "wordFrequency.xlsx",
        sheet_name="3 wordForms",
        usecols=["word", "wordFreq"]
    )
    df["Probability"] = df["wordFreq"] / df["wordFreq"].sum()
    return df

df = load_data()

st.title("The Engine")

num_words_to_print = st.slider("Number of words to generate:", min_value=5, max_value=100, value=10, step=5)

def generate_words(n):
    sampled_words = random.choices(
        population=df["word"],
        weights=df["Probability"],
        k=n
    )
    # Group words in rows of 5
    rows = [sampled_words[i:i+5] for i in range(0, len(sampled_words), 5)]
    return rows


if st.button("Generate new words"):
    word_rows = generate_words(num_words_to_print)
    for row in word_rows:
        cols = st.columns(len(row))
        for col, word in zip(cols, row):
            col.write(f"**{word}**")  # Bold for visibility
