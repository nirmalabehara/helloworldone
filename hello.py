import streamlit as st


st.title("Simple Streamlit App")

slider_value = st.slider("Select a number", min_value=0, max_value=100, value=50)
st.write(f"Slider value: {slider_value}")
st.write(f"Square of the slider value: {slider_value ** 2}")

user_input = st.text_input("Enter some text")
st.write(f"You entered: {user_input}")

if st.button("Click me"):
    st.write("Button was clicked!")

import datetime
st.write("Current time:", datetime.datetime.now())

