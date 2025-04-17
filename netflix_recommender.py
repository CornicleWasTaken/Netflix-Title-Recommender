import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("netflix_titles.csv")

df = df[['title', 'director', 'cast', 'listed_in', 'description']]

df = df.dropna()
def combine_features(row):
    return f"{row['director']} {row['cast']} {row['listed_in']} {row['description']}"

df['combined'] = df.apply(combine_features, axis=1)
vectorizer = TfidfVectorizer(stop_words='english')

tfidf_matrix = vectorizer.fit_transform(df['combined'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
df = df.reset_index()
def recommend(title, cosine_sim=cosine_sim):
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()

    idx = indices.get(title)

    if idx is None:
        return ["Movie not found. Please try another title."]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]

    movie_indices = [i[0] for i in sim_scores]

    return df['title'].iloc[movie_indices].tolist()


if __name__ == "__main__":
    movie = input("Enter a Netflix movie title: ")
    print("\nTop 5 recommendations:")
    for rec in recommend(movie):
        print(f"- {rec}")