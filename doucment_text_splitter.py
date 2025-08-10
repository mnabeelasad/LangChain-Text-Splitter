from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """ 
# A simple function
def greet(name):
    return f"Hello, {name}!"

# First class: Person
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}."

# Second class: Student (inherits from Person)
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

"""


splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=200,
    chunk_overlap=20,
    language=Language.MARKDOWN
)

# Performing the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])