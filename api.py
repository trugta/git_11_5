#Thư viện api
from fastapi import FastAPI, Path
#TV pydantic (nhập data/sửa)
from pydantic import BaseModel

from typing import Optional
#
app = FastAPI()
#Data khởi đầu
students={
    '1':{
        "Name":"Ta",
        "age":20
    },
    '2':{
        "Name":"Tam",
        "age":19
    },
    '3':{
        "Name":"BCD",
        "age":18
    }
}
#Post đẩy dữ liệu lên mt
class InputData(BaseModel):
        name: str
        age: int
#Put update
class UpdateData(BaseModel):
        name: Optional[str]=None
        age: Optional[int]=None
#Get
@app.get("/get_student/{student_ID}")
def get_student(student_ID:str ):
    return students[student_ID]
#Post
@app.post("/post_student/{student_ID}")
def post_student(student_ID:str, studentinput:InputData ):
    if student_ID in students:
        return {"Error":'student_ID existed'}
    students[student_ID]=studentinput
    return students[student_ID]
#Pust
@app.put("/put_student/{student_ID}")
def put_student(student_ID:int, students:UpdateData):
    if student_ID not in students:
        return {"Error":"student_ID not found"}
    students[student_ID]=students
    return students[student_ID]
    