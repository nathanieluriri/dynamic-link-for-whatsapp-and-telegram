import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from db import insert_url_document_for_whatsApp,get_url_document_for_whatsApp,get_url_document_for_telegram,insert_url_document_for_telegram
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/whatsApplink")
async def redirect1():
    # Redirect to the first URL
    sa= get_url_document_for_whatsApp()
    
    return RedirectResponse(url=f"{get_url_document_for_whatsApp()}")

@app.get("/Telegramlink")
async def redirect2():
    # Redirect to the second URL
    return RedirectResponse(url=f"{get_url_document_for_telegram}")


@app.get("/")
async def root():
      return {"message": f"Deployed Succesfully! for { os.getenv("APPTYPE")}"}

class UrlRequest(BaseModel):
    url: str


@app.post("/add/whatsApplink")
async def redirect2(data: UrlRequest):
    insert_url_document_for_whatsApp(url=data.url)  # Extract URL from request
    return {"message": "URL successfully added"}


@app.post("/add/Telegramlink")
async def redirect2(data: UrlRequest):
    insert_url_document_for_telegram(url=data.url)  # Extract URL from request
    return {"message": "URL successfully added"}