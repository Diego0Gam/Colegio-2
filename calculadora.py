def calculadora(num, num2):
    suma = num + num2
    resta = num - num2
    multiplicacion = num * num2
    division = num / num2
    return suma, resta, multiplicacion, division
    
resultado = calculadora(5, 3)
print(resultado)