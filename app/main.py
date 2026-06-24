from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {
        "project": "devops-demo",
        "version": "1.0",
        "time": str(datetime.now())
    }

@app.get("/health")
def health():
    return {"status": "healthy"}