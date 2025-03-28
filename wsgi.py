import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import flet as ft
from main import main

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    page = await ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        port=int(os.environ.get("PORT", 8000)),
        web_renderer="html"  # Added this line
    )
    return page