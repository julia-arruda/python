from math import tan
oposto=float(input("Informe o número do cateto oposto: "))
adjacente=float(input("Informe o número do cateto adjacente: "))
div=oposto/adjacente
resultado=tan(div)
print(f"A hipotenusa é:{resultado}")