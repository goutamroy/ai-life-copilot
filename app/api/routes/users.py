from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.security import decode_access_token

from app.models.user import User

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/token"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    payload = decode_access_token(token)

    if not payload:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user_id = payload.get(
        "user_id"
    )

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.get("/me")
def get_me(
    current_user: User = Depends(
        get_current_user
    )
):

    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }

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

@router.get("/test")
def test():
    return {
        "message": "Protected route file loaded"
    }