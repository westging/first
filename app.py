import streamlit as st
import sqlite3
import pandas as pd
import os.path

con = sqlite3.connect('db.db')
cur = con.cursor()

def login_user(id, password):
    cur.execute(f"SELECT * " 
                f"FROM users "
                f"WHERE id='{id}'and password='{password}'")
    return cur.fetchone()

menu = st.sidebar.selectbox('Menu', options =['Sign in', 'Sign up', 'Members list'])

if menu == 'Sign in':
    st.subheader('Sign in')

    login_id = st.text_input('id', placeholder='enter your id')
    login_pw = st.text_input('password',
                             placeholder='enter your password'
                             , type='password')
    login_btn = st.button('Sign in')

    if login_btn:

        user_info = login_user(login_id, login_pw)
        filename = './img/'+user_info[0]+'.png'

        if os.path.exists(filename):
            st.sidebar.image(filename)
            st.sidebar.title(user_info[0])
            st.sidebar.write('{}님, 환영합니다.'.format(user_info[4]))
        else:
            st.sidebar.write('{}님, 환영합니다.'.format(user_info[4]))



if menu == 'Sign up':
    st.subheader('Sign up')
    st.info("Fill this form and click 'Sign Up' button")

    uid = st.text_input('id', max_chars=10, placeholder='enter your id')
    name = st.text_input('name', max_chars=10, placeholder='enter your name')
    upw = st.text_input('password',type='password', placeholder='enter your password')
    upw_chk = st.text_input('check your password', type='password', placeholder='check your password')
    age = st.text_input('age', placeholder='enter your age')
    gender = st.radio(
        'gender', options=['W','M'], horizontal=True
    )


    signup_btn = st.button('Sign up')

    if signup_btn:

        if upw != upw_chk:
            st.warning('Please check your password again')
            st.stop()

        cur.execute(f"INSERT INTO users(id, password, gender, age, name) "
                    f"VALUES('{uid}', '{upw}', '{gender}', {age}, '{name}')"
                    )
        st.success('Successful Sign Up')
        con.commit()

if menu == 'Members list':
    st.subheader('Members list')

    df = pd.read_sql('SELECT name,gender,id FROM users', con)
    st.dataframe(df)

    st.sidebar.subheader('Members list')


