import streamlit as st
import pickle
import gzip

# Load movies
movies = pickle.load(open('movies.pkl', 'rb'))

# Load compressed similarity matrix
with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

# Movie recommendation function
def recommend(movie):
    if movie not in movies['original_title'].values:
        st.error(f"'{movie}' not found in movie list.")
        return []

    index = movies[movies['original_title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended = [movies.iloc[i[0]]['original_title'] for i in movie_list]
    return recommended

# Streamlit App UI
st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox(
    'Select a movie to get recommendations:',
    movies['original_title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    if recommendations:
        st.write("Top 5 recommended movies:")
        for rec in recommendations:
            st.write("🎥", rec)
