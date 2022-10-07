from dotenv import load_dotenv
from fastapi import FastAPI
import motor.motor_asyncio
import os
from routers.reconcile import router as reconcile_router

load_dotenv()

# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ['MONGODB_URL'])


app = FastAPI()
app.include_router(reconcile_router)

@app.get('/')
async def index():
    return {
        'message': 'Message'
    }               