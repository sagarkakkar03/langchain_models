from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
import os

load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
llm = HuggingFaceEndpoint(model="zai-org/GLM-4.7-Flash", huggingfacehub_api_token=HF_TOKEN)

model_openai = ChatOpenAI(model="gpt-5")
model_glm = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Create notes about the {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Create a quiz about the {topic}. Write 5 mcq questions.",
    input_variables=["topic"]
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n notes: {notes} and quiz: {quiz}",
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()

parallel_chain = (
    {
        'notes': prompt1 | model_openai | parser,
        'quiz': prompt2 | model_glm | parser
    }
)

merge_chain = prompt3 | model_openai | parser


chain = parallel_chain | merge_chain

result = chain.invoke({'topic': 'Langchain'})
print(result)