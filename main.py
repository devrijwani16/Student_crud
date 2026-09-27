# pip install fastapi uvicorn pydantic
# uvicorn main:app --reload

#Remove-Item -Recurse -Force __pycache__

#git init then # git add .

# "Renamed main.py to student_crud.py" //  uvicorn student_crud:app --reload

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import studentRouter
from routers.studentRouter import studentRouter

app = FastAPI()
app.include_router(studentRouter)

# render try to run on https://student-curd.onrender.com 
@app.get("/")
def home():
    return RedirectResponse(url="/docs")

