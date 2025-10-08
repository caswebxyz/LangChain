import langchain
import langchain_core
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import ShellTool
from dotenv import load_dotenv
load_dotenv()
search_tool = DuckDuckGoSearchResults()
results = search_tool.invoke("India Cricket team selected for Asia cup")
print(results)

search_tool1 = TavilySearchResults()
res = search_tool1.invoke("Number of states in India")
print(res)

shell_tool = ShellTool()
shell_results = shell_tool.invoke("ls")
print(shell_results)
shell_results = shell_tool.invoke("dir")
print(shell_results)

