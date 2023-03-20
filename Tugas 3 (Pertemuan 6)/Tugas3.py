import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


# 1. Write and Magic

st.title("1. Write and Magic")
st.write('Halo, ini merupakan contoh menggunakan st.write')

('Sementara Kalimat ini ditulis menggunakan Magic yang merupakan command yang dapat menuliskan sesuatu tanpa command st.write, command yang digunakan adalah : (petik text petik)')

# 2. Text Element

st.title("2. Text Element")
st.title("Text ini dibuat menggunakan st.title")

st.markdown('My name is :blue[Andreas] **:green[Hidayat]**')
st.markdown('Kalimat ini dibuat menggunakan st.markdown yang dapat memberi warna')

st.markdown('The **_:green[closer]_** you think you are , the **_:green[Less]_** you will actually see')

# 3. Data Display Elements
st.title("3. Data Display Elements")
df = pd.DataFrame(
   np.random.randn(21, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)

# 4. Chart Elements
st.title("4. Chart Elements")
chart_data = pd.DataFrame(
    np.random.randn(30, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)

# 5. Input Widget
st.title("5. Input Widget")

st.write('Silahkan Masukan Nama Anda: ')
# Input Text Widget
nama = st.text_input('Nama', '')

# 6. Media Elements
st.title("6. Media Elements")

img = Image.open("E:/babygroot.JPG")

st.image(img, caption='Baby Groot GOTG')

# 7. Layouts and Containers
st.title("7. Layouts and Containers")

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Phone", "Message")
)

with st.container():
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")


# 8. Status Element
st.title("8. Status Element")
st.warning('THIS IS WARNING!', icon="⚠️")

st.error("[ERROR]: maaf anda kalah", icon="🪲")

# 9. Control Flow
st.title("9. Control Flow")

name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')

# 10. Utilities
st.title("10. Utilities")

with st.echo():
    st.write('Ini Merupakan perintah echo Utilities!')