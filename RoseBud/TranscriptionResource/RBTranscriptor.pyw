from re import S
import speech_recognition as sr
from os import path
import json


def transcribe(file):
    AUDIO_FILE = path.realpath("uploads\\audio\\"+file)

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    transcript = json.loads(r.recognize_vosk(audio))
    
    return transcript["text"]


