import tkinter as tk
import time
import random
import tkinter.messagebox as mb
import results
import os
import glob
os.chdir(os.path.dirname(__file__))

wpm_list=[]
accuracy_list=[]
time_list=[]
time_limit= 60
max_level=len(glob.glob('lvl_*.txt'))
total_chars = 0
correct_chars = 0
current_level=1
sentence_index=0
correct_count=0
total_typed=0
start_time=0
game_running=False
sentences=[]


def load_level(file, count=10):
    with open (file) as f:
        lines= [line.strip() for line in f.readlines()]
        return  random.sample(lines,min(count, len(lines)))
    
def show_sentence():
    global sentence_index
    if sentence_index < len(sentences):
        text_label.config(state='normal')
        text_label.delete(1.0,tk.END)
        text_label.insert(tk.END, sentences[sentence_index])
        text_label.config(state='disabled')
        input_entry.delete(0, tk.END)
        input_entry.focus()
    else:
        end_game()

def start_game():
    global sentence_index, correct_count, total_typed, game_running, start_time
    sentence_index=0
    correct_count=0
    total_typed=0
    game_running=True
    start_time=time.time()
    show_sentence()
    update_timer()

def load_level_start(level):
    global sentences, current_level
    current_level=level
    input_entry.config(state='normal')
    result_label.config(text='')
    next_level_btn.config(state='disabled')
    sentences.clear()
    file= f'lvl_{level}.txt'
    sentences.extend(load_level(file, 15))
    start_game()
    level_label.config(text=f'level {level}')
    if level == max_level:
        next_level_btn.config(text='Show Results', command=show_results, state='normal')
    else:
        next_level_btn.config(text='Next Level', command=next_level, state='disabled')

def show_results():
    root.destroy()
    results.show()
def check_input(event):
    global sentence_index, correct_count, total_typed
    if not game_running:
        return
    typed = input_entry.get().strip()
    if len(typed) == 0:
        mb.showwarning('Empty input', 'Please type at least one character.')
        input_entry.delete(0, tk.END)
        input_entry.focus()
        return
    typed_words = typed.split()
    target_words = sentences[sentence_index].split()

    correct_words = sum(1 for t, s in zip(typed_words, target_words) if t == s)
    total_words = max(len(target_words), len(typed_words))

    correct_count += correct_words
    total_typed += total_words
    sentence_index += 1
    show_sentence()





def update_timer():

    if not game_running:
        return
    remaining = time_limit - int(time.time() - start_time)
    timer_label.config(text=f'Time left: {remaining}s')
    if remaining <= 0:
        end_game()
    else:
        root.after(1000, update_timer)

def end_game():
    global game_running
    game_running = False
    total_time = time.time() - start_time
    accuracy = (correct_count / total_typed) * 100 if total_typed > 0 else 0
    wpm = (correct_count / 5) / (total_time / 60) if total_time > 0 else 0
    result_label.config(text=f'WPM: {wpm:.2f} | Accuracy: {accuracy:.1f}%')
    input_entry.config(state='disabled')

    wpm_list.append(wpm)
    accuracy_list.append(accuracy)
    time_list.append(total_time)

    if current_level < max_level:
        next_level_btn.config(state='normal')
    else:
        next_level_btn.config(text='Show Results', command=show_results, state='normal')



def next_level():
    load_level_start(current_level + 1)
    next_level_btn.config(state='disabled')


def show():
    global root, level_label, text_label, input_entry, timer_label, result_label, next_level_btn

    mb.showinfo('DISCLAIMER', 'Welcome to TypeStack! \nThis is a typing tutor game which contains 5 levels: \nLevel 1: Only Letters \nLevel 2: warm up with random letters. \nLevel 3: 15 randomly selected words from the Software Engineering modules such as object oriented programing and software automation. \nLevel 4: 5 short sentences related to the words from level 3. \nlevel 5: 3 Full paragraphs regarding the words in level 3. \n(Level 5 is extremely difficult to complete, so try your best.) \n once completed press next level. Once 5 levels are completed you will receieve a final accuracy mark and words per minute (WPM). \nWhen ready to begin press ok. Good luck! ')
    root= tk.Tk()
    root.title('TypeStack')
    root.geometry('800x500')
    root.overrideredirect(True)
    centre(root)
    level_label=tk.Label(root, text=f'level {current_level}', font=('Arial', 30))
    level_label.pack(pady=5)

    text_label = tk.Text(root, height=10, width=80, wrap='word')
    text_label.pack(pady=20)
    text_label.config(state='disabled')

    input_entry = tk.Entry(root, font=('Fira Code', 16), width=60)
    input_entry.pack()
    input_entry.bind('<Return>', check_input)

    timer_label = tk.Label(root, text='', font=('Fira Code',20))
    timer_label.pack(pady=15)

    result_label = tk.Label(root, text='', font=('Fira Code', 14))
    result_label.pack(pady=10)

    next_level_btn = tk.Button(root, text='Next Level', bg='light green', state='disabled', command=next_level, width=20)
    next_level_btn.pack(pady=10)
    tk.Button(text='Exit', bg='red', state='normal', width=20, command=back).pack()
    load_level_start(1)
    root.mainloop()



def back():
    root.destroy()
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
