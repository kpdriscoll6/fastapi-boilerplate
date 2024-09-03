from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

# Set the environment, defaulting to "development" if not specified
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # Specify allowed origins for CORS production frontend url and local frontend url
    allow_origins=["https://render-react-boilerplate.onrender.com", "http://localhost:3000"],
    #allow_origins=["*"],  # Allows all origins (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}

@app.get("/items")
async def get_items():
    return {"items": ["Item 1", "Item 2", "Item 3"]}