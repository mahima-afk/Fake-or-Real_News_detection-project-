import tkinter as tk
import sqlite3

class AnalyticsPage(tk.Frame):
    def __init__(self, parent, controller, username):
        super().__init__(parent)
        self.controller = controller
        self.username = username

        tk.Label(self, text=f"{username}'s Analytics", font=("Helvetica", 16)).pack(pady=10)

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM history WHERE username=?", (username,))
        total = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM history WHERE username=? AND result='FAKE'", (username,))
        fake = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM history WHERE username=? AND result='REAL'", (username,))
        real = cursor.fetchone()[0]

        conn.close()

        tk.Label(self, text=f"Total Predictions: {total}").pack()
        tk.Label(self, text=f"Fake News: {fake}").pack()
        tk.Label(self, text=f"Real News: {real}").pack()

        tk.Button(self, text="⬅ Back", command=self.go_back).pack(pady=10)

    def go_back(self):
        from dashboard import DashboardPage
        self.destroy()
        dashboard = DashboardPage(self.controller.container, self.controller, self.username)
        dashboard.pack(fill="both", expand=True)
