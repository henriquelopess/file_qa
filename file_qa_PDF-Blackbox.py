import PyPDF2
from io import BytesIO
import requests
from urllib.parse import urlparse

def is_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def read_pdf_from_url(url):
    response = requests.get(url)
    pdf_file = BytesIO(response.content)
    return pdf_file

def get_pdf_text(file_path):
    pdf_file = open(file_path, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for page in range(read_pdf.numPages):
        text += read_pdf.getPage(page).extractText()
    pdf_file.close()
    return text

def extract_answer(text, question):
    # implement your logic to extract the answer
    # based on the position of the question in the text
    # this is a placeholder and may need adjustments based on your pdf structure
    index = text.find(question)
    if index != -1:
        answer = text[index:].split('\n')[1]
        return answer
    else:
        return None

def extract_info(file_path, questions):
    if is_url(file_path):
        pdf_file = read_pdf_from_url(file_path)
    else:
        pdf_file = file_path
    text = get_pdf_text(pdf_file)
    results = {}
    for question in questions:
        answer = extract_answer(text, question)
        results[question] = answer
    return results

questions = ["Pergunta 1", "Pergunta 2", "Pergunta 3"]
file_path = "caminho/para/seu/arquivo.pdf"
answers = extract_info(file_path, questions)
print(answers)