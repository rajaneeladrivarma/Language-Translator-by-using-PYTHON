from tkinter import *
import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator
from tkinter import messagebox, filedialog

root = tk.Tk()
root.title('Language Translator')
root.geometry('590x400')
root.configure(bg='#A9D6E5')

frame1 = Frame(root, width=590, height=400, relief=RIDGE, borderwidth=5, bg='#A9D6E5')
frame1.place(x=0, y=0)

Label(root, text="Language Translator", font=("Helvetica 20 bold"), fg="black", bg='#A9D6E5').pack(pady=10)

history = []

def translate():
    lang_1 = text_entry1.get("1.0", "end-1c").strip()
    src_lang = source_language.get().lower()
    tgt_lang = target_language.get().lower()
    if lang_1 == '':
        messagebox.showerror('Language Translator', 'Enter the text to translate!')
        return
    if src_lang == 'auto detect':
        src_lang = 'auto'
    try:
        output = GoogleTranslator(source=src_lang, target=tgt_lang).translate(lang_1)
        text_entry2.delete(1.0, 'end')
        text_entry2.insert('end', output)
        history.append((lang_1, src_lang, tgt_lang, output))
    except Exception as e:
        messagebox.showerror('Language Translator', f"Error: {e}")

def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')

def switch_text():
    source_text = text_entry1.get("1.0", "end-1c")
    target_text = text_entry2.get("1.0", "end-1c")
    src_lang = source_language.get()
    tgt_lang = target_language.get()
    text_entry1.delete(1.0, 'end')
    text_entry1.insert('end', target_text)
    text_entry2.delete(1.0, 'end')
    text_entry2.insert('end', source_text)
    source_language.set(tgt_lang)
    target_language.set(src_lang)

def save_translation():
    translated_text = text_entry2.get("1.0", "end-1c").strip()
    if not translated_text:
        messagebox.showerror('Save Translation', 'No text available to save!')
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(translated_text)
        messagebox.showinfo('Save Translation', 'Translation saved successfully!')

def copy_to_clipboard():
    translated_text = text_entry2.get("1.0", "end-1c").strip()
    if not translated_text:
        messagebox.showerror('Copy to Clipboard', 'No text available to copy!')
        return
    root.clipboard_clear()
    root.clipboard_append(translated_text)
    messagebox.showinfo('Copy to Clipboard', 'Translation copied to clipboard!')

def view_history():
    if not history:
        messagebox.showinfo("History", "No translations in history yet!")
        return
    history_window = Toplevel(root)
    history_window.title("Translation History")
    history_window.geometry("500x400")
    history_window.configure(bg='#A9D6E5')
    Label(history_window, text="Translation History", font=("Helvetica 15 bold"), bg='#A9D6E5').pack(pady=10)
    history_list = Text(history_window, wrap=WORD, font=('verdana', 10), bg="white", fg="black")
    history_list.pack(expand=True, fill=BOTH, padx=10, pady=10)
    for idx, (src_text, src_lang, tgt_lang, translated_text) in enumerate(history, 1):
        history_list.insert(END, f"{idx}. {src_lang.upper()} → {tgt_lang.upper()}\n")
        history_list.insert(END, f"   Original: {src_text}\n")
        history_list.insert(END, f"   Translation: {translated_text}\n\n")

def exit_app():
    root.destroy()

languages = [
    "english", "telugu", "hindi", "bengali", "marathi", "tamil", "urdu", "gujarati", "kannada",
    "malayalam", "punjabi", "assamese", "oriya", "spanish", "french", "german", "italian", "chinese",
    "japanese", "korean", "russian", "portuguese", "arabic", "turkish", "vietnamese", "thai", "dutch",
    "swedish", "greek", "polish", "czech", "danish", "finnish", "hebrew", "norwegian", "hungarian",
    "indonesian", "malay", "swahili", "zulu"
]

source_language = ttk.Combobox(frame1, width=27, state='readonly', font=('verdana', 10, 'bold'))
source_language['values'] = ["Auto Detect"] + languages
source_language.place(x=15, y=60)
source_language.current(0)

target_language = ttk.Combobox(frame1, width=27, state='readonly', font=('verdana', 10, 'bold'))
target_language['values'] = languages
target_language.place(x=305, y=60)
target_language.current(0)

text_entry1 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry1.place(x=10, y=100)

text_entry2 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry2.place(x=300, y=100)

btn1 = Button(frame1, command=translate, text="Translate", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#0077B6', fg="white", cursor="hand2")
btn1.place(x=80, y=300)

btn2 = Button(frame1, command=clear, text="Clear", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#0077B6', fg="white", cursor="hand2")
btn2.place(x=170, y=300)

btn3 = Button(frame1, command=switch_text, text="Switch", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#0077B6', fg="white", cursor="hand2")
btn3.place(x=260, y=300)

btn4 = Button(frame1, command=save_translation, text="Save", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#0077B6', fg="white", cursor="hand2")
btn4.place(x=350, y=300)

btn5 = Button(frame1, command=copy_to_clipboard, text="Copy", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#0077B6', fg="white", cursor="hand2")
btn5.place(x=440, y=300)

btn6 = Button(frame1, command=view_history, text="History", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#00A19D', fg="white", cursor="hand2")
btn6.place(x=80, y=350)

btn7 = Button(frame1, command=exit_app, text="Exit", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#D90429', fg="white", cursor="hand2")
btn7.place(x=515, y=300)

root.mainloop()
