# Importing necessary modules from FastAPI, SQLAlchemy, and typing
from typing import List

from fastapi import (
    APIRouter,  # a class from FastAPI that allows you to create groups of routes
)
from fastapi import Depends  # a function for declaring dependencies
from fastapi import HTTPException  # a class for raising HTTP exceptions
from sqlalchemy.orm import (  # a class from SQLAlchemy's ORM that manages persistence operations for ORM-mapped objects.
    Session,
)

# Importing the database session and engine from our database module
from alfred.database import (
    SessionLocal,  # a factory function for generating new SQLAlchemy Session objects (which represent database connections)
)
from alfred.database import (
    engine,  # the SQLAlchemy Engine object that provides a source of database connectivity and behavior
)

# Importing the database model and schema for the prediction
from alfred.models import (  # SQLAlchemy model is used to interface with the database
    DbPrediction,
)
from alfred.schemas import (  # Pydantic model is used to validate and serialize the data
    PredictionSchema,
)

# Creating a new API router
router = APIRouter()


# Declaring a dependency that gets a database session
def get_db():
    # Creating a new database session
    db = SessionLocal()
    try:
        # Yielding the session to be used by the dependencies
        yield db
    finally:
        # Closing the session after it has been used
        db.close()


# Defining a route that gets a list of predictions from the database
@router.get(
    "/predictions/", response_model=List[PredictionSchema]
)  # The route returns a list of predictions
def read_predictions(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):  # Default skip is 0 and limit is 100
    # Querying the database for predictions
    predictions = db.query(DbPrediction).offset(skip).limit(limit).all()
    # Returning the predictions
    return predictions


# Defining a route that gets a specific prediction from the database by its ID
@router.get("/predictions/{prediction_id}", response_model=PredictionSchema)
def read_prediction(prediction_id: int, db: Session = Depends(get_db)):
    # Querying the database for the prediction with the given ID
    prediction = db.query(DbPrediction).filter(DbPrediction.id == prediction_id).first()
    # If no prediction was found, raising a 404 error
    if prediction is None:
        raise HTTPException(status_code=404, detail="Prediction not found")
    # Returning the prediction
    return prediction
