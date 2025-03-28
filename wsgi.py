from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import flet as ft
from main import main

app = FastAPI()

# Adiciona middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
@app.head("/")  # Adiciona suporte ao método HEAD
async def home(request: Request):
    try:
        page = ft.Page(
            title="Contador de Exercícios",
            theme_mode=ft.ThemeMode.LIGHT
        )
        await main(page)
        return page.render()
    except Exception as e:
        return HTMLResponse(content=f"<h1>Erro ao carregar: {str(e)}</h1>", status_code=500)