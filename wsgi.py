import flet as ft
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    def main(page: ft.Page):
        page.title = "Contador de Exercícios"
        page.update()
    
    return ft.app(target=main, view=ft.AppView.WEB_BROWSER)

@app.get("/assets/{path:path}")
async def serve_assets(path: str):
    return flet.app_assets(path)