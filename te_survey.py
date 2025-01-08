import streamlit as st
from streamlit_star_rating import st_star_rating

#stars = st_star_rating("Please rate your experience", maxValue=5, defaultValue=3)
#st.write(f"You rated {stars} stars!")
#st_star_rating(label = "Please rate you experience", maxValue = 5, defaultValue = 3, key = "rating", customCSS = "div {background-color: red;}" )

# Set page title
st.title("Survey with Star Ratings")

# Questions for the survey
questions = [
    "Atendimento ao Plano de Capacitação",
    "Problemas Técnicos",
    "Comentários sobre classificação",
]

# Dictionary to store responses
responses = {}

# Function to display star rating
def star_rating(label):
    return st_star_rating(label, maxValue=5,defaultValue=None)

# Display questions with star ratings
for question in questions:
    responses[question] = star_rating(question)

# Submit button
if st.button("Submeter"):
    st.write("Thank you for your responses!")
    st.write(responses)


import streamlit as st

# Create a sidebar for navigation
page = st.sidebar.selectbox("Select a page:", ["Page 1", "Page 2", "Page 3"])

# Define the content for each page
if page == "Page 1":
    st.title("Page 1")
    st.write("This is the content of Page 1.")
    # Add your form elements for Page 1 here
elif page == "Page 2":
    st.title("Page 2")
    st.write("This is the content of Page 2.")
    # Add your form elements for Page 2 here
elif page == "Page 3":
    st.title("Page 3")
    st.write("This is the content of Page 3.")
    # Add your form elements for Page 3 here
