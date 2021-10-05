
paises = {
"ar": "Argentina",
"es": "España",
"us": "Estados Unidos",
"fr": "Francia"
}

while True:
    try:
        codigo = input('Ingrese codigo del pais: ')
        print(paises[codigo])
        break
    except Exception:
        print('Ese codigo de pais no existe.')