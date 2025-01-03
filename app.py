import streamlit as st
import pickle
import operator
import base64
from scipy import spatial

movies = pickle.load(open('movies.pkl', 'rb'))
st.set_page_config(layout="wide")
# Define CSS styles
st.markdown("""
<style>
h1 {
    color: #F0FFFF;
}
select {
    width: 300px;
    background-color: #1c1c1c;
    color: #FFBF00;
    border: none;
    border-radius: 4px;
    padding: 10px;
}
.button {
    font-size: 20px;
    font-weight: bold;
    color: white;
    background-color: #004E64FF;
    border: none;
    border-radius: 5px;
    padding: 10px;
    margin-left: 10px;
}
.button:hover {
    cursor: pointer;
    background-color: #00203FFF;
}
.recommended-movies {
    background-color: rgba(0,0,0,0.5);
    padding: 20px;
    border-radius: 4px;
}

</style>
""", unsafe_allow_html=True)

# Define functions
def Similarity(movieId1, movieId2):
    a = movies.iloc[movieId1]
    b = movies.iloc[movieId2]

    genresA = a['genres_bin']
    genresB = b['genres_bin']

    genreDistance = spatial.distance.cosine(genresA, genresB)

    scoreA = a['cast_bin']
    scoreB = b['cast_bin']
    scoreDistance = spatial.distance.cosine(scoreA, scoreB)

    directA = a['director_bin']
    directB = b['director_bin']
    directDistance = spatial.distance.cosine(directA, directB)

    wordsA = a['words_bin']
    wordsB = b['words_bin']
    wordsDistance = spatial.distance.cosine(directA, directB)
    return genreDistance + directDistance + scoreDistance + wordsDistance

def recommend_movies(name):
    new_movie = movies[movies['original_title'].str.contains(name)].iloc[0]
    recommended_movies = []

    def getNeighbors(baseMovie, K):
        distances = []
        for index, movie in movies.iterrows():
            if movie['new_id'] != baseMovie['new_id']:
                dist = Similarity(baseMovie['new_id'], movie['new_id'])
                distances.append((movie['new_id'], dist))

        distances.sort(key=operator.itemgetter(1))
        neighbors = []

        for x in range(K):
            neighbors.append(distances[x])
        return neighbors

    K = 10
    avgRating = 0
    neighbors = getNeighbors(new_movie, K)

    for neighbor in neighbors:
        recommended_movies.append(movies.loc[movies['new_id'] == neighbor[0], 'original_title'].iloc[0])

    return recommended_movies

# Streamlit app
st.title('Movie Recommendation System')
st.markdown("<h2 style='color: #F0FFFF;'>Find movies similar to your favorite</h2>", unsafe_allow_html=True)
search_name = st.selectbox(
    'Enter the movie name:',
    movies['original_title'].values)
if st.button('Recommend'):
    recommended_movies = recommend_movies(search_name)
    if recommended_movies:
        st.write('Recommended Movies:',
                recommended_movies)
    else:
        st.write('Searched movie is not found')

# Add a background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string});
            background-size: cover;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_local('2471303.gif')