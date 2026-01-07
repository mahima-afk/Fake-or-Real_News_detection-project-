import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Load and display background image
        bg_img = Image.open("news_background.jpg")  # Make sure this file exists
        bg_img = bg_img.resize((900, 600))
        self.bg_photo = ImageTk.PhotoImage(bg_img)
        bg_label = tk.Label(self, image=self.bg_photo)
        bg_label.place(relwidth=1, relheight=1)

        # Login frame (on top of background)
        login_frame = tk.Frame(self, bg="#001f3f")
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(login_frame, text="Login", bg="#001f3f", fg="white", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(login_frame, text="Username", bg="#001f3f", fg="white").pack()
        self.username_entry = tk.Entry(login_frame, bg="#001f3f", fg="white", insertbackground="white")
        self.username_entry.pack()

        tk.Label(login_frame, text="Password", bg="#001f3f", fg="white").pack()
        self.password_entry = tk.Entry(login_frame, show="*", bg="#001f3f", fg="white", insertbackground="white")
        self.password_entry.pack()

        tk.Button(login_frame, text="Login", command=self.login).pack(pady=5)
        tk.Button(login_frame, text="Register", command=self.register).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            messagebox.showinfo("Login Success", f"Welcome {username}!")
            from dashboard import DashboardPage
            self.destroy()
            dashboard = DashboardPage(self.controller.container, self.controller, username)
            dashboard.pack(fill="both", expand=True)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def register(self):
        messagebox.showinfo("Register Clicked", "Redirect to registration")
