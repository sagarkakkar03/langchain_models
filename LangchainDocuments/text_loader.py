from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="Write the topic of the given {text}",
    input_variables=["text"]
)

loader = TextLoader('LangchainDocuments/n8n.txt', encoding="utf-8")

docs = loader.load()

chain = prompt | model | StrOutputParser()

print(chain.invoke({'text': docs[0].page_content}))