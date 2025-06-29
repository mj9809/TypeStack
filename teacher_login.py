import tkinter as tk
import tkinter.messagebox as mb
import TypeStackV2
import teacher_page
import os
os.chdir(os.path.dirname(__file__))

def show():
    global username, password,win
    win = tk.Tk()
    win.title('Teacher Login')
    win.geometry('300x250')
    win.overrideredirect(True)
    centre(win)
    tk.Label(win, text='Teacher Login Page').pack(pady=10)
    tk.Label(win, text='Username:').pack()
    username=tk.Entry(win)
    username.pack(pady=5)
    tk.Label(win, text='Password:').pack()
    password= tk.Entry(win, show='*')
    password.pack()
    tk.Button(text='Submit', state='normal', command= login, bg='light green').pack(pady=20)
    tk.Button(text='Back', bg='red', state='normal', command=back).pack()
    win.mainloop()


def login():
    global win,username,password
    userval= username.get()
    passval= password.get()
    if userval== 'admin' and passval== '1234':
        mb.showinfo('Success', 'Welcome admin!')
        win.destroy()
        teacher_page.show()
    else: 
        mb.showerror('Error', 'Invalid username or password')
        

def back():
    win.destroy()
    os.system('python login.py')

def centre(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x}+{y}')
