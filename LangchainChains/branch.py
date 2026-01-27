from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableBranch, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

openai_model = ChatOpenAI(
    model="gpt-5"
)

prompt = PromptTemplate(
    template="Write a summary about the given {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | openai_model | parser

prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}",
    input_variables=["text"]
)

def is_long_text(text: str) -> bool:
    return len(text.split()) > 300

chain2 = RunnableBranch(
    (is_long_text, prompt2 | openai_model | parser),
    RunnablePassthrough()
)
chain3 = chain | chain2

print(chain3.invoke({'topic': 'n8n'}))