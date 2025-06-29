import tkinter as tk
from tkinter import filedialog
import os
os.chdir(os.path.dirname(__file__))
from tkinter import simpledialog


win= None
def show():
    global win
    win = tk.Tk()
    win.title("File Dialog")
    win.geometry('400x350')
    win.overrideredirect(True)
    centre(win)
    tk.Label(text='Please click Open File to select a custom level for students. \nYou can only select txt files. \nIn order to edit files click edit adn select your desired file.').pack(pady=30)
    tk.Button(win, text="Open File", bg='green', command=browse_file, width=28).pack(pady=20)
    tk.Button(text='edit', bg='orange', state='normal', command=edit_file, width= 30).pack(pady=20)
    tk.Button(text='Back', bg='red', state='normal', command=back, width= 30).pack(pady=20)
    

def browse_file():
    
    file_path=filedialog.askopenfilename(filetypes=[('Text files','*.txt')])
    if not file_path:
        return
    with open(file_path, 'r') as f:
        content=f.read()
    i=6
    while True:
        filename = f'lvl_{i}.txt'
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            break
        i+=1
    with open(f'lvl_{i}.txt','w') as l:
        l.write(content)
    tk.messagebox.showinfo('Success', f'Level {i} created.')
        
def back():
    global win
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


def edit_file():
    file_path = filedialog.askopenfilename(initialdir=".", filetypes=[("Text files", "lvl_*.txt")])
    if not file_path:
        return
    with open(file_path, 'r') as f:
        content = f.read()
    new_content = simpledialog.askstring("Edit Level", "Edit content:", initialvalue=content)
    if new_content is not None:
        with open(file_path, 'w') as f:
            f.write(new_content)
        import glob
        max_files = len(glob.glob('lvl_*.txt'))
        from TypeStackV2 import max_level
        max_level = max_files
        tk.messagebox.showinfo("Success", "Level updated.")
