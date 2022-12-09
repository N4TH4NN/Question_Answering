
import streamlit as st
import streamlit.components.v1 as com
import Architecture
import FunctionWidgets

#Criando o Escopo da pagina
arquiterura = Architecture.ArchitecturePage()
arquiterura.scope()


#Criando um objeto da classe Estilizacao
estilo = FunctionWidgets.IG()


com.html(
'''
<html>
    <img src="https://i.picasion.com/pic92/ec38fbc4485444660f70ff9df37f0f35.gif" width="400" height="180" border="0"/>
</html>  

'''
)

estilo.addHeader('Stooody👻 - Um plataforma de Estudo')

estilo.addSubHeader('Utilizando I.A para criar uma plataforma de estudo e memorização de conteúdo')


st.markdown("***")

com.html(
'''
<html>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <div class="w3-container">
        <font color="#FFFFFF">
            <h1 class="w3-center w3-animate-left">Tutorial passo a passo 📋</h1><br>       
        </font>
    </div>
</html>  
'''
)

estilo.addText('''
1) Adicione um arquivo -PDF ou DOC - com material de Estudo ✔️
2) Faça uma pergunta sobre o material escolhido ✔️
3) ✨ Aguarde a resposta! ✨''')
st.markdown("***")

estilo.addText('Simples e fácil. Ideal para revisar conteúdo teórico 👌')


ir_para_pagina2 = estilo.button('Usar Plataforma')   
if ir_para_pagina2:
    estilo.switch_page('page2')







