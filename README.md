# Data Analyst Agent

This FastAPI app accepts analysis tasks via POST, performs scraping/EDA/plotting, and returns structured answers.

## Endpoint

POST /api/

Supports `questions.txt` (required) and other files (optional).