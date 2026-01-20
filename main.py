from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TriageInput(BaseModel):
    symptoms: str
    vitals: str

@app.get("/")
def root():
    return {"status": "STeCS backend running"}

@app.post("/triage")
def triage(data: TriageInput):
    # Dummy logic for now
    if "unconscious" in data.symptoms.lower():
        return {
            "priority": "RED",
            "action": "Secure airway and call ambulance immediately"
        }

    return {
        "priority": "GREEN",
        "action": "Observe, provide oral fluids, reassess"
    }
