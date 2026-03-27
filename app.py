import streamlit as st

st.set_page_config(
    page_title="CineMatch Chatbot",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
}
.main-title {
    text-align: center;
    font-size: 3.2rem;
    font-weight: 800;
    color: #ffcc00;
    margin-bottom: 0.2rem;
}
.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #f2f2f2;
    margin-bottom: 1.5rem;
}
.block-box {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.35);
}
.movie-card {
    background: rgba(255,255,255,0.10);
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 12px;
    border-left: 5px solid #ffcc00;
}
.footer {
    text-align: center;
    color: #dddddd;
    margin-top: 30px;
    font-size: 15px;
}
.small-note {
    color: #dddddd;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

movie_data = {
    "Action": {
        "Recent": [
            {"title": "John Wick: Chapter 4", "year": "2023", "poster": "https://m.media-amazon.com/images/M/MV5BMjMxNGY4YjctZmM4NC00YmExLWE1NjAtNGQwZmQxYjY0Y2Y4XkEyXkFqcGc@._V1_.jpg"},
            {"title": "Extraction 2", "year": "2023", "poster": "https://m.media-amazon.com/images/M/MV5BYmM4NGM5MGYtYjNjMC00M2M0LTg0ZDUtN2Q3MDY3YzQ0YmY0XkEyXkFqcGc@._V1_.jpg"},
            {"title": "Mission: Impossible – Dead Reckoning", "year": "2023", "poster": "https://m.media-amazon.com/images/M/MV5BZDc5NjJlMDgtOTZjNy00NTljLTgxNzgtNmNlODQwZmRiYjZiXkEyXkFqcGc@._V1_.jpg"},
            {"title": "The Beekeeper", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BNzM3YzRjNWUtN2E2ZC00NTRjLThiZDQtYTI2MWE3MjhjNGQzXkEyXkFqcGc@._V1_.jpg"}
        ],
        "Classic": [
            {"title": "The Dark Knight", "year": "2008", "poster": "https://m.media-amazon.com/images/I/81AJdOIEIhL.jpg"},
            {"title": "Gladiator", "year": "2000", "poster": "https://m.media-amazon.com/images/M/MV5BNjQwMTM2NTctYTAwZS00YzY0LThmNjItODI1NTg0MjVjZThhXkEyXkFqcGc@._V1_.jpg"},
            {"title": "Die Hard", "year": "1988", "poster": "https://m.media-amazon.com/images/M/MV5BZjhkOGYxYjItM2EwMy00MjM0LTkxNDUtZDVlZjdkOTY3YjQ2XkEyXkFqcGc@._V1_.jpg"},
            {"title": "Mad Max: Fury Road", "year": "2015", "poster": "https://m.media-amazon.com/images/M/MV5BNjk1OTg3ZjUtNmVmYi00N2Q0LTg3YjMtMzg4ZmI2YmRhZDQzXkEyXkFqcGc@._V1_.jpg"}
        ],
        "Trending": [
            {"title": "Monkey Man", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BODZiYzg2NzgtZGQ2MS00NDljLWI4ODItM2U3YzY2OWVkMmY1XkEyXkFqcGc@._V1_.jpg"},
            {"title": "Road House", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BNjM0OWFlODctYWE0Zi00MjU4LTgzOWEtNWI2NTk0NzJjODc2XkEyXkFqcGc@._V1_.jpg"}
        ]
    },
    "Comedy": {
        "Recent": [
            {"title": "Anyone But You", "year": "2023", "poster": "https://m.media-amazon.com/images/M/MV5BN2M0ODMwNzMtZDU2Zi00NWY4LTg5NmYtYzM2NDYxNWNhMTczXkEyXkFqcGc@._V1_.jpg"},
            {"title": "No Hard Feelings", "year": "2023", "poster": "https://m.media-amazon.com/images/M/MV5BYzg3YjVhODctMzYzOC00N2Y0LTk0Y2UtZjY5NmQ0MjNhMjQ3XkEyXkFqcGc@._V1_.jpg"},
            {"title": "Barbie", "year": "2023", "poster": "https://m.media-amazon.com/images/M/MV5BYjA3N2I0ZmYtZjI0Mi00MGMwLWE0NTQtOTQ0YzgxNDA1ZjkzXkEyXkFqcGc@._V1_.jpg"},
            {"title": "The Fall Guy", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BZjNlODRjYTYtNjk4NS00ZDAzLWFmNGMtOWM2Yzk2MmRkM2U5XkEyXkFqcGc@._V1_.jpg"}
        ],
        "Classic": [
            {"title": "The Mask", "year": "1994", "poster": "https://m.media-amazon.com/images/M/MV5BNzY0ZTE3MjktZjI4OC00YzBiLWE0ZjYtMjk0YjBlOWFjM2Q0XkEyXkFqcGc@._V1_.jpg"},
            {"title": "Superbad", "year": "2007", "poster": "https://m.media-amazon.com/images/M/MV5BMjI2NTBiOTktMThiMS00N2QxLThmZWItM2Y0YzNmOTY1M2U2XkEyXkFqcGc@._V1_.jpg"},
            {"title": "3 Idiots", "year": "2009", "poster": "https://m.media-amazon.com/images/M/MV5BNTk3Y2M5MGEtZWQxZC00NDI1LTg0YzEtMDhkN2EzNzkzNGM4XkEyXkFqcGc@._V1_.jpg"},
            {"title": "Home Alone", "year": "1990", "poster": "https://m.media-amazon.com/images/M/MV5BMzM2NjVhNmYtNzQ3Mi00YjAyLTg0ZjEtZjVlM2QzNzc0YWQ0XkEyXkFqcGc@._V1_.jpg"}
        ],
        "Trending": [
            {"title": "Hit Man", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BOGJiMGEyNzktY2ExNi00OWQ3LTkzYmMtOGMxYTM2Y2IwNWIxXkEyXkFqcGc@._V1_.jpg"},
            {"title": "Mean Girls", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BY2VjNjE3OGMtNGJmNi00YmQ0LWI2ZGYtNWY5YTRmOWVjOWVkXkEyXkFqcGc@._V1_.jpg"}
        ]
    },
    "Romance": {
        "Recent": [
            {"title": "Past Lives", "year": "2023", "poster": "https://m.media-amazon.com/images/M/MV5BZjQ5M2FmODEtNGVkZS00OGM5LWJmMGUtODI5YjQ3M2E0MjE4XkEyXkFqcGc@._V1_.jpg"},
            {"title": "Anyone But You", "year": "2023", "poster": "https://m.media-amazon.com/images/M/MV5BN2M0ODMwNzMtZDU2Zi00NWY4LTg5NmYtYzM2NDYxNWNhMTczXkEyXkFqcGc@._V1_.jpg"},
            {"title": "The Idea of You", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BMDQ1YTI1NzQtYzlkNi00YWY0LTg4ZTktZjQ2ZjQ4MzQ4Yjg5XkEyXkFqcGc@._V1_.jpg"},
            {"title": "Love Again", "year": "2023", "poster": "https://m.media-amazon.com/images/M/MV5BNzhkMzFlZDMtNzlkYy00NDA3LWI4NjQtMTE0ODZkNzkwZGIwXkEyXkFqcGc@._V1_.jpg"}
        ],
        "Classic": [
            {"title": "Titanic", "year": "1997", "poster": "https://m.media-amazon.com/images/I/71lV2Ndrx7L.jpg"},
            {"title": "The Notebook", "year": "2004", "poster": "https://m.media-amazon.com/images/M/MV5BMTU0NzYzMjEtNDAwMC00NjljLTlkMjEtN2MyMjQwM2FjZjM0XkEyXkFqcGc@._V1_.jpg"},
            {"title": "La La Land", "year": "2016", "poster": "https://m.media-amazon.com/images/M/MV5BMzA4NDg0MzEtMDRkYy00MWQ0LWE2MmEtMzYzZGM0MWQ2ZWM0XkEyXkFqcGc@._V1_.jpg"},
            {"title": "Pride & Prejudice", "year": "2005", "poster": "https://m.media-amazon.com/images/M/MV5BNTM0ODgwNzg3MV5BMl5BanBnXkFtZTcwNzkzMzIzMw@@._V1_.jpg"}
        ],
        "Trending": [
            {"title": "Challengers", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BZDQ0NGU4ODAtMmVjOS00ZjA0LTgxNzAtNjRkNWEwMzA5YmU1XkEyXkFqcGc@._V1_.jpg"},
            {"title": "We Live in Time", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BODRhNDY5ZjctODRkMy00YzlmLTk1MDQtNzFlMGNlM2JlMWVjXkEyXkFqcGc@._V1_.jpg"}
        ]
    },
    "Horror": {
        "Recent": [
            {"title": "Talk to Me", "year": "2023", "poster": "https://m.media-amazon.com/images/M/MV5BOTU4NTM0MjEtMTE5Yi00ZDY2LThmYTctZmM0MDM1YmIwNWQyXkEyXkFqcGc@._V1_.jpg"},
            {"title": "M3GAN", "year": "2022", "poster": "https://m.media-amazon.com/images/M/MV5BY2NkMTExMzEtZmI3Yi00Yzc5LTk5N2QtNWY1ZjU2NWIwZmYwXkEyXkFqcGc@._V1_.jpg"},
            {"title": "Smile", "year": "2022", "poster": "https://m.media-amazon.com/images/M/MV5BMjQwOTExMjQ2OV5BMl5BanBnXkFtZTgwMDE2NjM1MTI@._V1_.jpg"},
            {"title": "Five Nights at Freddy's", "year": "2023", "poster": "https://m.media-amazon.com/images/M/MV5BZDU3OTQ3NmYtYmQ0NC00NWYyLWFjYTktOWIxMDQ4ZTJkY2JhXkEyXkFqcGc@._V1_.jpg"}
        ],
        "Classic": [
            {"title": "The Conjuring", "year": "2013", "poster": "https://m.media-amazon.com/images/M/MV5BOWQ4N2M3ZDQtMTA2MS00NTA4LWEyOTEtNzM0NTA5YWM5YTZiXkEyXkFqcGc@._V1_.jpg"},
            {"title": "Insidious", "year": "2010", "poster": "https://m.media-amazon.com/images/M/MV5BNzc4ODdjMDYtMjQzNS00Njg4LTg1MTgtNzhmOTNkOTRhZDEzXkEyXkFqcGc@._V1_.jpg"},
            {"title": "A Quiet Place", "year": "2018", "poster": "https://m.media-amazon.com/images/M/MV5BMjE2NzI3ODE4Ml5BMl5BanBnXkFtZTgwNjYwMjQ0NTM@._V1_.jpg"},
            {"title": "The Ring", "year": "2002", "poster": "https://m.media-amazon.com/images/M/MV5BNzQyMzY5Njg0OV5BMl5BanBnXkFtZTgwOTQzODI0MDE@._V1_.jpg"}
        ],
        "Trending": [
            {"title": "Longlegs", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BMTY5YzNlMDAtM2Y3MC00NDUxLTk0NGEtMmI1NTE1NTRmZmRhXkEyXkFqcGc@._V1_.jpg"},
            {"title": "The First Omen", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BMjQyOGYzZTYtYmY5Yi00OWIyLWJjNjMtNzk0MjQ4ODc1OTljXkEyXkFqcGc@._V1_.jpg"}
        ]
    },
    "Sci-Fi": {
        "Recent": [
            {"title": "Dune: Part Two", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BN2QzZDUwODQtOTQ3Zi00N2Q3LTlkOTQtMWY0MDk2ZmMyNTRmXkEyXkFqcGc@._V1_.jpg"},
            {"title": "The Creator", "year": "2023", "poster": "https://m.media-amazon.com/images/M/MV5BYzZhNmM1NjgtODhmYS00ZDU0LWFjYTgtOWY4MDE0ZmY2ODBlXkEyXkFqcGc@._V1_.jpg"},
            {"title": "Atlas", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BZWJhYTc0ZDUtMmJmZC00NTRmLWI0NmYtMjM4YjM4ZmM1ZTQwXkEyXkFqcGc@._V1_.jpg"},
            {"title": "Rebel Moon", "year": "2023", "poster": "https://m.media-amazon.com/images/M/MV5BOWQ0MWNkM2YtNjAyZi00NzE1LThjOWQtNzJmMjk4Y2YwMzY1XkEyXkFqcGc@._V1_.jpg"}
        ],
        "Classic": [
            {"title": "Interstellar", "year": "2014", "poster": "https://m.media-amazon.com/images/I/71niXI3lxlL._AC_UF1000,1000_QL80_.jpg"},
            {"title": "Inception", "year": "2010", "poster": "https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_UF1000,1000_QL80_.jpg"},
            {"title": "The Matrix", "year": "1999", "poster": "https://m.media-amazon.com/images/I/51EG732BV3L.jpg"},
            {"title": "Blade Runner 2049", "year": "2017", "poster": "https://m.media-amazon.com/images/M/MV5BODQ2MTA4MTItZjliZS00ZWIwLWI4MzEtYTI3YjNhNDI4ZjExXkEyXkFqcGc@._V1_.jpg"}
        ],
        "Trending": [
            {"title": "Furiosa: A Mad Max Saga", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BZGQ0MWYwNjEtYTQ4NC00OGY5LTk1ZDMtZjAzYzQ1YjIxMGM0XkEyXkFqcGc@._V1_.jpg"},
            {"title": "Kingdom of the Planet of the Apes", "year": "2024", "poster": "https://m.media-amazon.com/images/M/MV5BNzQ3NDdjYTktN2I2Yy00NjY5LWJmZjgtMzk2M2VkNTkyZGY4XkEyXkFqcGc@._V1_.jpg"}
        ]
    }
}

mood_map = {
    "Excited": "Action",
    "Happy": "Comedy",
    "Emotional": "Romance",
    "Scared": "Horror",
    "Mind-bending": "Sci-Fi"
}

if "submitted" not in st.session_state:
    st.session_state.submitted = False

def imdb_search_link(movie_title):
    query = movie_title.replace(" ", "+")
    return f"https://www.imdb.com/find/?q={query}"

def reset_app():
    st.session_state.submitted = False

st.markdown('<div class="main-title">🎬 CineMatch Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Get stylish movie recommendations based on genre, mood, and release preference</div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("🎛️ Choose Your Preferences")
    mood = st.selectbox("Select your mood", ["Excited", "Happy", "Emotional", "Scared", "Mind-bending"])
    genre = st.selectbox("Or choose a genre directly", list(movie_data.keys()))
    language = st.selectbox("Preferred language", ["English", "Hindi", "Korean", "Tamil", "Telugu"])
    category = st.selectbox("Choose movie category", ["Recent", "Classic", "Trending"])
    count = st.slider("How many movies do you want?", 2, 4, 3)

    if st.button("🎥 Get Recommendations"):
        st.session_state.submitted = True

    if st.button("🔄 Reset"):
        reset_app()

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="block-box">', unsafe_allow_html=True)
    st.subheader("🤖 Chatbot Conversation Flow")
    st.write("**Bot:** Hello! I can suggest movies for you.")
    st.write(f"**User Mood:** {mood}")
    st.write(f"**User Genre Choice:** {genre}")
    st.write(f"**User Language:** {language}")
    st.write(f"**User Preference:** {category}")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.submitted:
        final_genre = genre if genre else mood_map[mood]
        recommendations = movie_data[final_genre][category][:count]

        st.markdown('<div class="block-box">', unsafe_allow_html=True)
        st.subheader("✨ Recommended Movies For You")

        st.write(f"**Selected Genre:** {final_genre}")
        st.write(f"**Language Preference:** {language}")
        st.write(f"**Category:** {category}")

        for movie in recommendations:
            st.markdown(
                f"""
                <div class="movie-card">
                    <strong>🎞️ {movie['title']} ({movie['year']})</strong><br>
                    <a href="{imdb_search_link(movie['title'])}" target="_blank">🔗 Search on IMDb</a>
                </div>
                """,
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="block-box">', unsafe_allow_html=True)
    st.subheader("🖼️ Posters")
    if st.session_state.submitted:
        final_genre = genre if genre else mood_map[mood]
        recommendations = movie_data[final_genre][category][:count]
        for movie in recommendations:
            st.image(movie["poster"], caption=movie["title"], use_container_width=True)
    else:
        st.write("Posters will appear here after you click **Get Recommendations**.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Made with ❤️ using Streamlit | Movie recommendation demo chatbot</div>', unsafe_allow_html=True)
