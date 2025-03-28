import flet as ft
from fastapi import FastAPI
from main import main

app = FastAPI()

@app.get("/")
async def home():
    return ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        assets_dir="assets",
        web_renderer="html"
    )