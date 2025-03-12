from logging import exception

import speech_recognition as sr
from scipy.cluster.vq import whiten
from speech_recognition.recognizers.google_cloud import recognize

recognizer=sr.Recognizer()

with sr.Microphone() as source:
     print(("fale alguma coisa"))
     audio=recognizer.listen(source)
try:

  text=recognizer.recognize_google(audio,language="pt-br")
  print("text")

except sr.UnknownValueError:
 print("não entendi seu audio")

except sr.RequestError:
 print("erro de requisição")
