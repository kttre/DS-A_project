from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from ttkthemes import ThemedTk, ThemedStyle, THEMES
from main_functions import *
from tkinter import scrolledtext


def clear():
    text_enter.delete(0, END)
    hash_enter.delete(0, END)
    ans_txt.delete('1.0', END)


def hashing():
    text = text_enter.get()
    new_hash = make_hash(text)
    window.clipboard_clear()
    window.clipboard_append(new_hash)
    text_enter.delete(0, END)
    messagebox.showinfo("Шифрование", "Готовый шифр скопирован в буфер обмена!")


def dehashing():
    hash = hash_enter.get()
    hash_enter.delete(0, END)
    user_text = make_dehash(hash)
    ans_txt.delete('1.0', END)
    ans_txt.insert('1.0', user_text)


def keypress(event):
    if event.keycode == 86:
        event.widget.event_generate('<<Paste>>')
    elif event.keycode == 67:
        event.widget.event_generate('<<Copy>>')
    elif event.keycode == 88:
        event.widget.event_generate('<<Cut>>')


window = Tk()
window.title("Шифровальная машина")
window.geometry('500x550')
window.resizable(False, False)
style = ThemedStyle(window)
style.set_theme("scidpurple")

window.bind("<Control-KeyPress>", keypress)

menu = Menu(window)
operation = Menu(menu, tearoff=0)
operation.add_command(label='Очистить данные', command=clear)
menu.add_cascade(label='Операции', menu=operation)

main_lbl = Label(window, text="ШИФРОВАЛЬНАЯ МАШИНА", font=("Arial Bold", 18))
main_lbl.place(x=55, y=20)

hash_lbl = Label(window, text="Введите текст, который хотите зашифровать в поле ниже", font=("Arial Bold", 10))
hash_lbl.place(x=40, y=90)

text_enter = ttk.Entry(window, width=20)
text_enter.place(x=170, y=130)

hash_btn = ttk.Button(window, text="Зашифровать", width=19, command=hashing)
hash_btn.place(x=173, y=170)


dehash_lbl = Label(window, text="Если у вас есть шифр, введите его в поле ниже", font=("Arial Bold", 10))
dehash_lbl.place(x=70, y=240)

hash_enter = ttk.Entry(window, width=20)
hash_enter.place(x=170, y=280)

dehash_btn = ttk.Button(window, text="Расшифровать", width=19, command=dehashing)
dehash_btn.place(x=173, y=320)

ans_txt = scrolledtext.ScrolledText(window, width=30, height=7)
ans_txt.place(x=100, y=370)

window.config(menu=menu)
window.mainloop()


