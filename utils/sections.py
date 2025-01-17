import streamlit as st
from streamlit_star_rating import st_star_rating
from streamlit_extras.stylable_container import stylable_container

css_styles = """
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                //background: rgba(47,60,144,0.2);
                padding: calc(1em - 1px)
            }
            """

# Function to create star rating questions and comments
def create_section(title, questions):
    with stylable_container(
        key="container_with_border",
        css_styles=css_styles,
    ):
        with st.container():
            st.warning(title)

            all_answered = True

            for question in questions:
                key = f"{title}_{question}"
                
                # Initialize session state for each question's rating
                if key not in st.session_state.ratings:
                    st.session_state.ratings[key] = None

                with st.container(border=True):
                    # Get the rating value from session state
                    rating = st_star_rating(question, maxValue=5, defaultValue=st.session_state.ratings[key], emoticons=True, key=f"rating_{key}")

                # Update session state with the current rating
                st.session_state.ratings[key] = rating

                if rating is None:
                    all_answered = False

            # Initialize session state for comments
            if title not in st.session_state.comments:
                st.session_state.comments[title] = ""

            # Get the comments value from session state
            comments = st.text_area(f"Comentários sobre {title}", value=st.session_state.comments[title], key=f"comments_{title}")

            # Update session state with the current comments
            st.session_state.comments[title] = comments

            # Update completion status
            st.session_state.completion_status[title] = all_answered