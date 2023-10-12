# Import FastAPI
from fastapi import FastAPI

# Import the routers for prediction and predictions
from .routers import topic

# Create a new FastAPI instance
app = FastAPI()

# Include the router from prediction
# This connects the routes defined in the prediction module to the FastAPI app
app.include_router(topic.router)
