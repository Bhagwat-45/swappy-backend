from fastapi import FastAPI

app = FastAPI(title="Swappy Backend", version="0.1.0")


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
