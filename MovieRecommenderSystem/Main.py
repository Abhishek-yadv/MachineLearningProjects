import pickle
import streamlit as st
import requests
import pandas as pd

# Function to fetch movie poster
def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=b7a7ac232a433bf2920625242069004d")
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = [
        (movies.iloc[i[0]].title, fetch_poster(movies.iloc[i[0]].movie_id))
        for i in distances[1:6]
    ]
    return recommended_movies

# Set page config
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stSelectbox > div > div {
        background-color: #262730;
    }
    .stButton > button {
        background-color: #ff4b4b;
        color: white;
    }
    .movie-title {
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 0.5em;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🎬 Movie Recommender System")

# Load data
@st.cache_data
def load_data():
    movies = pd.DataFrame(pickle.load(open('movie_dict.pkl', 'rb')))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

movies, similarity = load_data()

# Movie selection
st.subheader("Select a movie you like")
selected_movie = st.selectbox("Type or select a movie from the dropdown", movies['title'].values)

# Show recommendation button
if st.button('🔍 Get Recommendations', key='recommend_button'):
    with st.spinner('Finding great movies for you...'):
        recommended_movies = recommend(selected_movie)
    
    st.subheader("You might also like these movies:")
    cols = st.columns(5)
    for i, (title, poster) in enumerate(recommended_movies):
        with cols[i]:
            st.image(poster, use_column_width=True)
            st.markdown(f"<p class='movie-title'>{title}</p>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Abhishek Yadav")