from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()

@app.get('/')
async def index():
    return {
        'message': 'Message'
    }           