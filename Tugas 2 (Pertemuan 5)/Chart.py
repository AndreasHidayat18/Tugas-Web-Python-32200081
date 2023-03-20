import streamlit as st
import pandas as pd
import numpy as np

st.write("Line chart")
chart_data = pd.DataFrame(
     np.random.randn(30, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)