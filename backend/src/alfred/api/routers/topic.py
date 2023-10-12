# Importing necessary modules from FastAPI and SQLAlchemy
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/healthcheck")
async def healthcheck():
    return {"status": "healthy"}
