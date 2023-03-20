import streamlit as st
import pandas as pd
import numpy as np

st.header('Andreas Hidayat 32200081')

st.write("Line Chart")
chart_data = pd.DataFrame(
    {
    'first column': [1, 4, 3, 2],
    'second column': [10, 50, 30, 40],
    'third column': [35, 25, 45, 60]

    },
     columns=['first column', 'second column', 'third column'])
st.line_chart(chart_data)