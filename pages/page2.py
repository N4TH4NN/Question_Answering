import FunctionWidgets
import TextExtraction
import Model
import streamlit as st


estilo = FunctionWidgets.IG()
extract = TextExtraction.Extracao()
model = Model.QA_Model()

opcao = estilo.AddMenuOptions('Qual formato será utilizado: ', [
                              'Selecione Uma Opção', 'Formato PDF', 'Formato DOC', 'Adicionar Texto'])
with st.form('my_form'):
    # Criando a pagina
    if opcao == 'Formato PDF':
        arquivo = estilo.upload('Escolha um Arquivo PDF')
        pergunta = estilo.addTextArea(10, 'Pergunta sobre o Material:')
        botao = st.form_submit_button("Enviar Pergunta")
        if arquivo is not None:
            texto = extract.ExtracaoPDF(arquivo)
            texto_tratado = extract.limpeza_Espacamento(texto)
            estilo.addBreakLine()

        if botao:
            if pergunta != '':
                with st.spinner(text="Aguarde um pouco..."):
                    modelo = model.Model_Portuguese(texto_tratado, pergunta)
                st.subheader("Resposta:")
                st.markdown(modelo['answer'])
            else:
                st.error('Cuidado! está enviando sem preencher tudo', icon="🚨")

    elif opcao == 'Formato DOC':
        arquivo = estilo.upload('Escolha um Arquivo DOC')
        pergunta = estilo.addTextArea(10, 'Pergunta sobre o Material:')
        botao = st.form_submit_button("Submit")
        if arquivo is not None:
            texto = extract.ExtracaoDOC(arquivo)
            texto_tratado = extract.limpeza_Espacamento(texto)
            estilo.addBreakLine()

        if botao:
            if pergunta != '':
                with st.spinner(text="Aguarde um pouco..."):
                    modelo = model.Model_Portuguese(texto_tratado, pergunta)
                st.subheader("Resposta:")
                st.markdown(modelo['answer'])
            else:
                st.error('Cuidado! está enviando sem preencher tudo', icon="🚨")

    elif opcao == 'Adicionar Texto':
        material = estilo.addTextArea(300, '')
        pergunta = estilo.addTextArea(10, 'Pergunta sobre o Material:')
        botao = st.form_submit_button("Submit")

        if botao:
            if material != '' and pergunta != '':
                texto_tratado = extract.limpeza_Espacamento(material)
                with st.spinner(text="Aguarde um pouco..."):
                    modelo = model.Model_Portuguese(texto_tratado, pergunta)
                st.subheader("Resposta:")
                st.markdown(modelo['answer'])

            else:
                st.error('Cuidado! está enviando sem preencher tudo', icon="🚨")
