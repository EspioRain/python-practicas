import time
import requests
import os

###################

def info():
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Santa%20Fe&units=metric&appid=e5e51f930637198e7fce594deff4a8d1")
    if r.status_code == 200:
        data = r.json()
        temp = data["main"]["temp"]
        hum = data["main"]["humidity"]
        pres = data["main"]["pressure"]
        vis = data["visibility"]
        nubes = data["clouds"]["all"]
        return [temp,hum,pres,vis,nubes]
    else:
        return False


###################


os.system("cls")

while True:
    print("""
    1 - Ver magnitudes
    2 - Prediccion
    3 - Salir
    """)
    opcion = input(">>> ")
    if opcion == "1":
        d = info()
        if d:
            print("La temperatura es:",d[0])
            print("La humedad es:",d[1])
            print("La presion es:",d[2])
            print("La visibilidad es:",d[3])
            print("El cielo esta",d[4],r"% cubierto")
        else:
            print("Hay un error en el servicio")
    elif opcion == "2":
        d = info()
        if d:
            if d[1] > 90 and d[2] < 1013:
                print("Se acerca la lluvia")
            else:
                print("No hay lluvia cerca")
        else:
            print("Hay un error en el servicio")
    elif opcion == "3":
        print("Gracias por usar nuestro programa!")
        break
    else:
        print("Error de opción")
    input("Toque ENTER para continuar...")
    os.system("cls")