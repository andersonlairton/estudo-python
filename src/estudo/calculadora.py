
def soma(n1,n2):
    return n1+n2
def subtracao(n1,n2):
    return n1-n2
def divisao(n1,n2):
    if(n1 == 0 or n2==0):
        return 'não é possivel divisão por zero'
    return n1/n2
def multiplicacao(n1,n2):
    return n1*n2

num1 = int(input("digite o primeiro numero: "))
print(f"voce digitou {num1} ")
num2 = int(input("digite o segundo numero: "))
print(f"voce digitou {num2} ")
print("***********************************************")
print("Operações disponiveis : 1-> adição;2->subtração;3->divisão;4->multiplicação")
operacao = input("digite o numero da operacao desejada ")

if(operacao == '1'):
    print(soma(num1,num2))
elif(operacao == '2'):
    print(subtracao(num1,num2))
elif(operacao == '3'):
    print(divisao(num1,num2))
elif(operacao == '4'):
    print(multiplicacao(num1,num2))
else:
    print(f"Operação {operacao} não corresponde a nenhuma operação mepada")