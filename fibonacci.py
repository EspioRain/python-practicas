def fib(x):

    if x < 2:
        print("La cantidad debe ser mayor a 2")
        return None
    else:
        valores = []
        fn = []
        for i in range(x):
            valores.append(i)

        for i in range(len(valores)):
            if i > 1:
                fn.append(fn[i-2]+fn[i-1])
            elif i == 0:
                fn.append(0)
            elif i == 1:
                fn.append(1)
        return fn
    


a = int(input("Ingrese la cantidad de numeros (>2): "))


f =open("fibo.txt", "w")

resultado = (fib(a))
if resultado != None:
    f.write(f"Fibonacci de {a}"+"\n")

    for i in range(len(resultado)):
        f.write(str(resultado[i])+"\n")

    f.close()
    


