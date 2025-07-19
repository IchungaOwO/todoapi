from fastapi import FastAPI
from routes import task
from routes import user
from routes import tag
app = FastAPI()
app.include_router(task.router)
app.include_router(user.router)
app.include_router(tag.router)