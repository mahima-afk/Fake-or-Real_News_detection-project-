from PIL import Image, ImageTk
from analytics import AnalyticsPage
import tkinter as tk
from tkinter import messagebox
from predictor import predict_news  # your ML function
from history import HistoryPage     # your history viewer

class DashboardPage(tk.Frame):
    def __init__(self, parent, controller, username):
        super().__init__(parent)
        self.controller = controller
        self.username = username

        tk.Label(self, text=f"Welcome, {username}!", font=("Helvetica", 16)).pack(pady=10)

        # Load and set background image
        bg_img = Image.open("dashboard_bg.jpg")
        bg_img = bg_img.resize((900, 600))  # Adjust size to your window
        self.bg_photo = ImageTk.PhotoImage(bg_img)

        bg_label = tk.Label(self, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        content_frame = tk.Frame(self, bg="#001f3f")
        content_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Then place labels/entries/buttons inside this frame
        tk.Label(content_frame, text="Title", bg="#001f3f", fg="white").pack()

        # Input fields
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Title").grid(row=0, column=0)
        self.title_entry = tk.Entry(form_frame, width=50)
        self.title_entry.grid(row=0, column=1, pady=5)

        tk.Label(form_frame, text="Author").grid(row=1, column=0)
        self.author_entry = tk.Entry(form_frame, width=50)
        self.author_entry.grid(row=1, column=1, pady=5)

        tk.Label(form_frame, text="News Text").grid(row=2, column=0)
        self.news_entry = tk.Text(form_frame, width=50, height=10)
        self.news_entry.grid(row=2, column=1, pady=5)

        # Buttons in a separate frame (using grid only)
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Predict", command=self.predict).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="View History", command=self.view_history).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="User Analytics", command=self.show_analytics).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Logout", command=self.logout).grid(row=0, column=3, padx=5)

        # Result display
        self.result_label = tk.Label(self, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

    def predict(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        text = self.news_entry.get("1.0", tk.END).strip()

        if not title or not author or not text:
            messagebox.showwarning("Input Error", "Please fill in all fields!")
            return

        result = predict_news(title, author, text)
        self.result_label.config(text=f"Prediction: {result}")

    def view_history(self):
        self.destroy()
        history = HistoryPage(self.controller.container, self.controller, self.username)
        history.pack(fill="both", expand=True)

    def show_analytics(self):
       self.destroy()
       analytics = AnalyticsPage(self.controller.container, self.controller, self.username)
       analytics.pack(fill="both", expand=True)

    def logout(self):
       self.destroy()  # ✅ This is correct — inside a function
       from login import LoginPage
       login = LoginPage(self.controller.container, self.controller)
       login.pack(fill="both", expand=True)
