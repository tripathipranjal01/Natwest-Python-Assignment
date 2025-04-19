from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload
from app.routes import config
from app.routes import generate
import os


os.makedirs("data", exist_ok=True)

app = FastAPI(
    title="Report Generator Microservice",
    description="Built for NatWest Markets Assignment",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health Check"])
def root():
    return {
        "message": "Report Microservice is running!",
        "version": "1.0",
        "docs": "/docs",
        "upload_guide": "Upload input.csv, reference.csv, and rules.yaml, then generate report"
    }


app.include_router(upload.router, tags=["Upload CSVs"])
app.include_router(config.router, tags=["Config Rules"])
app.include_router(generate.router, tags=["Generate Report"])


