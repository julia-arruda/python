print("Conversão de bases numéricas.")

num = int(input("Informe um número inteiro: "))

print('Para converter de inteiro para binário: Aperte 1')
print('Para converter de inteiro para octal: Aperte 2')
print('Para converter de inteiro para hexadecimal: Aperte 3')
print('Senão quer converter: Aperte outra coisa')

digito = int(input("Informe o número escolhido: "))


if digito == 1:
    resultado = bin(num)
    print(f"{resultado}")
elif digito ==2:
    resultado = oct(num)
    print(f"{resultado}")
elif digito==3:
    resultado =hex(num)
    print(f"{resultado}")
else:
    print("Obrigada pela atenção!")