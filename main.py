from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/api/")
async def get_answer(request: QueryRequest):
    question = request.query

    # Dummy logic - replace this with real logic later
    answer = f"Answering: {question}"

    return JSONResponse(content={"answer": answer})
