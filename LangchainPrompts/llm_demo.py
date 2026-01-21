from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-5-mini', temperature=0, max_completion_tokens=2000)

result = llm.invoke("Write a poem?")

print(result)