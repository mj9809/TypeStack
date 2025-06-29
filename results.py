import tkinter as tk
import TypeStackV2 
import os
os.chdir(os.path.dirname(__file__))


def show():
    global win
    win=tk.Tk()
    win.title('Results')
    win.geometry('400x200')
    win.overrideredirect(True)
    centre(win)
    wpm= TypeStackV2.wpm_list
    accuracy= TypeStackV2.accuracy_list
    time= TypeStackV2.time_list
    ave_wpm=round(sum(wpm)/len(wpm))
    ave_accuracy=round(sum(accuracy)/len(accuracy))
    ave_time=round(sum(time)/len(time))
    tk.Label(text='Student results:').pack(pady=15)
    tk.Label(text= f'Averge time of completion: {ave_time} seconds').pack(pady=5)
    tk.Label(text= f'Averge accuracy: {ave_accuracy}%').pack(pady=5)
    tk.Label(text= f'Averge words per minute: {ave_wpm}').pack(pady=5)
    tk.Button(text='Exit', width=10, bg='red', state='normal', command=back).pack(pady=15)
    
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