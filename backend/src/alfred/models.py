# Importing necessary data types and functions from SQLAlchemy
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Creating a base class from which our SQLAlchemy models will inherit
Base = declarative_base()


# Defining a new SQLAlchemy model class to represent our predictions table in the database
class DbPrediction(Base):  # type: ignore
    # Specifying the name of the table in the database
    __tablename__ = "predictions"

    # Creating columns in the table. Each attribute of this class represents a column in the table.
    id = Column(
        Integer, primary_key=True, index=True
    )  # An integer column that will serve as the primary key
    sepal_length = Column(Float, index=True)  # A float column to store the sepal length
    sepal_width = Column(Float, index=True)  # A float column to store the sepal width
    petal_length = Column(Float, index=True)  # A float column to store the petal length
    petal_width = Column(Float, index=True)  # A float column to store the petal width
    species = Column(
        String, index=True
    )  # A string column to store the species predicted
