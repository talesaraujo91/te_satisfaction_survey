import streamlit as st

def variables_intialization():
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