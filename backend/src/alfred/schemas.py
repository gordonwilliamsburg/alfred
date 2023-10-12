# Importing the Pydantic BaseModel class, which we will inherit from to create our own models
from pydantic import BaseModel


# Defining a Pydantic model to represent an iris species, on which to perform prediction.
# This model can be used for data validation, serialization, and documentation.
class IrisSpecies(BaseModel):
    # Each attribute in a Pydantic model represents a field in the schema
    # The type annotation defines what type the data should be
    sepal_length: float  # A field for sepal length
    sepal_width: float  # A field for sepal width
    petal_length: float  # A field for petal length
    petal_width: float  # A field for petal width


# Defining another Pydantic model for the prediction schema
# We inherit from IrisSpecies to include the fields from that model
class PredictionSchema(IrisSpecies):
    # Adding more fields specific to this schema
    id: int  # A field for the prediction id
    species: str  # A field for the predicted species

    # Defining configuration settings for this model
    class Config:
        # Enabling ORM mode so that the model can read data from SQLAlchemy models
        orm_mode = True
