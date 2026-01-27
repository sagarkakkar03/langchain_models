from langchain_community.document_loaders import UnstructuredPDFLoader
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

loader = UnstructuredPDFLoader(
    "LangchainDocuments/provisional_degree.pdf",
)

docs = loader.load()

print(docs)
chain = prompt | model | StrOutputParser()

print(chain.invoke({'text': docs[0].page_content}))