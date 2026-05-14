import streamlit as st

# add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# add a slider to the sidebar
add_slider = st.sidebar.slider(
    'Select a range to values',
    0.0, 1000.0, (25.0, 75.0)
)