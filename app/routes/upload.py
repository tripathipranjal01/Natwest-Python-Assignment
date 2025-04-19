from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil
import pandas as pd

router = APIRouter()
DATA_FOLDER = "data"

required_input_cols = [
    "field1", "field2", "field3", "field4", "field5", "refkey1", "refkey2"
]

required_reference_cols = [
    "refkey1", "refkey2", "refdata1", "refdata2", "refdata3", "refdata4"
]

async def save_and_validate(file: UploadFile, filename: str, expected_cols: list):
    if not (file.filename.endswith(".csv") or file.filename.endswith(".txt")):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")

    os.makedirs(DATA_FOLDER, exist_ok=True)
    file_path = os.path.join(DATA_FOLDER, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    read_success = False
    for encoding in ["utf-8-sig", "utf-8", "ISO-8859-1"]:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            read_success = True
            break
        except Exception:
            continue

    if not read_success:
        raise HTTPException(status_code=400, detail="Invalid CSV encoding. Try UTF-8 or UTF-8 BOM formats.")

    df.columns = [col.strip().lower() for col in df.columns]
    expected_lower = [col.lower() for col in expected_cols]

    missing = [col for col in expected_lower if col not in df.columns]
    if missing:
        raise HTTPException(
            status_code=400,
            detail=f"Missing required column(s): {', '.join(missing)}"
        )

    return {"message": f"{filename} uploaded and validated successfully "}

@router.post("/upload/input", summary="Upload Input CSV", description="Upload and validate input.csv with required columns.")
async def upload_input_csv(file: UploadFile = File(...)):
    return await save_and_validate(file, "input.csv", required_input_cols)

@router.post("/upload/reference", summary="Upload Reference CSV", description="Upload and validate reference.csv with required columns.")
async def upload_reference_csv(file: UploadFile = File(...)):
    return await save_and_validate(file, "reference.csv", required_reference_cols)

