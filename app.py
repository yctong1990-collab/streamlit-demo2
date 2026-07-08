import streamlit as st
from PIL import Image

# App title
st.title("Simple Streamlit Demo")

# Header and subheader
st.header("Welcome to My App")
st.subheader("An interactive Python web app")

# Display text and markdown
st.text("This is plain text.")
st.markdown("**This is boldddd markdown text.**")

# Display status messages
st.success("Operation successful!")
st.info("Here is some information.")
st.warning("This is a warning.")
st.error("An error occurred.")

# Image display
img = Image.open("dog.jpg")
st.image(img, width=200)

# Checkbox
if st.checkbox("Show message"):
   st.write("Checkbox is checked!")
   
# Radio button
gender = st.radio("Select Gender:", ['Male', 'Female'])
st.success(f"Selected: {gender}")
if gender == "Male":
    st.write("You have chosen Male")
else:
    st.write("You have chosen Female")

# Selectbox - using a list variable instead of hardcoded values
hobbies = [&quot;Dancing&quot;, &quot;Reading&quot;, &quot;Sports&quot;, &quot;Gaming&quot;,
&quot;Cooking&quot;, &quot;Music&quot;, &quot;Photography&quot;, &quot;Gardening&quot;]
hobby = st.selectbox(&quot;Select your main hobby:&quot;, hobbies)
st.write(&quot;Your main hobby is:&quot;, hobby)

# Multiselect - lets the user pick more than one hobby
selected = st.multiselect(&quot;Pick all your hobbies:&quot;, hobbies)
# Loop through the selected hobbies and display each one
if selected:
st.write(f&quot;You selected {len(selected)} hobbies:&quot;)
for h in selected:
st.write(f&quot; - {h}&quot;)
else:
st.info(&quot;No hobbies selected yet.&quot;)

# Slider
level = st.slider("Choose a level", 1, 5)
st.write(f"Selected level: {level}")

# Text input
name = st.text_input("Enter your name", "Type here...")
if st.button("Submit"):
   st.success(f"Hello, {name.title()}!")
