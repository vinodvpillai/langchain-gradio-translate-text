# Translation Application

## Overview
This application is designed to translate text and documents into various languages using the OpenAI LLM model. It supports multiple file formats for input and provides a user-friendly interface for translation tasks.

## Features
- Allows users to enter text directly.
- Allows users to upload files for translation (supports .txt, .docx, .pdf).
- Provides options for users to select the target language for translation.
- Displays the translated text in the interface.
- Ensures modular and maintainable code structure following industry standards.

## Project Structure
```
translator_app/
├── main.py
├── translate/
│   ├── __init__.py
│   ├── file_reader.py
│   ├── translator.py
├── interface/
│   ├── __init__.py
│   ├── gradio_interface.py
├── requirements.txt
```

### main.py
The entry point of the application, which launches the Gradio interface.

### translate/file_reader.py
Handles reading of different file types (.txt, .docx, .pdf).

### translate/translator.py
Handles text translation using the OpenAI LLM model.

### interface/gradio_interface.py
Sets up the Gradio interface for user interaction.

## Setup and Installation

### Prerequisites
- Python 3.11 or higher
- An OpenAI API key

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-username/langchain-gradio-translate-text.git
   cd langchain-gradio-translate-text
   ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key:
   - Open `langchain-gradio-translate-text.git/util/constants.py`.
   - Replace `'your-openai-api-key'` with your actual OpenAI API key:
     ```python
     openai.api_key = 'your-openai-api-key'
     ```

### Running the Application
Run the following command to start the application:
```
python main.py
```
This will launch the Gradio interface in your default web browser.

## Usage
1. **Add Document:**
   - Enter text directly into the provided textbox or upload a file (TXT, PDF, DOCX).
   - Select the target language for translation.
   - Click on the "Add Document" button to upload and translate the document.

2. **Ask Question:**
   - Enter your question in the provided textbox.
   - Click on the "Ask Question" button to get the translated answer based on the context of the uploaded documents.

3. **Clear Documents:**
   - Click on the "Clear Documents" button to clear all documents from the vector database.

## Dependencies
- `langchain`
- `gradio`
- `openai`
- `python-docx`
- `PyPDF2`
- `pandas`

## License
This project is licensed under the MIT License.

## Acknowledgements
- [OpenAI](https://openai.com) for the language model.
- [LangChain](https://python.langchain.com/v0.2/docs/tutorials/) for the prompt templates.
- [Gradio](https://www.gradio.app/) for the user interface.
