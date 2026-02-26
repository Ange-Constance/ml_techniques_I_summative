from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Ezza QA API")

# Request body model
class Query(BaseModel):
    question: str

# Dummy function for generating responses
def ezza_generate(question: str) -> str:
    # You can replace this with your actual model logic later
    return f"Echo: {question}"

# POST endpoint
@app.post("/ask")
def ask_ezza(query: Query):
    response = ezza_generate(query.question)
    return {"response": response}

# Optional root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "Ezza QA API is running!"}