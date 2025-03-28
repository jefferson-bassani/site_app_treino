from flask import Flask
import flet as ft
from main import main

server = Flask(__name__)

@server.route("/")
def serve_flet_app():
    return ft.app(target=main, view=ft.AppView.WEB_BROWSER)

app = server

if __name__ == "__main__":
    app.run()