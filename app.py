
import streamlit as st
import re
import random
from urllib.parse import quote_plus

st.set_page_config(
    page_title="MovieMate - Your Movie Companion",
    page_icon="🎬",
    layout="wide"
)

# =====================================
# STYLING
# =====================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(125deg,
        #101025 0%, #231942 58%, #391b43 100%);
    color: #f8fafc;
}
[data-testid="stSidebar"] {
    background: #19152e;
}
.hero {
    background: linear-gradient(110deg, #6d28d9, #be185d);
    padding: 34px;
    border-radius: 22px;
    color: white;
    margin-bottom: 20px;
}
.hero h1, .hero p {
    color: white !important;
}
[data-testid="stChatMessage"] {
    background: #2a2347;
    border: 1px solid #67558a;
    border-radius: 16px;
}
.stButton button, .stLinkButton a {
    border-radius: 12px;
}
.movie-card {
    background: #292242;
    border: 1px solid #594876;
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 10px;
}
.movie-card h3, .movie-card p {
    color: #f8fafc !important;
}
.small-text {
    color: #ddd6fe !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🎬 MovieMate</h1>
<p>Your Smart Mood-Based Movie Recommendation Chatbot</p>
<p>💜 Tell us your mood. Discover your next favorite movie.</p>
</div>
""", unsafe_allow_html=True)

# =====================================
# CURATED MOVIE DATABASE
# =====================================

# Title | Year | Language | Genres | Moods | Minutes | Description

DATA = [
    ("3 Idiots", 2009, "Hindi", "Comedy,Drama",
     "Happy,Inspiring,Comfort", 170,
     "Three friends discover the meaning of success and friendship."),

    ("Zindagi Na Milegi Dobara", 2011, "Hindi",
     "Adventure,Comedy,Drama", "Happy,Comfort,Inspiring", 153,
     "A memorable road trip changes three friends' lives."),

    ("Queen", 2013, "Hindi", "Comedy,Drama",
     "Happy,Inspiring,Comfort", 146,
     "A young woman discovers independence during a solo trip."),

    ("Dear Zindagi", 2016, "Hindi", "Drama,Romance",
     "Comfort,Emotional,Inspiring", 151,
     "A young woman learns about life and emotional wellbeing."),

    ("Jab We Met", 2007, "Hindi", "Romance,Comedy",
     "Romantic,Happy,Comfort", 138,
     "Two strangers meet during an unexpected train journey."),

    ("Barfi!", 2012, "Hindi", "Romance,Drama,Comedy",
     "Romantic,Emotional,Comfort", 151,
     "A heartwarming story about love and connection."),

    ("Andhadhun", 2018, "Hindi", "Thriller,Mystery,Crime",
     "Thrilling,Mind-bending,Dark", 139,
     "A pianist becomes involved in a dangerous mystery."),

    ("Drishyam", 2015, "Hindi", "Thriller,Drama,Crime",
     "Thrilling,Mind-bending,Dark", 163,
     "A father devises a plan to protect his family."),

    ("Tumbbad", 2018, "Hindi", "Horror,Fantasy,Thriller",
     "Scary,Dark,Thrilling", 104,
     "A supernatural story exploring greed and obsession."),

    ("Stree", 2018, "Hindi", "Horror,Comedy",
     "Scary,Happy,Thrilling", 128,
     "A mysterious ghost legend troubles a small town."),

    ("Dangal", 2016, "Hindi", "Drama,Sport",
     "Inspiring,Emotional", 161,
     "A father trains his daughters to become wrestlers."),

    ("Taare Zameen Par", 2007, "Hindi", "Drama,Family",
     "Emotional,Inspiring,Comfort", 165,
     "A teacher recognizes a child's unique abilities."),

    ("12th Fail", 2023, "Hindi", "Drama",
     "Inspiring,Emotional", 147,
     "An aspiring civil servant perseveres despite obstacles."),

    ("Laapataa Ladies", 2023, "Hindi", "Comedy,Drama",
     "Happy,Inspiring,Comfort", 124,
     "Two newly married women are accidentally switched."),

    ("The Lunchbox", 2013, "Hindi", "Romance,Drama",
     "Romantic,Comfort,Emotional", 104,
     "A misplaced lunchbox creates an unexpected connection."),

    ("Kahaani", 2012, "Hindi", "Thriller,Mystery",
     "Thrilling,Mind-bending,Dark", 122,
     "A woman's search in Kolkata uncovers hidden secrets."),

    ("Inception", 2010, "English", "Science Fiction,Thriller",
     "Mind-bending,Thrilling", 148,
     "A team enters dreams to influence people's ideas."),

    ("Interstellar", 2014, "English",
     "Science Fiction,Adventure,Drama",
     "Mind-bending,Emotional,Inspiring", 169,
     "Astronauts explore space to secure humanity's future."),

    ("The Dark Knight", 2008, "English", "Action,Crime,Thriller",
     "Thrilling,Dark", 152,
     "Batman faces the Joker in a battle against chaos."),

    ("Knives Out", 2019, "English", "Mystery,Comedy,Crime",
     "Thrilling,Happy,Mind-bending", 130,
     "A detective investigates a wealthy family's secrets."),

    ("Shutter Island", 2010, "English", "Mystery,Thriller",
     "Mind-bending,Dark,Thrilling", 138,
     "An isolated psychiatric facility hides disturbing mysteries."),

    ("The Prestige", 2006, "English", "Mystery,Drama,Thriller",
     "Mind-bending,Dark,Thrilling", 130,
     "Two magicians become consumed by rivalry."),

    ("The Shawshank Redemption", 1994, "English", "Drama",
     "Inspiring,Emotional,Comfort", 142,
     "A powerful story about hope, patience and friendship."),

    ("The Pursuit of Happyness", 2006, "English", "Drama",
     "Inspiring,Emotional", 117,
     "A father works relentlessly to improve his family's future."),

    ("Little Miss Sunshine", 2006, "English", "Comedy,Drama",
     "Happy,Comfort,Emotional", 101,
     "An unconventional family takes an unforgettable road trip."),

    ("About Time", 2013, "English", "Romance,Comedy,Drama",
     "Romantic,Comfort,Emotional", 123,
     "A man learns about love, family and appreciating life."),

    ("La La Land", 2016, "English", "Romance,Drama,Musical",
     "Romantic,Emotional", 128,
     "Two aspiring artists balance romance and ambition."),

    ("10 Things I Hate About You", 1999, "English",
     "Romance,Comedy", "Romantic,Happy,Comfort", 97,
     "An entertaining teenage romantic comedy."),

    ("The Conjuring", 2013, "English", "Horror,Thriller",
     "Scary,Dark,Thrilling", 112,
     "Paranormal investigators confront a haunting."),

    ("Get Out", 2017, "English", "Horror,Mystery,Thriller",
     "Scary,Mind-bending,Dark", 104,
     "A family visit becomes increasingly disturbing."),

    ("A Quiet Place", 2018, "English", "Horror,Thriller",
     "Scary,Thrilling", 90,
     "A family must remain silent to survive."),

    ("Coco", 2017, "English", "Animation,Family,Adventure",
     "Comfort,Happy,Emotional", 105,
     "A young musician explores his family's history."),

    ("Inside Out", 2015, "English", "Animation,Family,Comedy",
     "Comfort,Emotional,Happy", 95,
     "A story about the emotions guiding a young girl."),

    ("Spider-Man: Into the Spider-Verse", 2018, "English",
     "Animation,Action,Adventure", "Happy,Inspiring,Thrilling", 117,
     "A young hero discovers a universe of Spider-People."),

    ("Everything Everywhere All at Once", 2022, "English",
     "Science Fiction,Comedy,Adventure",
     "Mind-bending,Emotional,Happy", 139,
     "A woman explores extraordinary alternate realities."),

    ("Parasite", 2019, "Korean", "Thriller,Drama",
     "Dark,Mind-bending,Thrilling", 132,
     "Two families become entangled across class boundaries."),

    ("Train to Busan", 2016, "Korean",
     "Horror,Action,Thriller", "Scary,Thrilling,Emotional", 118,
     "Passengers struggle to survive a zombie outbreak."),

    ("My Sassy Girl", 2001, "Korean", "Romance,Comedy",
     "Romantic,Happy,Emotional", 123,
     "An unpredictable relationship blossoms."),

    ("Your Name", 2016, "Japanese",
     "Animation,Romance,Fantasy", "Romantic,Emotional,Mind-bending",
     106, "Two teenagers form a mysterious connection."),

    ("Spirited Away", 2001, "Japanese",
     "Animation,Fantasy,Adventure", "Comfort,Happy,Mind-bending",
     125, "A girl explores an enchanting spirit world."),

    ("Howl's Moving Castle", 2004, "Japanese",
     "Animation,Fantasy,Romance", "Comfort,Romantic,Mind-bending",
     119, "A magical adventure involving a moving castle."),

    ("RRR", 2022, "Telugu", "Action,Drama,Adventure",
     "Thrilling,Inspiring", 187,
     "Two revolutionaries forge an extraordinary friendship."),

    ("Baahubali: The Beginning", 2015, "Telugu",
     "Action,Fantasy,Drama", "Thrilling,Inspiring", 159,
     "A warrior discovers his royal identity."),

    ("Eega", 2012, "Telugu", "Fantasy,Action,Comedy",
     "Happy,Thrilling", 134,
     "A man is reborn as a fly and seeks revenge."),

    ("Kantara", 2022, "Kannada", "Action,Thriller,Drama",
     "Dark,Thrilling", 148,
     "A conflict involving land, tradition and belief."),

    ("Kumbalangi Nights", 2019, "Malayalam",
     "Drama,Comedy", "Comfort,Emotional", 135,
     "Brothers reconnect and rebuild their relationships."),

    ("Premam", 2015, "Malayalam", "Romance,Comedy,Drama",
     "Romantic,Comfort,Emotional", 156,
     "A man experiences love across different life stages.")
]

MOVIES = []

for title, year, language, genres, moods, minutes, description in DATA:
    MOVIES.append({
        "title": title,
        "year": year,
        "language": language,
        "genres": genres.split(","),
        "moods": moods.split(","),
        "minutes": minutes,
        "description": description
    })

# =====================================
# MOOD DETECTION
# =====================================

MOOD_KEYWORDS = {
    "Happy": ["happy", "fun", "funny", "laugh", "comedy"],
    "Comfort": ["sad", "stressed", "comfort", "cozy",
                "lonely", "relax", "down", "wholesome"],
    "Romantic": ["love", "romance", "romantic", "date"],
    "Thrilling": ["thriller", "thrill", "suspense",
                  "action", "exciting"],
    "Mind-bending": ["mystery", "twist", "mind",
                     "brain", "intelligent"],
    "Emotional": ["cry", "emotional", "touching", "tear"],
    "Inspiring": ["inspire", "inspiring", "motivation",
                  "study", "career", "success"],
    "Scary": ["scary", "horror", "ghost", "haunted"],
    "Dark": ["dark", "serious", "intense", "gritty"]
}

def detect_moods(text):
    text = text.lower()
    detected = []

    for mood, keywords in MOOD_KEYWORDS.items():
        if any(word in text for word in keywords):
            detected.append(mood)

    return detected

# =====================================
# SIDEBAR FILTERS
# =====================================

ALL_GENRES = sorted({
    g for movie in MOVIES for g in movie["genres"]
})

ALL_LANGUAGES = sorted({
    movie["language"] for movie in MOVIES
})

with st.sidebar:
    st.title("🎭 Personalize Your Vibe")

    selected_mood = st.selectbox(
        "Choose your mood",
        ["Any Mood"] + list(MOOD_KEYWORDS.keys())
    )

    selected_genre = st.selectbox(
        "Favorite Genre",
        ["Any Genre"] + ALL_GENRES
    )

    selected_language = st.selectbox(
        "Preferred Language",
        ["Any Language"] + ALL_LANGUAGES
    )

    duration = st.selectbox(
        "Movie Duration",
        ["Any Duration", "Under 2 Hours", "Under 2.5 Hours"]
    )

    result_count = st.slider(
        "Number of Recommendations",
        2, 8, 4
    )

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.chat = []
        st.session_state.seen = []
        st.rerun()

    st.caption("Curated recommendations. No paid AI API needed.")

# =====================================
# SESSION STATE
# =====================================

if "chat" not in st.session_state:
    st.session_state.chat = []

if "seen" not in st.session_state:
    st.session_state.seen = []

# =====================================
# RECOMMENDATION ENGINE
# =====================================

def get_recommendations(query="", exclude=None):
    query_lower = query.lower()
    moods = detect_moods(query)

    if selected_mood != "Any Mood":
        moods.append(selected_mood)

    matched_genres = [
        g for g in ALL_GENRES
        if g.lower() in query_lower
    ]

    matched_languages = [
        lang for lang in ALL_LANGUAGES
        if lang.lower() in query_lower
    ]

    scored = []

    for movie in MOVIES:
        if selected_genre != "Any Genre":
            if selected_genre not in movie["genres"]:
                continue

        if selected_language != "Any Language":
            if movie["language"] != selected_language:
                continue

        if duration == "Under 2 Hours" and movie["minutes"] >= 120:
            continue

        if duration == "Under 2.5 Hours" and movie["minutes"] >= 150:
            continue

        if matched_genres and not any(
            g in movie["genres"] for g in matched_genres
        ):
            continue

        if matched_languages:
            if movie["language"] not in matched_languages:
                continue

        score = 1 + sum(
            4 for m in moods if m in movie["moods"]
        )

        if "short" in query_lower and movie["minutes"] < 120:
            score += 2

        if "recent" in query_lower or "new" in query_lower:
            if movie["year"] >= 2020:
                score += 2

        if "classic" in query_lower and movie["year"] < 2010:
            score += 2

        if movie["title"] in (exclude or []):
            score -= 100

        scored.append((score, movie))

    rng = random.Random(
        query_lower + str(selected_mood)
        + str(selected_genre) + str(selected_language)
    )

    rng.shuffle(scored)
    scored.sort(key=lambda item: item[0], reverse=True)

    available = [
        movie for score, movie in scored
        if score > 0
    ]

    return available[:result_count]

# =====================================
# MOVIE DISPLAY
# =====================================

def movie_card(movie):
    st.markdown(
        f"### 🎞️ {movie['title']} ({movie['year']})"
    )

    st.write(movie["description"])

    st.caption(
        f"🎭 {', '.join(movie['genres'])} | "
        f"🌍 {movie['language']} | "
        f"⏱️ {movie['minutes']} minutes"
    )

    st.caption(
        "Mood: " + ", ".join(movie["moods"])
    )

    imdb = (
        "https://www.imdb.com/find/?q="
        + quote_plus(movie["title"] + " " + str(movie["year"]))
    )

    watch = (
        "https://www.justwatch.com/in/search?q="
        + quote_plus(movie["title"])
    )

    c1, c2 = st.columns(2)

    with c1:
        st.link_button(
            "⭐ IMDb Details",
            imdb,
            use_container_width=True
        )

    with c2:
        st.link_button(
            "📺 Find Where to Watch",
            watch,
            use_container_width=True
        )

    st.divider()

# =====================================
# QUICK SUGGESTIONS
# =====================================

st.subheader("✨ Discover Movies Based on Your Feelings")

quick_questions = [
    "I feel sad and need a comforting movie",
    "Suggest a romantic movie",
    "I want an exciting thriller",
    "Show me a mind-blowing movie"
]

columns = st.columns(4)

for i, suggestion in enumerate(quick_questions):
    with columns[i]:
        if st.button(
            suggestion,
            key=f"quick_{i}",
            use_container_width=True
        ):
            st.session_state.quick_prompt = suggestion

# =====================================
# MAIN TABS
# =====================================

chat_tab, explore_tab, about_tab = st.tabs([
    "💬 Movie Chatbot",
    "🍿 Discover Movies",
    "ℹ️ About Project"
])

# =====================================
# CHATBOT
# =====================================

with chat_tab:

    for item in st.session_state.chat:
        with st.chat_message(item["role"]):
            st.write(item["message"])

            for movie in item.get("movies", []):
                movie_card(movie)

    user_message = st.chat_input(
        "Tell me your mood, genre or movie preference..."
    )

    question = user_message or st.session_state.pop(
        "quick_prompt", None
    )

    if question:
        is_more = any(
            word in question.lower()
            for word in [
                "more", "another", "different",
                "else", "next"
            ]
        )

        excluded = (
            st.session_state.seen if is_more else []
        )

        recommendations = get_recommendations(
            question, excluded
        )

        if recommendations:
            response = (
                "🍿 Here are some movies that match your "
                "mood and preferences!"
            )

            st.session_state.seen.extend(
                movie["title"]
                for movie in recommendations
            )

        else:
            response = (
                "I couldn't find matching movies. "
                "Try changing your filters or requesting "
                "a different mood."
            )

        st.session_state.chat.extend([
            {
                "role": "user",
                "message": question
            },
            {
                "role": "assistant",
                "message": response,
                "movies": recommendations
            }
        ])

        st.rerun()

    if not st.session_state.chat:
        st.info(
            "👋 Tell MovieMate how you're feeling "
            "to get movie recommendations."
        )

# =====================================
# MOVIE DISCOVERY
# =====================================

with explore_tab:
    st.subheader("🎬 Explore Handpicked Movies")

    st.write(
        f"Discover from {len(MOVIES)} curated movies."
    )

    if st.button("🎲 Surprise Me"):
        choices = get_recommendations() or MOVIES
        st.session_state.surprise = random.choice(choices)

    if "surprise" in st.session_state:
        movie_card(st.session_state.surprise)

    recommendations = get_recommendations()

    if not recommendations:
        st.warning("No movies match your filters.")

    for movie in recommendations:
        movie_card(movie)

# =====================================
# ABOUT
# =====================================

with about_tab:
    st.markdown("""
    ### About MovieMate

    MovieMate is an interactive mood-based movie
    recommendation chatbot built using Python and Streamlit.

    **Features**
    - Mood-based recommendations
    - Natural-language keyword matching
    - Genre and language filtering
    - Movie duration filtering
    - Multilingual curated movie catalog
    - Interactive recommendations
    - IMDb search links
    - Where-to-watch search links
    - Chat history

    MovieMate uses a rule-based recommendation engine,
    rather than generative AI.
    """)

st.divider()
st.caption(
    "🎬 MovieMate | Python • Streamlit • Recommendation System"
)
