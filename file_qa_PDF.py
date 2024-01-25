import PyPDF2

class fileQaPDF:
    
    def extrair_texto_pdf(arquivo_pdf):
        with open(arquivo_pdf,'rb') as file:
            leitor_pdf = PyPDF2.PdfReader(file)

        texto = ""
        for pagina in range(len(leitor_pdf.pages)):
        obj_pagina = leitor_pdf.pages[pagina]
        texto += obj_pagina.extract_text()

        return texto