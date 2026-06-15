from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.auth import router as auth_router
from app.api.routes.users import router as users_router
from app.api.routes.chat import router as chat_router
from app.api.routes.documents import router as documents_router
from app.api.routes.rag import router as rag_router

from app.core.database import Base, engine

# Import all models
import app.models

app = FastAPI(
    title="AI Life Copilot",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(chat_router)
app.include_router(documents_router)
app.include_router(rag_router)


@app.on_event("startup")
def startup():

    Base.metadata.create_all(bind=engine)

    print("AI Life Copilot Backend Started")


@app.get("/")
def root():
    return {
        "message": "AI Life Copilot Backend Running"
    }