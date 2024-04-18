from fastapi import APIRouter, HTTPException, Depends, status, Path, Query, Security, BackgroundTasks, Request
from fastapi.security import OAuth2PasswordRequestForm, HTTPAuthorizationCredentials, HTTPBearer
from send_email import send_email
from sqlalchemy.orm import Session


import auth_services
import schemas
import users
from db import get_db


router = APIRouter(prefix='/auth', tags=['auth'])
get_refresh_token = HTTPBearer()


@router.post("/signup/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def signup(body: schemas.UserSchema, bt: BackgroundTasks, db: Session = Depends(get_db)):
    if users.get_user_by_email(body.email, db):
        print(1)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists",

        )

    body.password = auth_services.Auth.get_password_hash(body.password)
    db_user = users.create_user(body, db)
    bt.add_task(send_email, db_user.email, db_user.username, str(request.base_url))
    return db_user



@router.post("/login/", response_model=schemas.TokenSchema)
def login(body: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = users.get_user_by_email(body.username, db)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    if not db_user.confirmed:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email not confirmed",
        )
    if not auth_services.Auth.verify_password(body.password, db_user.password):

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    access_token = auth_services.Auth.create_access_token(data={'sub': db_user.email})
    refresh_token = auth_services.Auth.create_refresh_token(data={'sub': db_user.email})
    users.update_token(db_user, refresh_token, db)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.get("/refresh_token/", response_model=schemas.TokenSchema)
def refresh_token(credentials: HTTPAuthorizationCredentials = Security(get_refresh_token),
                           db: Session = Depends(get_db)):
    token = credentials.credentials
    email = auth_services.Auth.decode_refresh_token()
    user = users.get_user_by_email(email, db)
    if user.refresh_token != token:
        users.update_token(user, None, db)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    access_token = auth_services.Auth.create_access_token(data={'sub': email})
    refresh_token = auth_services.Auth.create_refresh_token(data={'sub': email})
    users.update_token(user, refresh_token, db)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.get('/confirmed_email/{token}')
def confirmed_email(token: str, db: Session = Depends(get_db)):
    email = auth_services.Auth.get_email_from_token(token)
    user = users.get_user_by_email(email, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Verification error")
    if user.confirmed:
        return {"message": "Your email is already confirmed"}
    users.confirmed_email(email, db)
    return {"message": "Email confirmed"}