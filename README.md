# 📊 Report Generator Microservice

This is a backend microservice developed using **FastAPI** to fulfill the NatWest Markets Backend Developer Assessment. It allows users to upload structured CSV files and transformation rules in YAML format to generate a final report in CSV, Excel, and JSON formats.

---

## ✅ Features

- Upload `input.csv` and `reference.csv`
- Upload transformation logic via `rules.yaml`
- Merge and process data based on rules
- Output report in CSV, XLSX, and JSON formats
- Input validation and structured logging
- Docker support for easy deployment
- Swagger UI for API interaction
- Unit test for core functionality

---

## 📁 Project Structure

```
report_microservice/
├── app/
│   ├── main.py                  # FastAPI entrypoint
│   ├── routes/                  # API endpoint routers
│   │   ├── upload.py
│   │   ├── config.py
│   │   └── generate.py
│   ├── services/
│   │   └── processor.py         # Report generation logic
│   └── utils/
│       └── logger.py            # Logging config
├── data/                        # Uploaded files and output
├── tests/                       # Unit test
├── Dockerfile                   # Docker support
├── requirements.txt             # Dependencies
└── README.md                    # Project instructions
```

---

## 🛠️ Setup Instructions

### 🔧 Run Locally

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Start the FastAPI app:**
```bash
uvicorn app.main:app --reload
```

Open your browser at:
```
http://localhost:8000/docs  ← Swagger UI
http://localhost:8000/redoc ← Redoc (optional)
```

### 🐳 Run with Docker
```bash
docker build -t report-microservice .
docker run -p 8000:8000 report-microservice
```

---

## 🌐 API Endpoints

| Method | Endpoint            | Description                          |
|--------|---------------------|--------------------------------------|
| POST   | `/upload/input`     | Upload the input CSV file            |
| POST   | `/upload/reference` | Upload the reference CSV file        |
| POST   | `/config/rules`     | Upload YAML transformation rules     |
| POST   | `/generate-report`  | Process and generate the report      |
| GET    | `/download-report`  | Download the latest generated report |
| GET    | `/`                 | Health check endpoint                |

---

## 🧪 Run Unit Tests

```bash
pytest tests/
```

---

## 🔐 Validations

- Ensures required columns are present in uploaded CSVs
- YAML file is parsed and validated for necessary keys (`outfield`, `operation`, `fields`)
- Supports UTF-8, UTF-8 BOM, ISO encodings
- Logs every transformation step

---

## ✨ Tech Stack

- **FastAPI** – Web framework
- **Pandas** – Data transformation
- **YAML** – Rule configuration
- **Docker** – Containerization
- **Uvicorn** – ASGI server

---
