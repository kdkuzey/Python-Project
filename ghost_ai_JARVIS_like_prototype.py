import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Voice recognition function
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for commands...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Request error from Google Speech Recognition.")
        return ""

# AI logic
def ghost_ai():
    speak("Ghost AI activated. Say 'Lumos' to start or 'Nox' to shut down.")
    while True:
        command = listen()
        if "lumos" in command:
            speak("Activating systems...")
        elif "nox" in command:
            speak("Shutting down. Goodbye.")
            break

ghost_ai()

import pyaudio
import speech_recognition as sr
import time

# GHOST AI ko activate/deactivate karne ke flags
ghost_active = False

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening for a command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"👾 You said: {command}")
        return command
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"⚠️ Error with Google Speech Recognition service: {e}")
        return ""

def main():
    global ghost_active

    print("🔥 GHOST AI is ready. Say 'Lumos' to activate or 'Nox' to shut down.")
    
    while True:
        command = listen_for_command()

        if "lumos" in command:
            if not ghost_active:
                ghost_active = True
                print("🌟 GHOST AI Activated!")
            else:
                print("✅ GHOST is already active.")

        elif "nox" in command:
            if ghost_active:
                ghost_active = False
                print("💤 GHOST AI Shutting Down...")
            else:
                print("🚫 GHOST is already inactive.")

        elif ghost_active:
            print(f"🤖 GHOST is active. Processing: {command}")

        time.sleep(1)

if __name__ == "__main__":
    main()

import speech_recognition as sr
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("Error with the speech recognition service.")
            return ""

def ghost_ai():
    speak("Ghost AI is ready. Say Lumos to activate or Nox to shut down.")
    while True:
        command = listen()
        if "lumos" in command:
            speak("GHOST AI activated!")
            print("🟢 GHOST AI activated!")
        elif "nox" in command:
            speak("Shutting down GHOST AI.")
            print("🔴 GHOST AI shutting down...")
            break

ghost_ai()

import speech_recognition as sr
import pyttsx3
import threading

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)  # Speed up speech rate

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)  # Faster noise adjustment
        print("🎤 Listening...")
        audio = recognizer.listen(source, timeout=5)  # Timeout if no command detected
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"👾 You said: {command}")
            return command
        except (sr.UnknownValueError, sr.RequestError):
            return ""

def process_command(command):
    if "lumos" in command:
        print("🌟 GHOST AI Activated!")
        speak("Ghost AI activated!")
    elif "nox" in command:
        print("💤 GHOST AI Shutting Down...")
        speak("Shutting down Ghost AI.")
        exit()

def ghost_ai():
    speak("GHOST AI is ready. Say 'Lumos' to activate or 'Nox' to shut down.")
    while True:
        command = listen()
        if command:
            threading.Thread(target=process_command, args=(command,)).start()

# Run the AI
if __name__ == "__main__":
    ghost_ai()

    import speech_recognition as sr
import pyttsx3
import threading
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        print("🎤 Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"👾 You said: {command}")
            return command
        except (sr.UnknownValueError, sr.RequestError):
            return ""

def process_command(command):
    if "lumos" in command:
        print("🌟 GHOST AI Activated!")
        speak("Ghost AI activated!")
    elif "nox" in command or "bye" in command:
        print("💤 GHOST AI Shutting Down...")
        speak("Shutting down Ghost AI.")
        sys.exit()

def ghost_ai():
    speak("GHOST AI is ready. Say 'Lumos' to activate or 'Nox' or 'Bye' to shut down.")
    while True:
        command = listen()
        if command:
            threading.Thread(target=process_command, args=(command,)).start()

if __name__ == "__main__":
    ghost_ai()


import speech_recognition as sr
import pyttsx3
import threading

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)  # Speed up speech rate

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)  # Faster noise adjustment
        print("🎤 Listening...")
        audio = recognizer.listen(source, timeout=5)  # Timeout if no command detected
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"👾 You said: {command}")
            return command
        except (sr.UnknownValueError, sr.RequestError):
            return ""

def process_command(command):
    if "lumos" in command:
        print("🌟 GHOST AI Activated!")
        speak("Ghost AI activated!")
    elif "nox" in command:
        print("💤 GHOST AI Shutting Down...")
        speak("Shutting down Ghost AI.")
        exit()

def ghost_ai():
    speak("GHOST AI is ready. Say 'Lumos' to activate or 'Nox' to shut down.")
    while True:
        command = listen()
        if command:
            threading.Thread(target=process_command, args=(command,)).start()

# Run the AI
if __name__ == "__main__":
    ghost_ai()


import speech_recognition as sr
import pyttsx3
import threading
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        print("🎤 Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"👾 You said: {command}")
            return command
        except (sr.UnknownValueError, sr.RequestError):
            return ""

def process_command(command):
    if "lumos" in command:
        print("🌟 GHOST AI Activated!")
        speak("Ghost AI activated!")
    elif "nox" in command or "bye" in command:
        print("💤 GHOST AI Shutting Down...")
        speak("Shutting down Ghost AI.")
        sys.exit()

def ghost_ai():
    speak("GHOST AI is ready. Say 'Lumos' to activate or 'Nox' or 'Bye' to shut down.")
    while True:
        command = listen()
        if command:
            threading.Thread(target=process_command, args=(command,)).start()

if __name__ == "__main__":
    ghost_ai()

import speech_recognition as sr
import pyttsx3
import threading
import time
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen for voice commands
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        print("🎤 Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"👾 You said: {command}")
            return command
        except sr.UnknownValueError:
            print("❌ Couldn't understand the audio.")
            return ""
        except sr.RequestError:
            print("⚠️ Speech recognition service error.")
            return ""
        except TimeoutError:
            print("⏳ Listening timed out.")
            return ""

# Process voice commands
def process_command(command):
    if "lumos" in command:
        print("🌟 GHOST AI Activated!")
        speak("Ghost AI activated!")

    elif "sleep mode" in command:
        print("😴 GHOST AI entering sleep mode for 10 seconds...")
        speak("Entering sleep mode for 10 seconds.")
        time.sleep(10)
        print("⏰ GHOST AI is awake again!")
        speak("I'm awake now.")

    elif "restart" in command:
        print("🔄 Restarting GHOST AI...")
        speak("Restarting Ghost AI.")
        time.sleep(2)
        ghost_ai()

    elif "nox" in command or "bye" in command:
        print("💤 GHOST AI Shutting Down...")
        speak("Shutting down Ghost AI.")
        sys.exit()

# Main AI loop
def ghost_ai():
    speak("GHOST AI is ready. Say 'Lumos' to activate, 'Sleep mode' to pause, 'Restart' to reboot, or 'Nox' or 'Bye' to shut down.")
    while True:
        command = listen()
        if command:
            threading.Thread(target=process_command, args=(command,)).start()

# Start the AI
if __name__ == "__main__":
    ghost_ai()


import speech_recognition as sr
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening for a command...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)  # Quick noise adjustment
        
        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)  # Fast listen
            command = recognizer.recognize_google(audio)
            print(f"👾 You said: {command}")
            return command.lower()

        except sr.UnknownValueError:
            print("❌ Didn't catch that.")
            return ""

        except sr.RequestError:
            print("⚠️ Google API is not responding. Using offline mode.")
            return ""

        except TimeoutError:
            print("⏳ Listening timed out.")
            return ""

def ghost_ai():
    speak("GHOST AI is ready. Say Lumos to activate or Nox to shut down.")
    while True:
        command = listen()
        if "lumos" in command:
            speak("GHOST AI activated!")
            print("🌟 GHOST AI Activated!")
        elif "nox" in command:
            speak("Shutting down GHOST AI.")
            print("💤 GHOST AI Shutting Down...")
            break

ghost_ai()

import os
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Path to Vosk model
model_path = "models/vosk-model-small-en-us-0.15"
if not os.path.exists(model_path):
    print("Vosk model not found. Please check the path.")
    exit(1)

# Load the Vosk model
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

# Audio queue for capturing voice input
q = queue.Queue()

# Audio callback function
def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    q.put(bytes(indata))

# Listen for voice commands using Vosk
def listen():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Listening for commands...")
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                command = result.get("text", "").lower()
                if command:
                    print(f"You said: {command}")
                    return command

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main AI loop
def ghost_ai():
    speak("GHOST AI activated. Awaiting your command.")
    while True:
        command = listen()
        
        if "lumos" in command:
            speak("I am online and ready.")
        elif "nox" in command or "shutdown" in command or "deactivate" in command:
            speak("Shutting down GHOST AI.")
            break
        elif "sleep mode" in command:
            speak("Entering sleep mode.")
        else:
            speak("Command not recognized. Please try again.")

ghost_ai()
