"""
ConvoForge
Build Once. Deploy Everywhere.
"""

from fastapi import FastAPI

app = FastAPI(
    title="ConvoForge",
    description="A modular messaging bot framework for WhatsApp, Telegram and Discord.",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "project": "ConvoForge",
        "status": "Running",
        "message": "Welcome to ConvoForge."
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }
