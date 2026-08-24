from fastapi import FastAPI
from assignment import router

app = FastAPI()

app.include_router(router)