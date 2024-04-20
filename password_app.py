import time
import tkinter
from tkinter import messagebox

RETREIVED_REAL_PASSWORD = "1234"
            
def check_password(password): 
    
    if len(password) != len(RETREIVED_REAL_PASSWORD):
        return False
    for x, y in zip(password, RETREIVED_REAL_PASSWORD):
        time.sleep(0.1) # Simulates the wait time of a safe's mechanism
        if int(x) != int(y):
            return False
    return True

window = tkinter.Tk()
window.title("Password Authentification")
window.geometry("640x440")
window.configure(bg="#333333")

def login():

    if check_password(password_entry.get()):
        messagebox.showinfo(title="Login Success", message="You entered the correct password.")
    else:
        messagebox.showerror(title="Error", message="Invalid password.")

frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Please enter password", bg='#333333', fg="#FF3399", font=("Arial", 30))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()
#import time
#import numpy as np
#
#real_password = "2687"
## not display import
#def check_password(password): # Don't change it
#    if len(password) != len(real_password):
#        return False
#    for x, y in zip(password, real_password):
#        #time.sleep(0.1) # Simulates the wait time of the safe's mechanism
#        if int(x) != int(y):
#            return False
#    return True
#
#def crack_password():
#    pw_candidate = ["0", "0", ]
#    #check_time = 0.12
#    for position_dig in range(len(pw_candidate)):
#        for dig in np.arange(0, 10, dtype=int).tolist():
#            pw_candidate[position_dig] = str(dig)
#            start = time.time()
#            check_password("".join(pw_candidate))
#            time_taken = time.time() - start
#            print(time_taken)
#            print(pw_candidate)
#    return None
#
##crack_password()
#
#def is_authorized(token):
#    if token == real_password:
#        return True
#    else:
#        return False
#
##pw_list = ["2687", "1000", "2000","3000","4000","5000","6000","7000","8000","9000"]#["2689", "2678", "2587", "1687", "9894", "2687" "2687"]
##for pw_candidate in pw_list:
##    import time
##    start = time.time()
##    print(is_authorized(pw_candidate))
##    time_taken = time.time() - start
##    print(time_taken)
##    print(pw_candidate)
#
#
#def sum_digits3(n):
#   r = 0
#   while n:
#       r, n = r + n % 10, n // 10
#   return r
#print(sum_digits3(int(real_password)))
#