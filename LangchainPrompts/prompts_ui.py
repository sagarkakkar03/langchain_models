from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

MODEL = ChatOpenAI(model="gpt-5-mini")

USER_INPUT = st.text_input('Enter your prompt')

TEMPLATE = PromptTemplate(
    template="""Give the answer of the following prompt {USER_INPUT} in less than 3 lines."""
)

PROMPT = TEMPLATE.invoke({
    'USER_INPUT': USER_INPUT
})

st.title('Research Tool')

if st.button("Run"):
    RESULT = MODEL.invoke(PROMPT)
    st.write(RESULT.content)