import streamlit as st

left_column, right_column = st.columns(2)

left_column.button("Press Me!")

# or better, call streamlit functions inside a 'with' block:
with right_column:
    chosen = st.radio(
        'Sorting Hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", 'Slytherin')
    )
    st.write(f"You are in {chosen} house!")