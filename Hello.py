import streamlit as st
from streamlit.logger import get_logger

from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestore-key.json")

# Create a reference to the Google post.
doc_ref = db.collection("stations").document("maciambu")

# Then get the data at that reference.
doc = doc_ref.get()


LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Olá",
        page_icon="👋❤",
    )

    st.write("#Bem Vindo ")

    st.sidebar.success("Selecione a Análise.")
    # Let's see what we got!
    st.write("The id is: ", doc.id)
    st.write("The contents are: ", doc.to_dict())


    st.markdown(
        """
        Está é uma página de teste para análise de dados
        ### Sites de dados das estações meteorológicas
        - Página da [IFSC](https://www.wunderground.com/dashboard/pws/IPALHO4)
        """
    )


if __name__ == "__main__":
    run()
