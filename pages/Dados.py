
# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestore-key.json")

# Create a reference to the Google post.
doc_ref = db.collection("stations").document("maciambu")

# Then get the data at that reference.
doc = doc_ref.get()


LOGGER = get_logger(__name__)

def run():


    st.write("#Bem Vindo ")

    st.sidebar.success("Selecione a Análise.")

    st.write("The id is: ", doc.id)
    st.write("The contents are: ", doc.to_dict())



if __name__ == "__main__":
    run()
