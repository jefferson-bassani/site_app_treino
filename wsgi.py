import os
import flet as ft
from main import main

app = ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8000)))