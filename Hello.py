import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Olá",
        page_icon="👋❤",
    )

    st.write("#Bem Vindo ")

    st.sidebar.success("Selecione a Análise.")

    st.markdown(
        """
        Está é uma página de teste para análise de dados
        ### Sites de dados das estações meteorológicas
        - Página da [IFSC](https://www.wunderground.com/dashboard/pws/IPALHO4)
        """
    )


if __name__ == "__main__":
    run()
