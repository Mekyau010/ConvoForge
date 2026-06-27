from fastapi import FastAPI

from bot import BotEngine
from schemas import MessageRequest

app = FastAPI(
    title="ConvoForge",
    version="0.1.0"
)

bot = BotEngine()


@app.get("/")
def home():
    return {
        "project": "ConvoForge",
        "status": "Running"
    }


@app.post("/message")
def message(data: MessageRequest):
    return bot.process_message(
        platform=data.platform,
        user_id=data.user_id,
        message=data.message
    )
