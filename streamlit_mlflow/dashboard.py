import streamlit as st 

st.title("HIV Inhibitor Dashboard")
valid_molecule = True 
loaded_molecule = None
selection = None
submit = None 

#  -- sidebar
page = st.sidebar.selectbox('Page Navigation', ["Predictor", "Model analysis"])

st.sidebar.markdown("""---""")
st.sidebar.write("Created by Jinyoung Song")
st.sidebar.image("assets/peng.jpg", width=100)

if page == "Predictor":
    st.markdown("Select input molecule.")
    upload_columns = st.columns([2, 1])
    
    # File upload
    file_upload = upload_columns[0].expander(label="Upload a mol file")
    uploaded_file = file_upload.file_uploader("Choose a mol file", type=['mol'])
    
    # Smiles input
    smiles_select = upload_columns[0].expander(label="Specify SMILES string")
    smiles_string = smiles_select.text_input('Enter a valid SMILES string.')


    # If Both are selected, give the option to swap between them
    if uploaded_file and smiles_string:
        selection = upload_columns[1].radio("Select Input")