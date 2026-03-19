import streamlit as st
import pandas as pd

import requests

API_KEY = "5fbcc2e2"  # replace with your key

def fetch_movie_details(movie_title):
    movie_title_clean = movie_title.split("(")[0].strip()

    if ", The" in movie_title_clean:
        movie_title_clean = "The " + movie_title_clean.replace(", The", "")
    if ", A" in movie_title_clean:
        movie_title_clean = "A " + movie_title_clean.replace(", A", "")

    url = f"http://www.omdbapi.com/?t={movie_title_clean}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        return {
            "poster": data.get("Poster"),
            "rating": data.get("imdbRating"),
            "genre": data.get("Genre"),
            "year": data.get("Year"),
            "plot": data.get("Plot")
        }
    return None
    
st.sidebar.title("📌About")

st.sidebar.info("This app recommends movies using collaborative filtering. Select a movie and get personalized suggestions using user ratings.")

st.sidebar.title("⚙️ Filters")
st.sidebar.markdown("Adjust recommendation settings below:")

min_ratings = st.sidebar.slider("Minimum Ratings", 0, 500, 100)

# Load data
@st.cache_data
def load_data():
    ratings = pd.read_csv("data/u.data", sep="\t",
                          names=["user_id", "item_id", "rating", "timestamp"])
    movies = pd.read_csv("data/Movie_Id_Titles")
    
    data = pd.merge(ratings, movies, on="item_id")

    movie_ratings = data.groupby("title")["rating"].agg(["mean", "count"])
    movie_ratings.rename(columns={"mean": "avg_rating", "count": "num_ratings"}, inplace=True)

    movie_matrix = data.pivot_table(index="user_id", columns="title", values="rating")

    return movie_matrix, movie_ratings

movie_matrix, movie_ratings = load_data()

# Recommendation function
def recommend_movies(movie_name):
    if movie_name not in movie_matrix.columns:
        return []

    movie_ratings_series = movie_matrix[movie_name]
    similar_movies = movie_matrix.corrwith(movie_ratings_series)

    corr_df = pd.DataFrame(similar_movies, columns=["correlation"])
    corr_df.dropna(inplace=True)

    corr_df = corr_df.join(movie_ratings["num_ratings"])

    recommendations = corr_df[corr_df["num_ratings"] > min_ratings] \
                        .sort_values("correlation", ascending=False)

    return recommendations.drop(movie_name, errors="ignore").head(10)

# UI
st.title("🎬 Movie Recommendation System")
st.markdown("### Find movies similar to your favorite one 🍿")
st.write("---")

movie_list = movie_matrix.columns.sort_values()

selected_movie = st.selectbox("Select a Movie", movie_list)
st.write(f"### You selected: **{selected_movie}**")

if st.button("Recommend"):
    with st.spinner("Finding best movies for you..."):
        results = recommend_movies(selected_movie)

    if len(results) == 0:
        st.write("No recommendations found.")
    else:
        st.subheader("🎬 Top Recommendations:")

        cols = st.columns(5)
        
        for i, movie in enumerate(results.index):
            details = fetch_movie_details(movie)

            with cols[i % 5]:

                # Poster
                if details and details["poster"] != "N/A":
                    st.image(details["poster"], use_container_width=True)
                else:
                    st.markdown("""
                        <div style="
                            height:250px;
                            display:flex;
                            align-items:center;
                            justify-content:center;
                            background-color:#1e1e1e;
                            border-radius:10px;
                            color:#888;">
                            No Image
                        </div>
                    """, unsafe_allow_html=True)

                # Movie Info
                if details:
                    st.markdown(f"""
                    <div style="text-align:center; color:white;">
                        <b>{movie}</b><br>
                        ⭐ {details['rating']} | 🎭 {details['genre']}<br>
                        📅 {details['year']}
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown(f"""
                    <div style="font-size:12px; color:#ccc; text-align:center;">
                        {details['plot'][:100]}...
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.caption(movie)

st.write("---")

st.markdown("""
<div style="text-align:center; color:white;">

Made with ❤️ by <b>Jasreman Kaur</b>  

<a href="https://www.linkedin.com/in/jasreman-kaur-818568298" target="_blank">
    <button style="background-color:#0077b5;color:white;border:none;padding:8px 12px;border-radius:5px;margin:5px;">
        LinkedIn
    </button>
</a>

<a href="https://github.com/Jasreman003" target="_blank">
    <button style="background-color:#333;color:white;border:none;padding:8px 12px;border-radius:5px;margin:5px;">
        GitHub
    </button>
</a>

</div>
""", unsafe_allow_html=True)                    