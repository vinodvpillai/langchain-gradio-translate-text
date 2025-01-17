import gradio as gr
from translate.file_reader import read_file
from translate.translator import translate_text

def translate_interface(text, file, language):
    if file:
        content, error = read_file(file)
        if error:
            return error
        text = content
        
    if text.strip() == "": # type: ignore
        return "Error: No text provided for translation."
    
    translated_text, error = translate_text(text, language)
    if error:
        return error
    
    return translated_text

def launch_interface():
    iface = gr.Interface(
        fn=translate_interface,
        inputs=[
            gr.Textbox(lines=2, placeholder="Enter text here..."),
            gr.File(label="Upload a (.txt or .pdf or .docx) file"),
            gr.Dropdown(
                label="Select language",
                choices=["Spanish", "French", "German", "Chinese", "Japanese"]
            )
        ],
        outputs=gr.Textbox(label="Translated text"),
        title="Language Translator",
        description="Translate text or documents to the language of your choice using OpenAI's LLM."
    )

    iface.launch()
