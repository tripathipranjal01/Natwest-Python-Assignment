from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
from app.services.processor import generate_report

router = APIRouter()

@router.post("/generate-report", summary="Generate Report", description="Triggers the report generation using uploaded input, reference, and rules.")
def generate():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists("data/input.csv") or not os.path.exists("data/reference.csv") or not os.path.exists("data/rules.yaml"):
        raise HTTPException(status_code=400, detail="Missing input/reference/rules file(s)")

    try:
        message = generate_report()
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/download-report", summary="Download Report", description="Downloads the most recent generated CSV report.")
def download():
    output_file = "data/output.csv"
    if not os.path.exists(output_file):
        raise HTTPException(status_code=404, detail="Output file not found")

    return FileResponse(output_file, media_type='text/csv', filename="report.csv")

