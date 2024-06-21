import os
from docx import Document
from PyPDF2 import PdfFileReader
from langchain_community.document_loaders import PyPDFLoader,Docx2txtLoader,TextLoader
from docx import Document as DocxDocument
import pypandoc
from io import BytesIO

def read_text_file(file):
    loader = TextLoader(file.name)
    documents = loader.load()
    return " ".join(doc.page_content for doc in documents)

def read_docx_file(file):
    loader = Docx2txtLoader(file.name)
    documents = loader.load()
    return " ".join(doc.page_content for doc in documents)

def read_pdf_file(file):
    loader = PyPDFLoader(file.name)
    documents = loader.load()
    return " ".join(doc.page_content for doc in documents)

def read_file(file):
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
