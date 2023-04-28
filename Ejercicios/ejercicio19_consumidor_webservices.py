#pip install requests
import requests
import json

KEY = "ee6e8770"
titulo = input("Introduce el título de la película:")
url = f'http://www.omdbapi.com/?apikey=ee6e8770&t={titulo}'

def guardar_html(*args):
    fichero = open(args[0] + ".html", mode="w", encoding="utf-8")
    fichero.write(f"<h1>{args[0]}</h1>")
    for elemento in args[1:-1]:
        fichero.write(f"<p>{elemento}</p>")
    fichero.write(f"<img src='{args[len(args)-1]}'>")
    fichero.close()

def autoguardar_pelicula(*args):
    fichero = open(args[0] + ".movie", mode="w", encoding="utf-8")
    for elemento in args:
        fichero.write(elemento)
        fichero.write("\n")    
    fichero.close()

def guardar_pelicula(title, year, rated, released, plot):
    fichero = open(title + ".movie", mode="w", encoding="utf-8")
    fichero.write(title)
    fichero.write("\n")
    fichero.write(year)
    fichero.write("\n")
    fichero.write(rated)
    fichero.write("\n")
    fichero.write(released)
    fichero.write("\n")
    fichero.write(plot)
    fichero.write("\n")
    fichero.close()

respuesta = requests.get(url)
if (respuesta.status_code==200):
    informacion = json.loads(respuesta.text)
    title = informacion["Title"]
    year = informacion["Year"]
    rated = informacion["Rated"]
    released = informacion["Released"]
    plot = informacion["Plot"]
    poster = informacion["Poster"]
    #guardar_pelicula(title, year, rated, released, plot)
    autoguardar_pelicula(title, year, rated, released, plot)
    guardar_html(title, year, rated, released, plot, poster)
else:
    print("Ha ido mal:" + str(respuesta.status_code))