@app.get("/")
def home():
    return {
        "project": "ConvoForge",
        "version": "0.1.0",
        "status": "Running",
        "supported_platforms": [
            "WhatsApp",
            "Telegram",
            "Discord"
        ]
    }
