from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import select
from app.database import SessionDep
from app.models import *
from app.models.user import *
from app.auth import *
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import status
from . import templates

app_router = APIRouter()

@app_router.get("/app", response_class=HTMLResponse)
async def app(
    request: Request,
    user: AuthDep,
    db:SessionDep
):
    return templates.TemplateResponse(
        request=request, 
        name="app.html",
        context={
            "user": user
        }
    )

    
@app_router.get("/users", response_class=HTMLResponse)
async def users(
    request: Request,
    user: AuthDep,
    db:SessionDep
):
    users = db.exec(select(User)).all()

    return templates.TemplateResponse(
        request=request, 
        name="users.html",
        context={
            "user": user,
            "all_users": users
        }
    )