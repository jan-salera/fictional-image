import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Where?", page_icon="🌍")

st.header("Where are you from?")

st.write("I was born and raised in the state of Michigan!")
st.markdown("**This makes me about 40-ish minutes away from the heart of Detroit!**")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [42.67, -83.03],
    columns=['lat', 'lon'])

st.map(map_data, zoom = 6.6)

st.markdown("However, I currently reside in East Lansing as I attend Michigan State for my Bachelor's in Electrical Engineering.")
st.image('https://th.bing.com/th/id/OIP.9KKh6rcjACJJtitgw-1rOwHaEY?rs=1&pid=ImgDetMain',width = 600)