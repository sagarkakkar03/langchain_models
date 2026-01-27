from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import (
    StrOutputParser, 
    PydanticOutputParser
    )
from langchain_core.runnables import (
    RunnableBranch,
    RunnableLambda
    )
from langchain_core.prompts import PromptTemplate
from typing import Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

class Feedback(BaseModel):
    sentiment: Literal['Positive', 'Negative'] = Field(description="Give sentiment of the sentence in positive or negative.")

parser = StrOutputParser()

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following {feedback} into positve or Negative. \n {format_instructions}",
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"]
)

classifier_chain =  prompt1 | model | parser2

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'Positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'Negative', prompt2 | model | parser),
    RunnableLambda(lambda x: "couldn't find sentiment")
)

chain = classifier_chain | branch_chain

# print(chain.invoke({'feedback': 'You are a wonderful person.'}))

chain.get_graph().print_ascii()