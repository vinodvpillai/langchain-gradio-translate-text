
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from util import constants

def translate_text(text, target_language):
    model = ChatOpenAI(base_url=constants.OPENAI_API_HOST, api_key=constants.OPENAI_API_KEY, model=constants.OPENAI_MODEL) # type: ignore
    # Translation
    system_template = "Translate the following into {language}:"
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )    
    parser = StrOutputParser()
    try:
        chain = prompt_template | model | parser
        translated_text = chain.invoke({"language": target_language, "text": text})
        return translated_text, None
    except Exception as e:
        return None, f"Error during translation: {e}"
