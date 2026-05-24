

import streamlit as st
st.title("Hello Streamlit!")
#text input
name = st.text_input("Enter your name")


 


# Button interaction
if st.button("Greetme"):
     st.write(f"Hello, {name}!")


 


# Choose a color
color = st.selectbox("Pick a color", ["Red", "Green","Blue","Purple"])
st.write(f"You chose: {color}")

# Simple slider
value = st.slider("Pick a number", 0, 100)
st.write(f"Number selected: {value}")