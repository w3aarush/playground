# import streamlit as st
# x = st.slider('x')
# st.write(x, 'squared is', x * x)

import streamlit as st
st.text_input("Your name", key='name')

# you can access the value at any point with:
st.session_state.name