import pyttsx3
engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
engine.say("Olá mundo")
engine.runAndWait()