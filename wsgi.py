import flet as ft
from main import main

def create_app():
    return ft.app(target=main, view=ft.AppView.WEB_BROWSER)

app = create_app()