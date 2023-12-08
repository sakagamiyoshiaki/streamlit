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
        ### Sites de dados do mercado
        - Página da [B3](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/cotacoes/)
        """
    )


if __name__ == "__main__":
    run()
