from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'sagar'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')


new_student = {'age':'32', 'email':'abc@gmail.com', 'new_field':'dfssd'}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])

print(type(student_dict['age']))
print(student_dict['name'])
# print(student_dict['new_field'])
print(type(student))

student_json = student.model_dump_json()