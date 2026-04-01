import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Load files
# -----------------------------
df = pickle.load(open("df.pkl", "rb"))
indices = pickle.load(open("indices.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))
tfidf_matrix = pickle.load(open("tfidf_matrix.pkl", "rb"))

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(movie_title):

    idx = indices[movie_title]

    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()

    sim_scores = list(enumerate(sim_scores))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:11]

    movie_indices = [i[0] for i in sim_scores]

    return df['title'].iloc[movie_indices]


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

# -----------------------------
# Header
# -----------------------------
st.title("🎬 Movie Recommendation System")
st.write("Type a movie name and get similar movie recommendations")

# -----------------------------
# Movie Input with Suggestions
# -----------------------------
movie_list = df['title'].values

movie_name = st.selectbox(
    "Search or Select Movie",
    movie_list
)

# -----------------------------
# Recommend Button
# -----------------------------
if st.button("Recommend Movies"):

    recommendations = recommend(movie_name)

    st.subheader("Recommended Movies 🎥")

    for i, movie in enumerate(recommendations):
        st.write(f"{i+1}. {movie}")