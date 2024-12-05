import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a la base de datos SQL Server.
# en el apartado de .env tambien se debe de poner 
DATABASE_URL = (
    "mssql+pyodbc://@DESKTOP-JM0C7CR\SQLDEVELOPER/bd_Genpact?"
    "driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()
Base = declarative_base()

def getDatabase():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
