
import tkinter as tk
from tkinter import ttk, messagebox
import speech_recognition as sr
from googletrans import Translator
from googletrans import LANGUAGES

# Initialize the translator
translator = Translator()

# Function to perform voice recognition
def voice_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            label_status.config(text="Listening...")
            audio = recognizer.listen(source, timeout=5)
            label_status.config(text="Recognizing...")
            recognized_text = recognizer.recognize_google(audio)
            input_text.delete(1.0, tk.END)
            input_text.insert(tk.END, recognized_text)
            label_status.config(text="Speech recognized successfully!")
        except sr.UnknownValueError:
            label_status.config(text="Could not understand the audio.")
            messagebox.showerror("Error", "Could not understand the audio.")
        except sr.RequestError as e:
            label_status.config(text="Error with recognition service.")
            messagebox.showerror("Error", f"Recognition service error: {e}")
        except Exception as e:
            label_status.config(text="An error occurred.")
            messagebox.showerror("Error", str(e))

# Function to translate text
def translate_text():
    source_text = input_text.get(1.0, tk.END).strip()
    if not source_text:
        messagebox.showwarning("Warning", "Please enter some text or use the voice-to-text feature.")
        return

    target_language = language_combobox.get()
    if not target_language:
        messagebox.showwarning("Warning", "Please select a target language.")
        return

    try:
        translation = translator.translate(source_text, dest=target_language)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, translation.text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")

# GUI Setup
root = tk.Tk()
root.title("Voice-to-Text Translator")
root.geometry("600x500")

# Input Text Area
tk.Label(root, text="Input Text / Recognized Speech:", font=("Arial", 12)).pack(pady=5)
input_text = tk.Text(root, height=8, width=60)
input_text.pack(pady=5)

# Translate Button
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

voice_button = tk.Button(btn_frame, text="Voice to Text", command=voice_to_text, bg="#4CAF50", fg="white", font=("Arial", 10))
voice_button.grid(row=0, column=0, padx=10)

translate_button = tk.Button(btn_frame, text="Translate", command=translate_text, bg="#2196F3", fg="white", font=("Arial", 10))
translate_button.grid(row=0, column=1, padx=10)

# Status Label
label_status = tk.Label(root, text="", font=("Arial", 10), fg="green")
label_status.pack(pady=5)

# Language Dropdown
tk.Label(root, text="Select Target Language:", font=("Arial", 12)).pack(pady=5)
language_combobox = ttk.Combobox(root, state="readonly", values=list(LANGUAGES.values()), width=30)
language_combobox.pack(pady=5)
language_combobox.set("en")  # Default to English

# Output Text Area
tk.Label(root, text="Translated Text:", font=("Arial", 12)).pack(pady=5)
output_text = tk.Text(root, height=8, width=60, state="normal")
output_text.pack(pady=5)

# Run the GUI
root.mainloop()  