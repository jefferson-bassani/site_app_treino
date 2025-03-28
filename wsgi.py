from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
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

@app.get("/", response_class=HTMLResponse)
@app.head("/")
async def home(request: Request):
    try:
        return await ft.app(
            target=main,
            view=ft.AppView.WEB_BROWSER,
            assets_dir="assets"
        )
    except Exception as e:
        return HTMLResponse(content=f"<h1>Erro ao carregar: {str(e)}</h1>", status_code=500)