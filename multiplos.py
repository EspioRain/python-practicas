def multiplos(x):
    numeros = []
    multip = [];
    for i in range(x):
        if i > 0:
            numeros.append(i)
    
    for i in range(len(numeros)):
        if numeros[i] % 3 == 0 and numeros[i] % 5 == 0:
            multip.append(numeros[i])
            
    return multip
            

print(multiplos(100))

nombre = "Carlos"

frase = f'Hola {nombre} sos puto'
