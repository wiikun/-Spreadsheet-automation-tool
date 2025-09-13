from tkinter import *
from tkinter import ttk

class Window:
    def __init__(self,name):
        self.root = Tk()
        self.root.title("window")
        self.entry = {}
        self.button = {}
        return
    def view(self):
        self.root.mainloop()
        return
    def entryadd(self,key,row,column,textvariable):
        self.entry[key] = (Entry(self.root,textvariable=textvariable))
        self.entry[key].grid(row=row,column=column)
        return
    def buttonadd(self,key,row,column,text="",command=None):
        self.button[key] = (Button(self.root,text=text,command=command))
        self.button[key].grid(row=row,column=column)
        return
if __name__ == "__main__":
    wd = Window("test")
    wd.entryadd("1",1,1)
    wd.buttonadd("2",2,1,"test",lambda:print("test"))
    wd.view()