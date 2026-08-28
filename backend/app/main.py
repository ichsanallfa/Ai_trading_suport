from fastapi import FastAPI

app = FastAPI(
    title="AI IDX Scalper",
    description="AI Trading Backend",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "status": "online",
        "message": "AI IDX Scalper Backend"
    }