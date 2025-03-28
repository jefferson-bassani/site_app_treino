from flask import Flask
import flet as ft
from main import main

app = Flask(__name__)

@app.route("/")
def home():
    return ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        port=8000
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)