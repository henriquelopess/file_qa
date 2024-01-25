
import os
import io
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import datetime

class gravarArquivo:
     def gravar_arquivo_txt(uploaded_file):
        diretorio_destino = "files_pdf/"
                
        with pdfplumber.open(uploaded_file) as pdf:
            pdf_pages = pdf.pages

            texto_concatenado = ""

            for page in pdf_pages:
                texto_concatenado += page.extract_text()

        
        text_spliter = RecursiveCharacterTextSplitter(chunk_size = 1000,\
                                                      chunk_overlap = 200,\
                                                      length_function = len)
        


        data_upload = datetime.datetime.now()
        formato_data_hora = "%Y-%m-%d_%H-%M-%S"
        data_hora_formatada = data_upload.strftime(formato_data_hora)
        nome_arquivo = f"upload_file_{data_hora_formatada}.pkl"


        chunks = text_spliter.split_text(text=texto_concatenado)

        

        caminho_completo = os.path.join(diretorio_destino, nome_arquivo)
        
        if os.path.exists(caminho_completo):
            with open(caminho_completo, 'rb') as f:
                vectorstore = pickle.load(f)
        
        else:
            embeddings = OpenAIEmbeddings()
            vectorstore = FAISS.from_texts(chunks, embeddings=embeddings)

            with open(caminho_completo, "wb") as f:
                pickle.dump(vectorstore, f)


        #with open(caminho_completo, 'w', encoding='utf-8') as f:
        #    f.write(texto_concatenado)

        return texto_concatenado
        