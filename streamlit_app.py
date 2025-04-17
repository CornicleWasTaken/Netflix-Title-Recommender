import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("netflix_titles.csv")
df = df[['title', 'director', 'cast', 'listed_in', 'description']]
df = df.dropna()
df['combined'] = df.apply(lambda row: f"{row['director']} {row['cast']} {row['listed_in']} {row['description']}", axis=1)
df = df.reset_index()

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend(title):
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()
    idx = indices.get(title)
    if idx is None:
        return ["Movie not found. Try another."]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

st.title("Movie Recommendations")
user_input = st.text_input("Enter a movie title:")

if user_input:
    results = recommend(user_input)
    st.subheader("Recommended Movies:")
    for movie in results:
        st.write(f"- {movie}")
