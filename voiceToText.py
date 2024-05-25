import tkinter as tk
import subprocess
import speech_recognition as sr

class SpeechToTextConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech to Text Converter")
        self.root.geometry("900x450")
        
        self.create_widgets()
        

    def create_widgets(self):
        # Top Frame
        top_frame = tk.Frame(self.root, bg="#28a745", width=900, height=100)
        top_frame.place(x=0, y=0)
        
        tk.Label(top_frame, text="Speech to Text", font="Arial 20 bold", bg="#28a745", fg="#FFFFFF").place(x=350, y=35)
        
        # Recognized Text Text Area
        self.recognized_text_area = tk.Text(self.root, font="Arial 15", bg="#FFFFFF", fg="#000000", relief=tk.GROOVE, wrap=tk.WORD)
        self.recognized_text_area.place(x=20, y=150, width=500, height=250)
        
        # Listen Button
        self.listen_button = tk.Button(self.root, text="Listen", command=self.start_conversion, font="Arial 14 bold", bg="#28a745", fg="#FFFFFF")
        self.listen_button.place(x=550, y=200, width=100)
        
        # Clear Button
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_text, font="Arial 14 bold", bg="#28a745", fg="#FFFFFF")
        self.clear_button.place(x=700, y=200, width=100)

        self.switch_button = tk.Button(self.root, text="Switch", width=10, bg="#39c790", font="arial 14 bold", command=self.switch_interface)
        self.switch_button.place(x=730, y=50)

    def start_conversion(self):
        recognizer = sr.Recognizer()
        
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            self.recognized_text_area.delete(1.0, tk.END)
            self.recognized_text_area.insert(tk.END, "Listening...")
            self.root.update()
            audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio)
            self.recognized_text_area.delete(1.0, tk.END)
            self.recognized_text_area.insert(tk.END, text)
        except sr.UnknownValueError:
            self.recognized_text_area.delete(1.0, tk.END)
            self.recognized_text_area.insert(tk.END, "Could not understand audio")
        except sr.RequestError as e:
            self.recognized_text_area.delete(1.0, tk.END)
            self.recognized_text_area.insert(tk.END, "Error fetching results; {0}".format(e))
            
    def clear_text(self):
        self.recognized_text_area.delete(1.0, tk.END)

    def switch_interface(self):
        # Hide the current window
        self.root.withdraw()

        # Launch the new window (TextToSpeech.py)
        subprocess.Popen(["python", "TextToSpeech.py"])

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechToTextConverter(root)
    root.mainloop()
