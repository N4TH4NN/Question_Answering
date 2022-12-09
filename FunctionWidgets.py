import streamlit as st
import time

#Criando uma classe de criação da interface gráfica e elementos Graficos
class IG:

    #Funcao cria um Titulo 
    def addTitle(self, titulo):
        st.title(titulo)

    #Funcao cria um Header 
    def addHeader(self, text):
        st.header(text)

    #Funcao cria um SubHeader
    def addSubHeader(self, text):
        st.subheader(text)

    #Funcao adiciona um Texto
    def addText(self, text):
         st.text(text)

    #Funcao add text area
    def addTextArea(self, tamanho, msg):
        text = st.text_area(msg, height= tamanho)
        return text
      


    #Funcao cria um menu opcaoes 
    def AddMenuOptions(self,question, options):
        option = st.selectbox(
            question,
            (options))

        return option

    #Funcao de espera
    def wait(self,value):
        time.sleep(value)

    #Funcao adicionar para linha em branco    
    def addBreakLine(self):
        st.write('')

    #Funcao para fazer upload de arquivo
    def upload(self,text):
        data = st.file_uploader(text)
        return data

    #Funcao para criar um botao
    def button(self, texto):
        botao = st.button(texto)
        return botao
       

    #Funcao para mudar paginas(quando se tem mais que uma tela)
    def switch_page(self, page_name: str): #source: Blackary in "https://discuss.streamlit.io/t/navigate-multipage-app-with-buttons-instead-of-sidebar/27986/7"
        from streamlit.runtime.scriptrunner import RerunData, RerunException
        from streamlit.source_util import get_pages

        def standardize_name(name: str) -> str:
            return name.lower().replace("_", " ")

        page_name = standardize_name(page_name)

        pages = get_pages("streamlit_app.py")  # OR whatever your main page is called

        for page_hash, config in pages.items():
            if standardize_name(config["page_name"]) == page_name:
                raise RerunException(
                    RerunData(
                        page_script_hash=page_hash,
                        page_name=page_name,
                    )
                )

        page_names = [standardize_name(config["page_name"]) for config in pages.values()]

        raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")


    
    

