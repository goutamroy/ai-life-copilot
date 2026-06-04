from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.auth import RegisterRequest
from app.schemas.auth import LoginRequest
from app.schemas.auth import TokenResponse

from app.services.auth_service import AuthService

from app.core.security import create_access_token

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    try:

        user = AuthService.register_user(
            db=db,
            name=request.name,
            email=request.email,
            password=request.password
        )

        return {
            "message": "User registered successfully",
            "user_id": user.id
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    user = AuthService.authenticate_user(
        db=db,
        email=request.email,
        password=request.password
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": user.email,
            "user_id": user.id
        }
    )

    return TokenResponse(
        access_token=token
    )

@router.post("/token")
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = AuthService.authenticate_user(
        db=db,
        email=form_data.username,
        password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": user.email,
            "user_id": user.id
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }