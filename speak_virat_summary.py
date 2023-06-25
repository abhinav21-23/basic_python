import pyttsx3
import wikipedia
a=wikipedia.summary("Virat kohli", sentences=10)
print(a)
pyttsx3.speak(a)