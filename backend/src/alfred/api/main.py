# Import FastAPI
from fastapi import FastAPI

# Import the routers for prediction and predictions
from .routers import prediction, predictions

# Create a new FastAPI instance
app = FastAPI()

# Include the router from prediction
# This connects the routes defined in the prediction module to the FastAPI app
app.include_router(prediction.router)

# Include the router from predictions
# This connects the routes defined in the predictions module to the FastAPI app
app.include_router(predictions.router)
