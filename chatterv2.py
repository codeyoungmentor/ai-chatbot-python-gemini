import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import requests

# API Key - Replace with your actual API Key
api_key = "AIzaSyAghvdcou5Q7ZQFDhGoyS-egbrJ2DgFel8"
api_endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

def send_message():
    user_input = input_box.get()
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {user_input}\n")
    chat_area.config(state=tk.DISABLED)
    input_box.delete(0, tk.END)

    # Call Gemini API
    prompt = {"contents": [{"parts": [{"text": user_input}]}]}
    try:
      response = requests.post(api_endpoint, json=prompt)
      response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
      response_data = response.json()
      answer = response_data['candidates'][0]['content']['parts'][0]['text']
      chat_area.config(state=tk.NORMAL)
      chat_area.insert(tk.END, f"AI: {answer}\n")
      chat_area.config(state=tk.DISABLED)
    except requests.exceptions.RequestException as e:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Error communicating with API: {e}\n")
        chat_area.config(state=tk.DISABLED)


# Main Window
root = ttk.Window(title="Chatter Box AI", themename="darkly")
root.geometry("800x600")

# Left Column - History
history_frame = ttk.Frame(root, padding=10)
history_frame.grid(row=0, column=0, sticky="nsew")
history_label = ttk.Label(history_frame, text="History", font=("Arial", 14, "bold"))
history_label.pack(pady=10)
history_text = tk.Text(history_frame, height=20, width=20, state=tk.DISABLED, wrap=tk.WORD)
history_text.pack(fill=tk.BOTH, expand=True)


# Middle Column - Chat Area
chat_frame = ttk.Frame(root, padding=10)
chat_frame.grid(row=0, column=1, sticky="nsew")

title_label = ttk.Label(chat_frame, text="Air Pollution", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

chat_area = tk.Text(chat_frame, height=20, width=60, state=tk.DISABLED, wrap=tk.WORD)
chat_area.pack(fill=tk.BOTH, expand=True)

input_frame = ttk.Frame(chat_frame)
input_frame.pack(fill=tk.X, pady=5)

input_box = ttk.Entry(input_frame, width=50)
input_box.pack(side=tk.LEFT, fill=tk.X, expand=True)

send_button = ttk.Button(input_frame, text="Send", command=send_message, bootstyle=SUCCESS)
send_button.pack(side=tk.RIGHT)

# Right Column - Chat Sources
source_frame = ttk.Frame(root, padding=10)
source_frame.grid(row=0, column=2, sticky="nsew")

source_label = ttk.Label(source_frame, text="Different Chatboxes", font=("Arial", 14, "bold"))
source_label.pack(pady=10)

sources_list = tk.Listbox(source_frame, height=10, width=20)
sources_list.insert(tk.END, "1. www.example.com")
sources_list.insert(tk.END, "2. www.anotherexample.com")
sources_list.pack(fill=tk.BOTH, expand=True)

sources_label = ttk.Label(source_frame, text="Sources", font=("Arial", 12))
sources_label.pack(pady=10)


# Settings Icon
settings_frame = ttk.Frame(root)
settings_frame.grid(row=0, column=2, sticky="ne", padx=10, pady=10)

settings_icon = ttk.Label(settings_frame, text="⚙️", font=("Arial", 20))  # Using a gear icon for settings
settings_icon.pack(side=tk.RIGHT, padx=5)

email_label = ttk.Label(settings_frame, text="example@gmail.com", font=("Arial", 10))
email_label.pack(side=tk.RIGHT)

# Configure grid layout for resizing
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)


root.mainloop()