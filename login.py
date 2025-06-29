import tkinter as tk
import student_login
import teacher_login
import os
os.chdir(os.path.dirname(__file__))

def open_student():
    root.destroy()
    student_login.show()

def open_teacher():
    root.destroy()
    teacher_login.show()




def centre(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x}+{y}')

root=tk.Tk()
root.overrideredirect(True)
root.title('Login Page')
root.geometry('400x250')
centre(root)
tk.Label(root, text='Are you a:', ).pack(pady=20)
tk.Button(root, text='Student', command=open_student, bg='green', width=15).place( x=50, y=120)
tk.Button(root, text='Teacher', command=open_teacher, bg='orange', width=15).place( x=230, y=120)
tk.Button(text='Exit', bg='red', state='normal', command=exit, width=40).place(x=54,y=200)
root.mainloop()

