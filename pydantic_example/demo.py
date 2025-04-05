from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    
    

newstudent = {"name": 12, "age": 20}
student=Student(name="John", age=30)
print(student)