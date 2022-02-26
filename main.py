from fastapi import FastAPI
from pydantic import BaseModel

# ? Define the Model
class Course(BaseModel):
    id: int
    name: str
    price: float 
    is_early_bird: bool | None = None

# ! It's a fake DB Created in List, but it's not a real DB. All Data 
# ! is stored in Secondary Memory and is lost once the Application is Closed.

fakedb = []

app = FastAPI()

@app.get("/")
async def read_root():
    return {"messege": "Welcome to NeedNation.com"}


@app.get("/courses")
async def get_courses():
    return fakedb

@app.get("/courses/{course_id}")
async def get_course_detail(course_id: int):
    course = course_id - 1
    return fakedb[course]

@app.post("/courses/")
async def add_course(course: Course):
    fakedb.append(course.dict())
    return fakedb[-1]

@app.delete("/courses/{course_id}")
async def delete_course(course_id: int):
    fakedb.pop(course_id - 1)
    return {"task": "deletion Successful !"}
    

