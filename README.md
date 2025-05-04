# Yukakone XSOverlay Trigger Listener

This is a background utility for Windows that listens to **media key inputs from XSOverlay**  
and sends HTTP requests to control **Yukanone's[ゆかコネ] mute ON/OFF** via local web queries.

## Features

- Detects XSOverlay **"Next Track" and "Previous Track"** media keys (`0xB0`, `0xB1`)
- Sends corresponding HTTP requests to a locally running Yukakone apps
- Log files are saved in the same folder as the executable with a timestamped filename

## Usage

1. Run `XSoverlayKeyHook.exe`
2. Press the XSOverlay **"Next Track"** media key (`0xB0`) to send a `MuteOn` command to Yukanone
3. Press the XSOverlay **"Previous Track"** media key (`0xB1`) to send a `MuteOff` command to Yukanone
4. Press **Enter** to gracefully exit the program

## Log Output

- Log files are saved in the same directory as the executable

## About this Script

This tool is based on the article:  
**"XSOverlayの手首メニューのメディアキーを自分のアプリの制御に利用する方法"**  
https://zenn.dev/dimebag29/articles/d29376aae38d97

Since the source was publicly shared, it's assumed to be free for use and modification.  
However, please refrain from claiming it as your own creation.  
This tool is provided **as-is**, with **no guarantees or warranties** of any kind.
