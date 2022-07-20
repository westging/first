import streamlit as st

st.markdown('## This is Markdown')
st.markdown('Streamlit is  **_really_ cool**')

st.caption('This is a string that explains something above')

code = '''def hello():
    print("Hello, Streamlit!")'''

st.code(code, language='python')

if st.button('button'):
    st.write('success')
else:
    st.write('hello')

text_contents = 'download file'
st.download_button('download', text_contents)

st.subheader('1, Checkbox test')
a = st.checkbox('no1')
b = st.checkbox('no2')
c = st.checkbox('no3')

if a:
    st.write('1 is chosen')
if b:
    st.write('2 is chosen')
if c :
    st.write('3 is chosen')

st.subheader('radiobutton')
food = st.radio(
    'what is your favorite food',
    ('sushi', 'ramen', 'rice')
)


if food == 'sushi':
    st.write('you selected sushi')
elif food == 'ramen':
    st.write('you selected reamen')
elif food == 'rice':
    st.write('you selected rice'
             )