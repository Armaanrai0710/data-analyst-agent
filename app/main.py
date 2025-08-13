from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.agent import process_task

app = FastAPI()

@app.post("/api/")
async def analyze(
    questions: UploadFile = File(...),  # required questions.txt
    files: list[UploadFile] = File(default=[])  # optional extra files
):
    """
    Analyze endpoint:
    - 'questions' must be sent and will contain the questions.txt file.
    - 'files' may contain zero or more additional files.
    - Supports concurrent requests automatically (FastAPI async).
    """
    try:
        response = await process_task(questions, files)
        return JSONResponse(content=response)
    except Exception as e:
        # Log the error for debugging during college tests
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )

