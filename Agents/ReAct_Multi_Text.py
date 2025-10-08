import langchain
from langchain_openai import OpenAI,ChatOpenAI
from dotenv import load_dotenv
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import tool
from langchain import hub
from langchain_community.tools import TavilySearchResults

load_dotenv()

@tool
def add(input: str) -> str:
    """Add two numbers Srinivas"""
    a, b = map(float, input.split(','))
    return str(a+b)

@tool
def sub(input: str) -> str:
    """Add two numbers Srinivas"""
    a, b = map(float, input.split(','))
    return str(a-b)

@tool
def multiply(input: str) -> str:
    """Add two numbers Srinivas"""
    a, b = map(int, input.split(','))
    return str(a*b)

@tool
def divide(input: int) -> str:
    """Add two numbers Srinivas"""
    a, b = map(float, input.split(','))
    return str(a/b)

tools = [add,sub,multiply,divide]

llm=ChatOpenAI(model="gpt-4o-mini")
prompt = hub.pull("hwchase17/react")
#create an Agent
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)
# create an Agent Executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)



res = agent_executor.invoke({"input": "multiply 12,4"})
res1 = agent_executor.invoke({"input": "add 7,8"})
res2 = agent_executor.invoke({"input": "product 7,8"})


# Output
print("Result 1:", res)
print("Result 2:", res1)
print("Result 3:", res2)
    

