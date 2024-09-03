from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    #allow_origins=["http://localhost:3000", "http://localhost:5000","https://*.onrender.com"],
    allow_origins=["https://render-react-boilerplate.onrender.com", "http://localhost:3000"],
    #allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}

@app.get("/items")
async def get_items():
    return {"items": ["Item 1-Kevin", "Item 2", "Item 3"]}