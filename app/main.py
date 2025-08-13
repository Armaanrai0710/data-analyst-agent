from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.agent import process_task

app = FastAPI()

@app.post("/api/")
async def analyze(
    questions: UploadFile = File(...), 
    files: list[UploadFile] = File(default=[])
):
    response = await process_task(questions, files)
    return JSONResponse(content=response)
