# Importing necessary modules from FastAPI and SQLAlchemy
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Importing the Pydantic models we defined earlier
from alfred.schemas import IrisSpecies, PredictionSchema

# Importing the make_prediction function from the services module
from alfred.services.prediction import make_prediction

# Creating a new API router. This is a group of routes that can be included in the main application.
router = APIRouter()


# Defining a new route in the router.
# This route will handle POST requests to the "/predict/" URL.
# The response_model parameter tells FastAPI that the response should match the PredictionSchema model.
@router.post("/predict/", response_model=PredictionSchema)
def predict_species(
    iris: IrisSpecies,
):  # The function parameter is type-annotated with the IrisSpecies model.
    # FastAPI will automatically validate the request data against this model.
    # If the data is valid, it will be parsed into an instance of IrisSpecies and passed to the function.
    try:
        # The function calls the make_prediction service, passing the values from the request data.
        return make_prediction(
            sepal_length=iris.sepal_length,  # Using the request data to make a prediction
            sepal_width=iris.sepal_width,
            petal_length=iris.petal_length,
            petal_width=iris.petal_width,
        )
        # The result of the make_prediction function call is returned as the response.
        # FastAPI will automatically validate the response data against the PredictionSchema model.
        # If the data is valid, it will be serialized into JSON and sent as the response body.
    except ValueError as ve:
        # ValueError, e.g. in case of invalid input, return a 400 Bad Request status to the client with the error message.
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception:
        # If any other exception occurs, return a 500 Internal Server Error status.
        raise HTTPException(
            status_code=500,
            detail="An error occurred during prediction.",
            # detail should not expose sensitive information or any implementation details of your application.
        )
