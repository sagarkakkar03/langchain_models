from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
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

loader = DirectoryLoader(
    path="LangchainDocuments/books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
# chain = prompt | model | StrOutputParser()

# print(chain.invoke({'text': docs[0].page_content}))