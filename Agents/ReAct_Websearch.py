import langchain
from langchain_openai import OpenAI,ChatOpenAI
from dotenv import load_dotenv
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import tool
from langchain import hub
from langchain_community.tools import TavilySearchResults

load_dotenv()
search_tool = TavilySearchResults()
llm=ChatOpenAI()
prompt = hub.pull("hwchase17/react")
#create an Agent
agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)
# create an Agent Executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=False
    
)

prompt = hub.pull("hwchase17/react")
print(prompt)

#Create Agent
agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)
#create Agent Executor
