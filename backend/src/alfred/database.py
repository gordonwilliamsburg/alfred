from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alfred.config import secrets
from alfred.models import Base

DATABASE_URL = secrets.database_url

# Creating an engine. The engine is the starting point for any SQLAlchemy application.
# It’s “home base” for the actual database and its DBAPI, delivered to the SQLAlchemy application
# through a connection pool and a Dialect, which describes how to talk to a specific kind of database/DBAPI combination.
engine = create_engine(DATABASE_URL)

# Creating a configured "Session" class.
# The sessionmaker function defines a Session class which will serve as a factory for new Session objects,
# and when called returns a new Session.
# The parameters like autocommit and autoflush are set to False, so you have more control over when the database is hit.
# Also, the sessionmaker is bound to the engine, so that it knows which database to communicate with.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Calling the create_all function on the metadata of the Base class.
# This will create all tables that don't exist yet according to the models defined in your SQLAlchemy classes.
# The bind parameter specifies the engine, which essentially tells SQLAlchemy where to create the tables.
Base.metadata.create_all(bind=engine)
