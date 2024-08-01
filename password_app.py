import time
import tkinter
from tkinter import messagebox

RETREIVED_REAL_PASSWORD = "1234"


def check_password(password):
    if len(password) != len(RETREIVED_REAL_PASSWORD):
        return False
    for x, y in zip(password, RETREIVED_REAL_PASSWORD):
        time.sleep(0.05)
        if int(x) != int(y):
            return False
    return True


window = tkinter.Tk()
window.title("Password Authentification")
window.geometry("640x440")
window.configure(bg="#333333")


def login():
    if check_password(password_entry.get()):
        messagebox.showinfo(
            title="Login Success", message="You entered the correct password."
        )
    else:
        messagebox.showerror(title="Error", message="Invalid password.")


frame = tkinter.Frame(bg="#333333")

# Creating widgets
login_label = tkinter.Label(
    frame, text="Please enter password", bg="#333333", fg="#FF3399", font=("Arial", 30)
)
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg="#333333", fg="#FFFFFF", font=("Arial", 16)
)
login_button = tkinter.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login
)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()
