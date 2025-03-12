import pyttsx3
import speech_recognition as sr
engine=pyttsx3.init()
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    engine.say("Fale Algo...")
    engine.runAndWait()
    audio=recognizer.listen(source)
try:
    #uso da API Google
    text=recognizer.recognize_google(audio,language="pt-BR")
    engine.say(f"Você disse: {text}")
    engine.runAndWait()
except sr.UnknownValueError:
    print("Não entendi seu áudio")
except sr.RequestError:
    print("Erro de requisição")





