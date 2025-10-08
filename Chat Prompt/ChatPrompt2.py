import langchain
from langchain_openai import OpenAI, ChatOpenAI
from langchain.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

system_prompt = SystemMessagePromptTemplate.from_template("You are Coding Tutor who explains programming concepts to beginners using simple language with real world examples")
human_prompt = HumanMessagePromptTemplate.from_template("Can you explain what is {topic} in {langauge}")

# template1 =  ChatPromptTemplate.from_messages([
#     SystemMessage(content="You are Coding Tutor who explains programming concepts to beginners using simple language with real world examples"),
#     HumanMessage(content="Can you explain what is {topic} in {langauge}")
    
# ])

template1 = ChatPromptTemplate(
    [system_prompt,human_prompt]
)

prompt=template1.format_messages(
    topic="dictionary",
    langauge="python",
   # tone="beginner-friendly"
)

model = ChatOpenAI(model="gpt-4")

res = model.invoke(prompt)

print(res.content)