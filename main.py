import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated
from dotenv import load_dotenv

load_dotenv()
from db import insert_url_document_for_whatsApp, get_url_document_for_whatsApp, get_url_document_for_telegram, insert_url_document_for_telegram

app = FastAPI()
security = HTTPBasic()

# Dummy credentials

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Authentication dependency
def verify_credentials(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if credentials.username != USERNAME or credentials.password != PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Unprotected routes
@app.get("/whatsApplink",include_in_schema=False)
async def redirect_to_whatsApp():
    return RedirectResponse(url=f"{get_url_document_for_whatsApp()}")

@app.get("/Telegramlink",include_in_schema=False)
async def redirect_telegram():
    return RedirectResponse(url=f"{get_url_document_for_telegram()}")

@app.post("/whatsAppChannel",include_in_schema=False)
async def redirect_whatsApp_channel():
    return RedirectResponse(url=f"{get_url_document_for_whatsApp()}")

@app.get("/",include_in_schema=False)
async def root():
    return {"message": f"Deployed Succesfully! for {os.getenv('APPTYPE')}"}

# Request model
class UrlRequest(BaseModel):
    url: str

# Protected routes with authentication
@app.post("/add/whatsApplink")
async def add_or_change_whatsApp_link(
    data: UrlRequest,
    username: Annotated[str, Depends(verify_credentials)]
):
    insert_url_document_for_whatsApp(url=data.url)
    return {"message": "URL successfully added"}

@app.post("/add/Telegramlink")
async def add_or_change_telegram_links(
    data: UrlRequest,
    username: Annotated[str, Depends(verify_credentials)]
):
    insert_url_document_for_telegram(url=data.url)
    return {"message": "URL successfully added"}