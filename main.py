from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PatientInput(BaseModel):
    symptoms: list[str] | None = None
    lab: dict | None = None
    imaging: str | None = None

@app.post("/input")
async def receive_data(data: PatientInput):
    # FastAPI automatically parses JSON into PatientInput
    return {"status": "received", "data": data}
