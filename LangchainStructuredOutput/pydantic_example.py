from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):

    name: str = 'Sagar'
    age: Optional[int] = None 


new_student = {'age': '32a'}

student = Student(**new_student)

print(student.age)