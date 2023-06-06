from tkinter import Tk, Entry, Label

def Calc(event):
    try:
        result = str(eval(entry.get()))
        entry.delete(0, 'end')
        entry.insert(0, result)
    except:
        clear()

def clear(*event):
    entry.delete(0, 'end')

window = Tk()
window.title("Calculator test")

entry = Entry(master = window)
entry.focus_set()
entry.pack()

window.bind('<Return>', Calc)
window.bind('c', clear)

window.mainloop()
