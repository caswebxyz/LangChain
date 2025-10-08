import langchain
import langchain_core
from langchain_core.tools import tool


@tool
def multiply(a:int, b:int) -> int:
    """Multiply two numbers - tool"""
    return a * b

res = multiply.invoke({"a":10,"b":20})
print(res)

print(multiply.name)
print(multiply.description)
print(multiply.args)