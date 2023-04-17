from gtts import gTTS
import os
nombre = input("Introduce tu nombre:")
mytext = f"Hola, {nombre}, bienvenido a mi mundo"
audio = gTTS(text=mytext, lang="es", slow=False)
audio.save("example.mp3")
os.system("start example.mp3")