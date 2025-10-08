import langchain
import langchain_core
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a : int = Field(required=True,description="First Number to add")
    b : int = Field(required=True,description="Second Number to add")
    
def multiply_func(a: int, b:int) -> int:
    return a * b

multiply_tool=StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="multiply two numbers",
    args_schema = MultiplyInput
)

res = multiply_tool.invoke({"a":10,"b":20})
print(res)