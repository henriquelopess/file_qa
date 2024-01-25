import streamlit as st
from gravar_arquivo import gravarArquivo

tab1, tab2 = st.tabs(["PDF", "YouTube"])
with st.sidebar:
    st.write("Informações de usuário")

with tab1:
    st.header("PDF")
    uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf", accept_multiple_files=False)
    try:
        if uploaded_file is not None:
            nome_arquivo = uploaded_file.name
            st.write("Carregando o arquivo", nome_arquivo)

            gravarArquivo.gravar_arquivo_txt(uploaded_file)

            st.success(f'Arquivo carregado com sucesso!')

    except:
        st.write("Não foi possivel ler o arquivo PDF")

with tab2:
    st.header("YouTube")
    st.write("Arquivo do YouTube")