import tkinter as tk
from login import LoginPage

class FakeNewsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fake News Detection System")
        self.geometry("900x600")
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.show_login()

    def show_login(self):
        login_page = LoginPage(self.container, self)
        login_page.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = FakeNewsApp()
    app.mainloop()
