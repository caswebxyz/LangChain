from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
import os
load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=token,)
    
chat_model = ChatHuggingFace(llm=llm)

message = HumanMessage(content=" What is Capital of India")

response = chat_model.invoke([message])
print(response.content)







