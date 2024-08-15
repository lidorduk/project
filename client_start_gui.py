from tkinter import *
from client_chat import *
from client_login_gui import *
from client_create_account_gui import *
from client_gui import *

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class chat_application_start_page:

    def __init__(self,):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def close(self):
        self.window.destroy()

    def _setup_main_window(self):
        self.window.title("Secured Chat Authority (start page)")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text='Welcome', font="Helvetica 30 bold", pady=10)

        head_label.place(x=150, y=50)

        login_b = Button(self.window, text='Login', font=FONT_BOLD, command=lambda: self.login_b())
        login_b.place(x=470/2-140/2, y=180, width=140, height=70)
        create_account_b = Button(self.window, text='Create account', font=FONT_BOLD, command=lambda: self.create_account_b())
        create_account_b.place(x=470 / 2 - 140 / 2, y=300, width=140, height=70)

    def login_b(self):
        start_func('1')
        self.close()
        app_login = client_login_gui.chat_application_login_page()
        app_login.run()



    def create_account_b(self):
        start_func('2')
        self.close()
        app_create_account = chat_application_create_account_page()
        app_create_account.run()



if __name__ == "__main__":
    app = chat_application_start_page()
    app.run()
