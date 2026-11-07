from fastapi import FastAPI

from src.routes import endpoints, checks
from fastapi import FastAPI

# Register all models with SQLAlchemy metadata
from src.models.user import User
from src.models.endpoint import Endpoint
from src.models.check import Check

app = FastAPI(
    title="API Monitoring Tool",
    description="Monitor API availability and response times.",
    version="1.0.0"
)


app.include_router(endpoints.router)
app.include_router(checks.router)


@app.get("/")
def root():
    return {"message": "API Monitoring Tool is running!"}