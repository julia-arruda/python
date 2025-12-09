#nome = str(input("Qual é o seu nome? "))

#if nome == 'Julia':
#    print(f"Você é inteligente. {nome}")
#elif nome=="juliana":
#    print('Você não é bem-vindo. Volte novamente!')
#else:
#     print("Boa tarde. ")

print("Empréstimo bancário")

valor = float(input("Informe o valor da casa: "))
salario = float(input('Qual o salário do comprador: '))
meses= int(input('Em quantos meses ele vai pagar: '))
prestacao = valor/meses;

if prestacao < (salario*0.3):
    print("Empréstimo concebido.")
else:
    print("Que pena! Empréstimo negado.")