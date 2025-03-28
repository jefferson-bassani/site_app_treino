import sqlite3
from datetime import datetime

class ExerciseDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('exercises.db')
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercise_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            flexao INTEGER,
            biceps INTEGER,
            agachamento INTEGER,
            abdominal INTEGER
        )''')
        self.conn.commit()

    def save_exercise(self, exercises_dict):
        cursor = self.conn.cursor()
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        cursor.execute('''
        INSERT INTO exercise_history (date, flexao, biceps, agachamento, abdominal)
        VALUES (?, ?, ?, ?, ?)
        ''', (current_date, 
              exercises_dict["Flexão"]["count"],
              exercises_dict["Biceps"]["count"],
              exercises_dict["Agachamento"]["count"],
              exercises_dict["Abdominal"]["count"]))
        self.conn.commit()

    def get_history(self, days=90):
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT date, flexao, biceps, agachamento, abdominal 
        FROM exercise_history 
        ORDER BY date DESC 
        LIMIT ?
        ''', (days,))
        return cursor.fetchall()