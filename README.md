# NatWest Markets Python Backend Developer Assessment

This repository contains my completed submission for the Python Backend Developer Assessment provided by NatWest Markets.


## Objective
To develop a microservice in Python using FastAPI that:
- Accepts large input files
- Applies transformation rules (add, assign, max, multiply_max)
- Joins with a reference dataset
- Generates output in CSV, Excel (.xlsx), and JSON formats


## Technologies Used
- FastAPI: Web framework for building the API
- Pandas: Data processing and transformation
- YAML: Configuration of transformation logic
- Docker: Containerization for portability
- Uvicorn: ASGI server for running the FastAPI app
- Pytest: For unit testing
- Git & GitHub: Version control and repository hosting


## Project Structure
report_microservice/
├── app/
│   ├── main.py                - App entrypoint
│   ├── routes/                - All API endpoints
│   ├── services/              - Report logic
│   └── utils/                 - Logger setup
├── data/                     - Uploaded/generated files (input.csv, reference.csv, output.csv)
├── sample_data/              - Sample test files for interviewer
├── tests/                    - Unit test(s)
├── Dockerfile                - Docker build config
├── requirements.txt          - Dependencies
└── README.md                 - Project instructions


## Setup Instructions

Install dependencies:

pip install -r requirements.txt

Run FastAPI project:

uvicorn app.main:app --reload

Open in browser:
http://127.0.0.1:8000/docs - Swagger UI
http://127.0.0.1:8000/redoc - Redoc


## Docker Support
Build image:

docker build -t report-microservice .

Run container:

docker run -p 8000:8000 report-microservice


## Test Execution

pytest tests/


## Sample Test Files
Located inside the sample_data/ folder:
- input_large.csv
- reference_large.csv
- rules_large.yaml

Use these files to test large datasets via Swagger UI.


## API Endpoints
Method | URL | Description
-------|-----|------------
POST   | /upload/input     | Upload input CSV
POST   | /upload/reference | Upload reference CSV
POST   | /config/rules     | Upload transformation rules
POST   | /generate-report  | Generate output reports
GET    | /download-report  | Download final report CSV
GET    | /                 | App health check


## Summary of this project 
This project satisfies:
- All functional requirements from the assessment 
- Structured logging and exception handling
- Multi-format output (CSV, XLSX, JSON)
- Real-world scalability (tested up to 1000 rows)
- Code is modular, dockerized, and production-ready
