import streamlit as st

st.title("Movie Recommendation Chatbot")
st.write("Hello! I will help you find a movie.")

if "step" not in st.session_state:
    st.session_state.step = 1
if "genre" not in st.session_state:
    st.session_state.genre = ""
if "language" not in st.session_state:
    st.session_state.language = ""
if "type_pref" not in st.session_state:
    st.session_state.type_pref = ""

if st.session_state.step == 1:
    st.subheader("Step 1: Select Genre")
    genre = st.selectbox("Choose genre", ["Action", "Comedy", "Romance", "Horror", "Sci-Fi"])
    if st.button("Next"):
        st.session_state.genre = genre
        st.session_state.step = 2

elif st.session_state.step == 2:
    st.subheader("Step 2: Select Language")
    language = st.selectbox("Choose language", ["English", "Hindi", "Korean", "Tamil"])
    if st.button("Next"):
        st.session_state.language = language
        st.session_state.step = 3

elif st.session_state.step == 3:
    st.subheader("Step 3: Select Type")
    type_pref = st.selectbox("Choose type", ["Recent", "Classic"])
    if st.button("Show Recommendations"):
        st.session_state.type_pref = type_pref
        st.session_state.step = 4

elif st.session_state.step == 4:
    st.subheader("Recommended Movies")

    genre = st.session_state.genre

    if genre == "Action":
        recs = ["John Wick", "Mad Max: Fury Road", "Extraction"]
    elif genre == "Comedy":
        recs = ["The Mask", "Superbad", "3 Idiots"]
    elif genre == "Romance":
        recs = ["Titanic", "The Notebook", "La La Land"]
    elif genre == "Horror":
        recs = ["The Conjuring", "Insidious", "A Quiet Place"]
    else:
        recs = ["Interstellar", "Inception", "The Matrix"]

    st.write("Your choices:")
    st.write("Genre:", st.session_state.genre)
    st.write("Language:", st.session_state.language)
    st.write("Type:", st.session_state.type_pref)

    st.write("Movie suggestions:")
    for movie in recs:
        st.write("- ", movie)

    again = st.radio("Do you want more recommendations?", ["No", "Yes"])

    if st.button("Finish"):
        if again == "Yes":
            st.session_state.step = 1
        else:
            st.success("Thank you for using the chatbot!")
