import streamlit as st
from streamlit_option_menu import option_menu
from utils.sections import create_section
from utils.initialization import variables_intialization

st.set_page_config(layout='wide')


variables_intialization()


# Define the options for the menu
options = ["Capacitação", "QSHE", "Equipamentos e Ferramentas", "Pessoas", "Colaboração"]

# Create an option menu with dynamic icons
def get_icons():
    icons = []
    for section, completed in st.session_state.completion_status.items():
        icons.append('check-circle' if completed else 'circle')
    return icons

selected = option_menu(
    menu_title="Pesquisa de Satisfação TermoEletro",  # required
    options=options,  # required
    icons=get_icons(),  # optional, dynamically set icons
    menu_icon="menu",  # optional
    default_index=0,  # optional
    orientation="horizontal",  # horizontal or vertical
    key="main_menu"
)


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

