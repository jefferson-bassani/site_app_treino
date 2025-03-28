import flet as ft
from main import main

async def create_app():
    return await ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        web_renderer="html",
        use_color_emoji=True,
        route_url_strategy="hash",
    )

app = create_app()