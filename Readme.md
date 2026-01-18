# Keystroke Logging Demonstration Project

## 📌 Overview
This project is a **cybersecurity demonstration** of how keystrokes can be captured using Python.  
It is designed for **educational purposes only** to raise awareness about the risks of keyloggers and how attackers might exploit them.  
⚠️ **Disclaimer**: This project must only be used in a controlled environment. Do not use it to capture sensitive information such as passwords, personal data, or private communications.

---

## 🎯 Features
- Captures keystrokes in real time.
- Logs output in:
  - **Letter-wise**: Each keystroke recorded individually.
- Adds **timestamps** to each log entry.
- Optional **Tkinter GUI** for interactive demonstration.
- Simple **visualizer** to analyze keystroke frequency.

---

## 🛠️ Project Structure

KeystrokeLoggerDemo/
│
├── logger.py            # Core keystroke logging logic (text + JSON output)
├── gui_demo.py          # Tkinter GUI with consent popup and start/stop buttons
├── visualizer.py        # Optional: analyze keystroke frequency from logs
│
├── keylog.txt           # Auto-created text log file (timestamp + keystrokes)
├── keylog.json          # Auto-created JSON log file (structured keystrokes)
│
├── requirements.txt     # Python dependencies (pynput, tkinter, etc.)
├── README.md            # Documentation with usage, disclaimer, and examples
└── .gitignore           # (optional) ignore log files or virtual environment
