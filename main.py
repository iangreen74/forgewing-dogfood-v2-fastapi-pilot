"""Minimal FastAPI pilot app for v2 pipeline testing."""
import os
from fastapi import FastAPI

app = FastAPI(title="Forgewing v2 Pilot")
PORT = int(os.environ.get("PORT", "8000"))
APP_NAME = os.environ.get("APP_NAME", "v2-pilot")

@app.get("/health")
def health():
    return {"status": "ok", "app": APP_NAME}

@app.get("/")
def root():
    return {"message": "Forgewing v2 pilot is running", "port": PORT}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
