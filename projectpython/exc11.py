import  pyttsx3

"""instalar a biblioteca"""

engine= pyttsx3.init()
rate= engine.getProperty("rate")
engine.setProperty("rate", rate-50)


engine.setProperty("volume",1)

texto="ola, isso é um teste de ia ha hah hah "

engine.say(texto)
engine.runAndWait()