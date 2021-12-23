from tkinter import *
import pyttsx3
from tkinter import filedialog
import PyPDF2
import os
root=Tk()
root.geometry("200x200")
def say(audio):
    engine=pyttsx3.init()
    #engine.say("hi Hrithik it's me ")
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    vrate=120
    engine.setProperty('rate',vrate)
    engine.say(audio)
    engine.runAndWait()
"""
def get_val():
    #e_text=entry.get()
    take_file()
"""
def take_file():
    filepath=filedialog.askopenfilename(filetypes=(
        ("PDF FILES","*.pdf"),
        ("ALL FILES","*.*")

    ))
    if filepath[len(filepath)-3]=="p":
        pdffile=PyPDF2.PdfFileReader(filepath)
        print(pdffile.numPages)
        for i in range(pdffile.numPages):
            page=pdffile.getPage(i)
            content=page.extractText()
            print(content)
            say(content)
    else:
        fp=open(filepath,'r')
        content=fp.read()
        say(content)
        fp.close()
   # Label(root,text=content).pack()
label=Label(root,text="open your file")
label.pack()
"""
entry=Entry(root)
entry.pack()"""
button1=Button(root,text="submit",command=take_file)
button1.pack()
root.mainloop()
