import docx2txt
import pdfplumber
import re

class Extracao:

    def limpeza_Espacamento(self, texto):
        new_texto = texto
        if(re.search(r'(\n{2,})', texto)):
            new_texto = re.sub(r'(\n{2,})', ' ', texto)
        else:
            new_texto = texto

        return new_texto
    
    def limpeza_Html(self, texto):
        if(re.search(r'<[^>]+?>', texto)):
            new_texto = re.sub(r'<[^>]+?>', '', texto)
        else:
            new_texto = texto
            
        return new_texto

    def limpeza_Geral(self, texto):
        new_texto = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', texto)
        return new_texto
        

    def combo_Limpeza(self, texto):
        texto_Sespaco = Extracao.limpeza_Espacamento(texto)
        texto_Shtml = Extracao.limpeza_Html(texto_Sespaco)
        texto_Normalizado = Extracao.limpeza_Espacamento(texto_Shtml)
        return texto_Normalizado

    def limpeza_Html(self, texto):
        if(re.search(r'<[^>]+?>', texto)):
            new_texto = re.sub(r'<[^>]+?>', '', texto)
        return new_texto


    def ExtracaoDOC(self, arquivo):
        return docx2txt.process(arquivo)

    def ExtracaoPDF(self, arquivo):
        path_doc = pdfplumber.open(arquivo)
        text_Inpath = ''
        for page in path_doc.pages:
            text_Inpath = text_Inpath + page.extract_text()
            text_Inpath= text_Inpath + ' '
        return text_Inpath
     