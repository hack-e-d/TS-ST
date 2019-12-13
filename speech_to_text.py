from os import path
from pydub import AudioSegment
import speech_recognition as sr 
import soundfile as sf        

    
# use the audio file as the audio source 
wav_path = "sample.wav"
 
r = sr.Recognizer() 
print(r)
with sr.AudioFile(wav_path) as source:
    audio = r.record(source) 
r.recognize_google(audio)
