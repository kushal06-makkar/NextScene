import streamlit as st
import pickle
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Create a session with retry logic
session = requests.Session()
retries = Retry(
    total=5,              # retry up to 5 times
    backoff_factor=1,     # wait 1s, 2s, 4s... between retries
    status_forcelist=[500, 502, 503, 504]
)
session.mount("https://", HTTPAdapter(max_retries=retries))

API_KEY = "10f0f26a48a7cd9e1ee49e3ab582384c"

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        headers = {"User-Agent": "Mozilla/5.0"}  # spoof browser
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        return None
    except Exception as e:
        st.error(f"Error fetching poster for movie {movie_id}: {e}")
        return None

def recommend(movie):
    movie_ind = movies[movies['title'] == movie].index[0]
    dist = similarity[movie_ind]
    movies_list = sorted(
        list(enumerate(dist)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recomm_movies = []
    movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recomm_movies.append(movies.iloc[i[0]].title)
        movie_posters.append(fetch_poster(movie_id))
    return recomm_movies, movie_posters


# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('🎬 NextScene – suggesting the next best watch.')

selected_movie = st.selectbox('Select Movie', movies['title'].values)

if st.button('Recommend Movie'):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(names[i])
            if posters[i]:
                st.image(posters[i])
            else:
                st.warning("Poster not available")
