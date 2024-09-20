def verifica(num):
    tipo = ''
    if(num%2 == 0):
        tipo = 'Par'
    else:
        tipo = 'Impar'
    return tipo


print("este script verifica se o numero é par ou impar")
print("*********************")
numero = input("digite um numero para verificação: ")

# verificando se o numero é valido ou negativo
if not numero.lstrip('-').isdigit():
    print('Numero digitado invalido')
else:
    print(f"Numero digitado {numero}")
    print(f"O numero {numero} é {verifica(float(numero))}")