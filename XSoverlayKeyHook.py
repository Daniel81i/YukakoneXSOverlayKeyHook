from pynput import keyboard
import requests
import sys
import platform
from datetime import datetime
import os
import threading

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

# === Enterキーで終了する処理 ===
def wait_for_exit():
    input()
    log("Manual exit requested. Stopping listener.")
    os._exit(0)  # 安全に強制終了

# バックグラウンドで入力待ちを起動
threading.Thread(target=wait_for_exit, daemon=True).start()

# === 起動ログ ===
log("Program started.")
log(f"Python version: {sys.version.split()[0]} ({platform.python_implementation()})")
log("Yukakone Mute On/Off XSOverlay Media Key Hook Listener: Previous->Off Next->On")
log("Listening for media keys...")
log("Press [Enter] to exit the program at any time.")

# === キーボード入力処理 ===
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

    if 0xB0 == data.vkCode:
        if msg == 257:
            log("Mute On (Pushed NextTrack key)")
            try:
                response = requests.get("http://localhost:15520/api/mute-on")
                log(f"Web request sent: {response.status_code}")
            except Exception as e:
                log(f"Failed to send web request: {e}")
        listener.suppress_event()

# === リスナー起動 ===
with keyboard.Listener(
    on_press=None,
    on_release=None,
    win32_event_filter=win32_event_filter,
    suppress=False
) as listener:
    listener.join()
