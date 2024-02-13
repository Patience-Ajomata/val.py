import streamlit as st

# Tittle
st.title('VALENTINE REQUEST TO YOU MY LOVE...')

st.text('WILL YOU BE MY VALENTINE ?')
if st.button('YES'):
    st.write('yassss!!!')

if st.button('NO'):
    st.write('argh!!!, we try again next year.')

#[theme]
base="light"
primaryColor="#920606"
backgroundColor="#9e0606"
textColor="#fbfbfd"
font="monospace"
