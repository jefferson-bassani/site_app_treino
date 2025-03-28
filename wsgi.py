import flet
from flet import Page, app
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from main import main

app = FastAPI()

@app.get("/")
async def root():
    try:
        page = Page()
        await main(page)
        return HTMLResponse(page.render())
    except Exception as e:
        return HTMLResponse(f"<h1>Error: {str(e)}</h1>")

@app.get("/assets/{path:path}")
async def serve_assets(path: str):
    return flet.app_assets(path)