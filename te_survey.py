import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_star_rating import st_star_rating
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(layout='wide')

css_styles = """
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                background: rgba(255,255,255,0.8);
                padding: calc(1em - 1px)
            }
            """

# Initialize session state to keep track of completion status and user inputs
if 'completion_status' not in st.session_state:
    st.session_state.completion_status = {
        "Capacitação": False,
        "QSHE": False,
        "Equipamentos e Ferramentas": False,
        "Pessoas": False,
        "Colaboração": False
    }

if 'ratings' not in st.session_state:
    st.session_state.ratings = {}

if 'comments' not in st.session_state:
    st.session_state.comments = {}

# Define the options for the menu
options = ["Capacitação", "QSHE", "Equipamentos e Ferramentas", "Pessoas", "Colaboração"]

# Create an option menu with dynamic icons
def get_icons():
    icons = []
    for section, completed in st.session_state.completion_status.items():
        icons.append('check-circle' if completed else 'circle')
    return icons

selected = option_menu(
    menu_title=None,  # required
    options=options,  # required
    icons=get_icons(),  # optional, dynamically set icons
    menu_icon="menu",  # optional
    default_index=0,  # optional
    orientation="horizontal",  # horizontal or vertical
    key="main_menu"
)

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

# Define the content for each section
if selected == "Capacitação":
    create_section("Capacitação", ["Atendimento ao Plano de Capacitação", "Problemas Técnicos"])

elif selected == "QSHE":
    create_section("QSHE", ["Uso de materiais e equipamentos", "Qualidade", "Contaminação do Solo"])

elif selected == "Equipamentos e Ferramentas":
    create_section("Equipamentos e Ferramentas", ["Disponibilidade", "Adequação", "Conservação"])

elif selected == "Pessoas":
    create_section("Pessoas", ["Quantidade e Qualidade", "Equipe de Apoio", "Agilidade", "Motivação", "Horas Extras", "Discriminação", "Uniformes"])

elif selected == "Colaboração":
    create_section("Colaboração", ["Cooperação / Disposição", "Proatividade", "Precisão e agilidade"])

