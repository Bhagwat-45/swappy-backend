from fastapi import FastAPI
from app.core.database import Base,engine
from app.models import ProfileTable,AssignmentTable

app = FastAPI(title="Swappy Backend", version="0.1.0")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return{
        "Welcome to Swappy Backend!"
    }

@app.get("/health")
def get_health():
    return {
        "message" : "okay"
    }


