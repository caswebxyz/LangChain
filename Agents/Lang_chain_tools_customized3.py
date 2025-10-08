import langchain
import langchain_core
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class MultiplyInput(BaseModel):
    a : int = Field(required=True,description="First Number to add")
    b : int = Field(required=True,description="Second Number to add")
    
def multiply_func(a: int, b:int) -> int:
    return a * b

class MultiplyTool(BaseTool):
    name : str = "multiply",
    description : str = "Multiply two numbers",
    arg_schema : Type[BaseModel] = MultiplyInput
    
    def _run(self, a:int,b:int) -> int:
        return a * b
mul = MultiplyTool()

res = mul.invoke({"a":11,"b":20})
print(res)