from tkinter import *
import client_chat
import client_login_gui
from client_gui import *


BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class chat_application_create_account_page:

    def __init__(self,):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def close(self):
        self.window.destroy()

    def _setup_main_window(self):
        self.window.title("Secured Chat Authority (create account page)")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        user_name = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                          text='Enter your first name last name', font="Helvetica 20",).place(x=10, y=30)
        line1 = Label(self.window, bg=BG_GRAY).place(x=15, y=65, width=375, height=4)

        user_name = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                          text='user name and password:', font="Helvetica 20", ).place(x=10, y=80)
        line2 = Label(self.window, bg=BG_GRAY).place(x=15, y=115, width=305, height=4)

        first_name = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                          text='First name:', font="Helvetica 15").place(x=10, y=130)
        self.e_first_name = Entry(self.window, width=40)
        self.e_first_name.place(x=150, y=136)


        last_name = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                          text='Last name:', font="Helvetica 15").place(x=10, y=190)
        self.e_last_name = Entry(self.window, width=40)
        self.e_last_name.place(x=150, y=196)


        user_name = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text='User name:', font="Helvetica 15").place(x=10, y=250)
        self.e_user_name = Entry(self.window, width=40)
        self.e_user_name.place(x=150, y=256)


        password = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                          text='Password:', font="Helvetica 15").place(x=10, y=310)
        self.e_password = Entry(self.window, width=40)
        self.e_password.place(x=150, y=316)

        login_b = Button(self.window, text='Submit', font="Helvetica 35 bold", command=lambda: self.create_account())
        login_b.place(x=150, y=400, width=200, height=70)

    def create_account(self):
        success = client_chat.create_account_func(self.e_first_name.get(), self.e_last_name.get(),
                                                  self.e_user_name.get(), self.e_password.get())
        if success == '1':
            self.close()
            app_login = client_login_gui.chat_application_login_page()
            app_login.run()
        elif success == '2':
            self.e_first_name.delete(0, END)
            self.e_last_name.delete(0, END)
            self.e_user_name.delete(0, END)
            self.e_password.delete(0, END)
        else:
            self.close()
            app_login = client_login_gui.chat_application_login_page()
            app_login.run()




'''if __name__ == "__main__":
    app = chat_application_create_account_page()
    app.run()'''
