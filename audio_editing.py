import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import pygame
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import  *
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Simple Audio Editor")
root.geometry("400x300")
font = tkFont.Font(family = 'Times New Roman', size = 20, weight = 'bold' )
root.configure(bg = 'lightblue')
style = ttk.Style()
style.configure("Custom.TButton", foreground="pink", background="orange", relief=tk.FLAT)

audio = None  

pygame.mixer.init()

def load_audio():
    global audio
    
    file_path = filedialog.askopenfilename(title="Select an audio file", filetypes=[("Audio Files", "*.wav *.mp3 *.ogg")])
    try:
        audio = AudioSegment.from_file(file_path)
        label.config(text=f"Loaded: {file_path.split('/')[-1]}")
    except pygame.error as e:
            label.config(text=f"Error playing audio: {e}")
    if file_path:
        audio = AudioSegment.from_file(file_path)
        label.config(text=f"Loaded: {file_path.split('/')[-1]}", font = font, fg='pink')

def play_audio():
    if audio:
        temp_file = "temp_audio.wav"
        audio.export(temp_file, format="wav")

        try:
            pygame.mixer.music.load(temp_file)
            pygame.mixer.music.play()
        except pygame.error as e:
            label.config(text=f"Error playing audio: {e}")
            
def stop_audio():
    try:
        pygame.mixer.music.stop()  
    except pygame.error as e:
        label.config(text=f"Error stopping audio: {e}")

def trim_audio(start, end):
    if audio:
        trimmed_audio = audio[start * 1000:end * 1000] 
        trimmed_audio.export("trimmed_audio.wav", format="wav")
        label.config(text="Trimmed audio saved as 'trimmed_audio.wav'")

load_button = tk.Button(root, text="Load Audio", command=load_audio, font = font, fg = 'pink', highlightbackground="white", bd=0, relief=tk.FLAT)
load_button.pack(pady=10)

play_button = tk.Button(root, text="Play Audio", command=play_audio, font = font, fg = 'pink', bg = 'white', highlightbackground="white", bd = 0, height = 1)
play_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Audio", command=stop_audio, font = font, fg = 'pink', bg = 'white', highlightbackground="white", bd = 0) 
stop_button.pack(pady=10)

start_label = tk.Label(root, text="Start time (seconds):", font = font, fg = 'pink', bg = 'white', highlightbackground="white", bd = 0, height = 1 )
start_label.pack(pady=5)
start_entry = tk.Entry(root)
start_entry.pack(pady=5)

end_label = tk.Label(root, text="End time (seconds):", font = font, fg = 'pink', bg = 'white', highlightbackground="white", bd = 0, height = 1)
end_label.pack(pady=5)
end_entry = tk.Entry(root)
end_entry.pack(pady=5)

trim_button = tk.Button(root, text="Trim Audio", command=lambda: trim_audio(int(start_entry.get()), int(end_entry.get())),font = font, fg = 'pink', bg = 'white', highlightbackground="white", bd = 0, height = 1 )
trim_button.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=20)

root.mainloop()
