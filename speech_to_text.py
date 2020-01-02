import speech_recognition as sr
print(sr.__version__) # just to print the version not required
r = sr.Recognizer()
harvard = sr.AudioFile('input_audio/1.wav')
with harvard as source:
    audio = r.record(source)
print(type(audio))
print(r.recognize_google(audio))