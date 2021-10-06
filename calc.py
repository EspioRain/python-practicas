def operaciones(a, b):
    while True:
        try:
         a = int(a)
         break
        except (TypeError, ValueError):
         a = input('Primer valor inválido, ingreselo nuevamente: ')
    while True:
        try:
            b = int(b)
            a/b
            break
        except (TypeError, ValueError, ZeroDivisionError):
            b=input('Segundo valor invalido, ingreselo nuevamente: ')
    print(f'{a} + {b} = {a+b}')
    print(f'{a} - {b} = {a-b}')
    print(f'{a} * {b} = {a*b}')
    print(f'{a} / {b} = {a/b}')