import os
from docx import Document
from PyPDF2 import PdfFileReader

def read_text_file(file):
    return file.read().decode("utf-8")

def read_docx_file(file):
    document = Document(file)
    return "\n".join([para.text for para in document.paragraphs])

def read_pdf_file(file):
    pdf_reader = PdfFileReader(file)
    text = []
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text.append(page.extract_text())
    return "\n".join(text)

def read_file(file):
    file_size = os.fstat(file.fileno()).st_size
    if file_size > 1 * 1024 * 1024:
        return None, "Error: File size exceeds 1 MB limit."
    
    file_name = file.name
    file_extension = os.path.splitext(file_name)[1].lower()
    
    try:
        if file_extension == ".txt":
            return read_text_file(file), None
        elif file_extension == ".docx":
            return read_docx_file(file), None
        elif file_extension == ".pdf":
            return read_pdf_file(file), None
        else:
            return None, "Error: Unsupported file format."
    except Exception as e:
        return None, f"Error reading file: {e}"
