from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.auth import router as auth_router
from app.api.routes.users import router as users_router
from app.api.routes.chat import router as chat_router

app = FastAPI(
    title="AI Life Copilot",
    version="1.0.0"
)

app.include_router(
    health_router
)

app.include_router(
    auth_router
)

app.include_router(
    users_router
)

app.include_router(
    chat_router
)


@app.on_event("startup")
def startup():
    print(
        "AI Life Copilot Backend Started"
    )


@app.get("/")
def root():
    return {
        "message": "AI Life Copilot Backend Running"
    }