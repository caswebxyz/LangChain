import langchain
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

code = """
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_details(self):
        return self.name
    
    def is_passing(self):
        return self.grade >=6.0


# Example usage
student1 = Student("Shaanvi",12,9.5)
print(student1.get_details())

student2 = Student("Abhay",7,5.5)
print(student2.get_details())

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 300,
    chunk_overlap = 0
)
    
chunks = splitter.split_text(code)
print(len(chunks),"===",chunks)

print(chunks[0])
print("----------------------------------")
print(chunks[1])
