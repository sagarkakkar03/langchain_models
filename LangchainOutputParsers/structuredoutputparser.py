from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

# model = ChatHuggingFace(llm = llm)
model = ChatOpenAI(
    model="gpt-5"
)

class Person(BaseModel):
    name: str = Field(description="Fictional Person's name")
    age: int
    city: str = Field(description="Fictioinal person's city")


parser = PydanticOutputParser(pydantic_object=Person)


template1 = PromptTemplate(
    template='Give me the female name, age and {city} of a fictional person \n {format_instructions}',
    input_variables=['city'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

template2 = PromptTemplate(
    template="Create a story about this person"
)

to_template2_input = RunnableLambda(
    lambda p: {
        "person_json": p.model_dump_json()
    }
)


chain = template1 | model | parser | to_template2_input | template2 | model
# result = chain.invoke({'city':'chandigarh'})
print(chain.invoke({"city": "Chandigarh"}))