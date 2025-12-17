import streamlit as st
st.title("My First streamlit App")
name = st.text_input("Enter your name")
st.write("Hello",name)
age = st.slider("Age", 0, 100)
st.write("Your age is", age)



if st.button("Say Hello"):
    st.write(f"Hello {name},nnice to meet you")
   
gender = st.radio("Select Gender", ["Male", "Female", "Other"])
st.write("You selected:", gender)

feedback = st.text_area("Enter your feedback")
st.write("You wrote:", feedback)

height = st.number_input("Enter your height in cm", min_value=50, max_value=250)
st.write("Your height:", height)

color = st.selectbox("Pick a color", ["Red", "Green", "Blue"])
if color == "Red":
    st.write("Stop! Danger ahead!")
else:
    st.write(f"You picked {color}.")