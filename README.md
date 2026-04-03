# Aviation Intelligence Platform

A full-stack flight delay prediction system built with Flask, scikit-learn, React, and SQLite.

## Project Structure

```
aviation-intelligence-platform/
├── backend/          # Flask API + ML model serving
├── frontend/         # React dashboard
└── data/
    ├── raw/          # Original CSV dataset
    ├── processed/    # Cleaned dataset + trained model
    ├── preprocessing.ipynb   # Data cleaning pipeline
    └── train_model.ipynb     # Model training pipeline
```

## Model

- Algorithm: Random Forest Classifier (scikit-learn Pipeline)
- Features: `airline`, `origin`, `destination`, `dep_hour`, `day_of_week`, `distance`
- Target: `DepDel15` — whether a flight is delayed 15+ minutes (1 = delayed, 0 = on time)
- ROC AUC: 0.66 | Accuracy: 0.59
- Dataset: January 2024 US domestic flights (~560k rows)

## Setup

### Prerequisites
- Python 3.13+
- Node.js 18+

### 1. Clone the repo
```bash
git clone https://github.com/hkonain27/aviation-intelligence-platform.git
cd aviation-intelligence-platform
```

### 2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install backend dependencies
```bash
pip install -r backend/requirements.txt
```

### 4. Install frontend dependencies
```bash
cd frontend && npm install
```

## Running the App

### Start the backend
```bash
cd backend
python app.py
```
Backend runs at `http://localhost:5001`

### Start the frontend
```bash
cd frontend
npm run dev
```
Frontend runs at `http://localhost:5173`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/predict` | Run a delay prediction |
| GET | `/predictions` | Get last 50 predictions |
| GET | `/api/dashboard-data` | Get dashboard chart data |

### POST `/predict` — Example request
```json
{
  "airline": "UA",
  "origin": "JFK",
  "destination": "LAX",
  "dep_hour": 17,
  "day_of_week": 5,
  "distance": 2475
}
```

### POST `/predict` — Example response
```json
{
  "status": "success",
  "prediction": 0,
  "prediction_label": "On Time Likely",
  "delay_probability": 0.2131
}
```

## Reproducing the Model

1. Run `data/preprocessing.ipynb` — generates `data/processed/flights_processed.csv`
2. Run `data/train_model.ipynb` — generates `data/processed/model.pkl`
