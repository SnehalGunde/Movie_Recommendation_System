import streamlit as st
import pickle
import pandas as pd

similarity=pickle.load(open('similarity.pkl','rb'))
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommended_movies =[]
    for i in movie_list[1:6]:
        movie_id=i[0]
        #fetch poster from API

        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

st.title("Movie Recommender System")
selected_option= st.selectbox(" Select the movie name", movies['title'].values)

if st.button('Recommend'):
    recommendations= recommend(selected_option)
    for i in recommendations:
        st.write(i)