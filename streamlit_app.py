import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = similariti[index]
    movies_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movi_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movi_dict)
similariti = pickle.load(open('similariti.pkl','rb'))



st.title('Movie Recommendation System')

Selected_movie = st.selectbox(
    'Search Your Movie',
    movies['title'].values)

if st.button('Recommend'):
    recommendatation = recommend(Selected_movie)
    for i in recommendatation:
        st.write(i)
    