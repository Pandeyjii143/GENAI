from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model=ChatOpenAI(model='gpt-4',temperature=1)
result=model.invoke("suggest me 5 indian boys names")
print(result.content)