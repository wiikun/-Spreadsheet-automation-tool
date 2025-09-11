from tkinter import *
from tkinter import ttk
import modules.read
import modules.xlmake

index = 0

def write():
    global index
    modules.xlmake.write(list(modules.read.data[index].values())[0],entry_text.get())
    index += 1
    view()

def load():
    modules.read.load(entry_text.get())
    button.config(command=write)
    view()
    
def save():
    modules.xlmake.save()
    quit()
    
def view():
    global index
    entry_text.set('')
    if index >= len(modules.read.data):
        button.config(command=save)
        label.config(text="save")
        entry.destroy()
        root.mainloop()
        return
    if list(modules.read.data[index].keys())[0] == "name":
        index += 1
        view()
        return
    else:
        label.config(text=list(modules.read.data[index].keys())[0])
    root.mainloop()
        

root = Tk()
root.title('表入力自動化ツール')

label = ttk.Label(root,text="json")
label.grid(row=1,column=10)

entry_text = StringVar()
entry = ttk.Entry(root,textvariable=entry_text)
entry.grid(row=2,column=10)

button = ttk.Button(text="ok",command=load)
button.grid(row=3,column=10)

root.mainloop()