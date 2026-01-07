import tkinter as tk
from tkinter import ttk
import sqlite3

class HistoryPage(tk.Frame):
    def __init__(self, parent, controller, username):
        super().__init__(parent)
        self.controller = controller
        self.username = username

        tk.Label(self, text="🕓 Prediction History", font=("Helvetica", 16)).pack(pady=10)

        # Back button
        tk.Button(self, text="⬅ Back", command=self.go_back).pack(pady=5)

        # Treeview for displaying history
        self.tree = ttk.Treeview(self, columns=("Title", "Author", "Result", "Timestamp"), show="headings")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Result", text="Result")
        self.tree.heading("Timestamp", text="Timestamp")

        self.tree.column("Title", width=150)
        self.tree.column("Author", width=100)
        self.tree.column("Result", width=80)
        self.tree.column("Timestamp", width=150)

        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.load_history()

    def load_history(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title, author, result, timestamp 
            FROM history 
            WHERE username = ?
            ORDER BY timestamp DESC
        """, (self.username,))
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def go_back(self):
        from dashboard import DashboardPage
        self.destroy()
        dashboard = DashboardPage(self.controller.container, self.controller, self.username)
        dashboard.pack(fill="both", expand=True)
