import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
import subprocess


root = Tk()
root.title("Text To Speech")
root.geometry("900x450")
root.resizable(False, False)
root.configure(bg='#FFD700')

engine = pyttsx3.init()

def switch_interface():
    # Close the current Tkinter window
    root.destroy()
    # Run the voice_to_text.py file
    subprocess.call(["python", "voiceToText.py"])

def speaknow():
    text= text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if(gender =="Male"):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if(text):
        if(speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif(speed=="Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

def download():
    text= text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if(gender =="Male"):
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if(text):
        if(speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif(speed=="Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

def switch_gender():
    current_gender = gender_combobox.get()
    if current_gender == "Male":
        gender_combobox.set("Female")
    else:
        gender_combobox.set("Male")

# Top Frame
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame .place(x=0, y=0)


Label (Top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg="black").place(x=350, y=35)

text_area = Text(root, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=20, y=150, width=500, height=250)

Label(root, text="VOICE", font="arial 15 bold", bg='#FFD700', fg="purple").place(x=580, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg='#FFD700', fg="purple").place(x=750, y=160)

gender_combobox= Combobox(root, values=['Male', 'Female'], font='arial 14', state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox= Combobox(root, values=['Fast', 'Normal','Slow'], font='arial 14', state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

btn= Button(root, text="Speak", width=10, bg="#39c790", font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280)

save= Button(root, text="Save", width=10, bg="#39c790" ,font="arial 14 bold", command=download)
save.place(x=720, y=280)


#switch button
switch_button = tk.Button(root, text="Switch", width=10, bg="#39c790", font="arial 14 bold", command=switch_interface)
switch_button.place(x=730, y=50)


root.mainloop()
