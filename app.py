import streamlit as st
import sqlite3

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
        st.write('{}님, 환영합니다.'.format(user_info[4]))


if menu == 'Sign up':
    st.subheader('Sign up')
    st.sidebar.subheader('Sign up')
if menu == 'Members list':
    st.subheader('Members list')
    st.sidebar.subheader('Members list')
