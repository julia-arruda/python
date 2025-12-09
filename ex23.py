print("Olá.")
print("Vamos brincar juntos? ")
opcao = int(input("Digite um zero para não, digite 1 para sim"))
c=0
soma=0
while opcao!=0:
    num = int(input("Informe um novo número: "))
    soma +=num
    c+=1;
    opcao = int(input("Digite um zero para não, digite 1 para sim"))
 
media = soma/c;
print(f"O resultado da média foi: {media} ")
