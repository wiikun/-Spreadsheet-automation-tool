import window
import writer
from tkinter import *

def appd():
    wt.append(txt1.get(),txt2.get())
    txt1.set("")
    txt2.set("")
    wind.view()

def save():
    wt.save("output.json")
    quit()

wt = writer.Writer("output.xls")

wind = window.Window("テンプレート生成ツール")

txt1 = StringVar(wind.root)
txt2 = StringVar(wind.root)

wind.entryadd("e1",row=1,column=1,textvariable=txt1)
wind.entryadd("e2",row=1,column=2,textvariable=txt2)
wind.buttonadd("b1",row=2,column=1,text="append",command=appd)
wind.buttonadd("b2",row=2,column=2,text="save",command=save)
wind.view()