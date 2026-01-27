from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

url = "https://job-boards.greenhouse.io/nutrafol/jobs/4651720005"

loader = WebBaseLoader(url)

docs = loader.load()

prompt = PromptTemplate(
    template="{question} from {text}",
    input_variables=["question", "text"]
)

model = ChatOpenAI()
chain = prompt| model

print(chain.invoke({"question": "What is the price", "text":docs[0].page_content}))