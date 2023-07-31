from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Archivo para establecer la configuracion y conexion a la base de datos.

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://Rata:a@localhost/opencode"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, #connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()