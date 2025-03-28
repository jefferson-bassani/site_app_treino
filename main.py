import os
import flet as ft
from database import ExerciseDatabase
from datetime import datetime

class ExerciseTracker:
    def __init__(self):
        self.db = ExerciseDatabase()
        self.exercises = {
            "Flexão": {"count": 0, "icon": ft.icons.FITNESS_CENTER},
            "Biceps": {"count": 0, "icon": ft.icons.FRONT_HAND},  # Alterado para ícone de braço
            "Agachamento": {"count": 0, "icon": ft.icons.DIRECTIONS_WALK},
            "Abdominal": {"count": 0, "icon": ft.icons.ACCESSIBILITY_NEW},
        }

    def create_exercise_counter(self, name):
        return ft.Column(
            controls=[
                ft.IconButton(
                    icon=self.exercises[name]["icon"],
                    icon_size=30,
                    icon_color=ft.colors.BLUE,
                ),
                ft.TextField(
                    value=str(self.exercises[name]["count"]),
                    width=70,
                    text_align=ft.TextAlign.CENTER,
                    keyboard_type=ft.KeyboardType.NUMBER,
                    on_change=lambda e: self.update_count(e, name),
                ),
                ft.Text(
                    value=name,
                    size=12,
                    color=ft.colors.GREY_700,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5,
        )

    def save_to_history(self, e):
        self.db.save_exercise(self.exercises)
        e.page.update()

    def create_history_table(self):
        history_data = self.db.get_history()
        
        return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Data")),
                ft.DataColumn(ft.Text("Flexão")),
                ft.DataColumn(ft.Text("Biceps")),
                ft.DataColumn(ft.Text("Agachamento")),
                ft.DataColumn(ft.Text("Abdominal")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(row[0])),
                        ft.DataCell(ft.Text(str(row[1]))),
                        ft.DataCell(ft.Text(str(row[2]))),
                        ft.DataCell(ft.Text(str(row[3]))),
                        ft.DataCell(ft.Text(str(row[4]))),
                    ],
                ) for row in history_data
            ],
        )

    def update_count(self, e, name):
        try:
            new_value = int(e.control.value) if e.control.value else 0
            self.exercises[name]["count"] = new_value
            e.control.value = str(new_value)
        except ValueError:
            e.control.value = str(self.exercises[name]["count"])
        e.page.update()

    def increment_count(self, e, name):
        self.exercises[name]["count"] += 1
        e.control.parent.controls[1].value = str(self.exercises[name]["count"])
        e.page.update()

def main(page: ft.Page):
    page.title = "Contador de Exercícios"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE
    page.padding = 20

    tracker = ExerciseTracker()

    page.add(
        ft.Text("TODAY", size=16, color=ft.colors.GREY_700),
        ft.Row(
            controls=[
                tracker.create_exercise_counter(name)
                for name in tracker.exercises.keys()
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            spacing=30,
        ),
        ft.ElevatedButton(
            "Salvar exercícios do dia",
            on_click=tracker.save_to_history
        ),
        ft.Text("Histórico dos últimos 90 dias", size=16, color=ft.colors.GREY_700),
        tracker.create_history_table(),
    )

if __name__ == "__main__":
    ft.app(target=main)