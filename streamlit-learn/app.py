# import streamlit as st
# import pandas as pd

# st.write("Here's our first attempt at using data to create a table:")
# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })
# # st.table(df)
# st.dataframe(df)

##############################################
# import streamlit as st
# import numpy as np

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)
#############################################

import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

# st.dataframe(dataframe.style.highlight_max(axis=0))
st.table(dataframe)