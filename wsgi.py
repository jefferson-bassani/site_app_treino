import os
from flask import Flask, Response
import flet as ft
from main import main

app = Flask(__name__)

@app.route('/')
def home():
    return Response(ft.app(target=main, view=ft.AppView.WEB_BROWSER))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)