import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c']
    )

    chart_data

df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first_column']
)
'You selected: ', option