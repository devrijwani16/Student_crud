# pip install fastapi uvicorn pydantic
# uvicorn main:app --reload

#Remove-Item -Recurse -Force __pycache__

from fastapi import FastAPI
from routers import studentRouter
from routers.studentRouter import studentRouter

app = FastAPI()
app.include_router(studentRouter)

