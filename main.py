#!/usr/bin/env python3
"""RS - a small Hinglish AI assistant demo.

Usage: python3 main.py
Type a message, RS replies with a simple Hinglish response.
Type 'exit' to quit.
"""

def reply(msg):
    msg = msg.lower()
    if "namaste" in msg or "hello" in msg or "hi" in msg:
        return "Namaste! Main RS hun, tumhara AI assistant. Kaise madad karun?"
    if "song" in msg or "music" in msg:
        return "Music ke liye title, hashtag aur checklist wale tools dekh lo, wo RS Worldwide Music ke kaam me madad karte hain."
    if "codex" in msg:
        return "Codex se simple tools banaye ja sakte hain, jaise title generator aur caption helper."
    return "Samajh gaya. Tum is baare me thoda aur batao, main simple Hinglish me jawab dunga."

if __name__ == "__main__":
    print("RS AI Assistant - type 'exit' to quit")
    while True:
        try:
            user = input("Tum: ")
        except EOFError:
            break
        if user.strip().lower() == "exit":
            print("RS: Alvida!")
            break
        print("RS:", reply(user))
