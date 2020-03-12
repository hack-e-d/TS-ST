import speech_recognition as sr

def voice_input():
    a2t=""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        r.record(source,duration=2)
        print("Say something!")
        audio = r.listen(source)
    try:
        a2t=r.recognize_google(audio)
        print("YOU SAID : " + a2t)
    except sr.UnknownValueError:
        print("Google could not understand audio")
    except sr.RequestError as e:
        print("Google error; {0}".format(e))
    return a2t 
voice_input()
