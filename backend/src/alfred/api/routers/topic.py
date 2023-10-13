# Importing necessary modules from FastAPI and SQLAlchemy
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/")
async def healthcheck():
    return {"status": "healthy"}
