import langchain
from langchain_openai import OpenAI,ChatOpenAI
from langchain.chains import LLMMathChain
from dotenv import load_dotenv
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import tool,Tool
from langchain import hub
from langchain_community.tools import TavilySearchResults, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

load_dotenv()


#tools = [add,sub,multiply,divide]

llm=ChatOpenAI(model="gpt-4o-mini")
prompt = hub.pull("hwchase17/react")
#

#prompt = hub.pull("hwchase17/openai-functions-agent", include_model=True)


tool_math = LLMMathChain.from_llm(llm = llm)

wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

calc = Tool(
    name="Calculator",
    func = tool_math.run,
    description="useful for Answering Math"
)

#create an Agent
agent = create_react_agent(
    llm=llm,
    tools=[calc,wiki],
    prompt=prompt
)
# create an Agent Executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[calc,wiki],
    verbose=True
)


# res = agent_executor.invoke({"input": "if a laptop costs 65,434 ruppes with 18% gst included calculate the original price of the laptop"})
res = agent_executor.invoke({"input": "if a laptop costs 65,434 ruppes with 18% gst included calculate the original price of 12% the laptop, exclude 12% discount in the original price"})


# Output
print("Result 1:", res)
# print("Result 2:", res1)
# print("Result 3:", res2)
    

