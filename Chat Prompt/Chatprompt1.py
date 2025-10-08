import langchain
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
template = ChatPromptTemplate.from_messages(
    [SystemMessage(content="You are Experienced career coach, provide practical and friendly advice in less than 50 words"),
     HumanMessage(content="My age is 42 working in {exist_tech} tech, i want to shift my career by only Learning {upcoming_tech}, how are the job openings will i get above 70 lakh package")
    ]
)

messages = template.format_messages(
    exist_tech = "Abinitio DWH",
    upcoming_tech="GenAI ( not learning Machine learning or Deep Learning)"
)

print(messages)

model = ChatOpenAI(model="gpt-4")
result = model.invoke(messages)
print(result)