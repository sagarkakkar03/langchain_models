from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv


load_dotenv()

MODEL = ChatOpenAI()

MESSAGES = [
    SystemMessage(content='You are Astra an helpful AI agent.'),
] 
while True:
    USER_INPUT = input('Human:')
    if USER_INPUT == 'EXIT':
        break
    MESSAGES.append(HumanMessage(content=USER_INPUT))
    RESPONSE = MODEL.invoke(MESSAGES)
    MESSAGES.append(AIMessage(content=RESPONSE.content))
    print('AI:', RESPONSE.content)
print(MESSAGES)