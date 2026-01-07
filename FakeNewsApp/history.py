import tkinter as tk
import sqlite3

class HistoryPage(tk.Frame):
    def __init__(self, parent, controller, username):
        super().__init__(parent)
        self.controller = controller
        self.username = username

        tk.Label(self, text=f"{username}'s History", font=("Helvetica", 16)).pack(pady=10)

        self.text_box = tk.Text(self, width=80, height=20)
        self.text_box.pack(pady=10)

        self.load_history()

        tk.Button(self, text="⬅ Back", command=self.go_back).pack()

    def load_history(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT title, author, text, result, timestamp FROM history WHERE username=? ORDER BY timestamp DESC", (self.username,))
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            self.text_box.insert(tk.END, "No history found.")
        else:
            for row in rows:
                self.text_box.insert(tk.END, f"{row[4]}\nTitle: {row[0]}\nAuthor: {row[1]}\nText: {row[2]}\nResult: {row[3]}\n{'-'*50}\n")

    def go_back(self):
        from dashboard import DashboardPage
        self.destroy()
        dashboard = DashboardPage(self.controller.container, self.controller, self.username)
        dashboard.pack(fill="both", expand=True)
