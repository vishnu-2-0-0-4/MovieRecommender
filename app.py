import streamlit as st
import pickle
import gzip

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))

# Load compressed similarity matrix
with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended = [movies.iloc[i[0]].title for i in movie_list]
    return recommended

# Streamlit UI
st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.write("Top 5 recommendations:")
    for rec in recommendations:
        st.write("🎬", rec)
