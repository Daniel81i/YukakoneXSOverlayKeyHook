from pynput import keyboard
import requests
import sys
import platform
from datetime import datetime
import os

# === ログファイル設定 ===
script_path = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(script_path)
script_name = os.path.basename(script_path).replace(".exe", "").replace(".py", "")
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file_path = os.path.join(script_dir, f"{script_name}_{timestamp}.log")

# === ログ出力関数 ===
def log(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{now}] {message}"
    print(full_message)
    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(full_message + "\n")

# === キーボードフック処理 ===
def win32_event_filter(msg, data):
    if 0xB1 == data.vkCode:
        if msg == 257:
            log("Mute Off (Pushed PreviousTrack key)")
            try:
                response = requests.get("http://localhost:15520/api/mute-off")
                log(f"Web request sent: {response.status_code}")
            except Exception as e:
                log(f"Failed to send web request: {e}")
        listener.suppress_event()

    if 0xB3 == data.vkCode:
        if msg == 257:
            log("Pushed Play/Pause key")
        listener.suppress_event()

    if 0xB0 == data.vkCode:
        if msg == 257:
            log("Mute On (Pushed NextTrack key)")
            try:
                response = requests.get("http://localhost:15520/api/mute-on")
                log(f"Web request sent: {response.status_code}")
            except Exception as e:
                log(f"Failed to send web request: {e}")
        listener.suppress_event()

# === 実行メイン処理 ===
log("Program started.")
log(f"Python version: {sys.version.split()[0]} ({platform.python_implementation()})")

try:
    with keyboard.Listener(
        on_press=None,
        on_release=None,
        win32_event_filter=win32_event_filter,
        suppress=False
    ) as listener:
        log("Listening for media keys... Press Ctrl+C to exit.")
        listener.join()
except KeyboardInterrupt:
    log("Ctrl+C detected. Shutting down gracefully.")
except Exception as e:
    log(f"Unexpected error: {e}")
finally:
    log("Program exited.")
