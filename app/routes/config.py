from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil
import yaml

router = APIRouter()

@router.post("/config/rules", summary="Upload Rules YAML", description="Uploads and validates the transformation rules YAML file.")
async def upload_yaml_rules(file: UploadFile = File(...)):
    if not file.filename.endswith(".yaml") and not file.filename.endswith(".yml"):
        raise HTTPException(status_code=400, detail="Only YAML files are supported")

    os.makedirs("data", exist_ok=True)
    file_location = os.path.join("data", "rules.yaml")
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        with open(file_location, "r") as f:
            rules = yaml.safe_load(f)
        for rule in rules.get("output_rules", []):
            if not all(k in rule for k in ("outfield", "operation", "fields")):
                raise HTTPException(status_code=400, detail=f"Invalid rule format: {rule}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid YAML: {str(e)}")

    return {"message": "Transformation rules uploaded and validated successfully "}
