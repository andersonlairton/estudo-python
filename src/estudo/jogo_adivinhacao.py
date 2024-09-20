import random
def mensagemSuspense(tentativas) : 
    print("Eita!!! =O")
    print(f"Só tem mais {tentativas}")

def reduzTentativa(tentativa) : 
    print("Ops.... uma tentativa a menos!hahaha")
    return tentativa - 1

def adivinhe(tentativas) : 
    numero = random.randint(1,100)

    while tentativas > 0:
        suposto = input("Qual é o numero?")
        
        if not suposto.lstrip('-').isdigit() :
            print("Ops.... numero invalido ")
            tentativas = reduzTentativa(tentativas)
            continue
        
        if(int(suposto) == numero) :
            print("Acertou mizeravi!! Parabens =D")
            print(f"ainda tinha {tentativas} tentativas")
            break

        elif int(suposto) < numero:
            print("O número é maior!")
        else:
            print("O número é menor!")
        
        tentativas = reduzTentativa(tentativas)
        if tentativas < 5:
            mensagemSuspense(tentativas)

        if tentativas == 0:
            print('Acabaram as tentativas! =( ')
            print(f'o numero era {numero}')



print("neste script o usuario deve adiivinhar um numero entre 1 e 100 em ate 10,ou um numero que ele desejar menor que 10")
print('***************************')

tentativas = input("Digite a quantidade de tentativas ")

if not tentativas.lstrip('-').isdigit() :
    print("Ops.... numero invalido ")
elif int(tentativas) >= 10  : 
    print('olha lá hein, amostradinho você hein kkkk mas esse numero nao pode!')
    print('Vou te dar uma colher de chá para a gente brincar,então você vai ter 10 tentativas! =D')
    tentativas = 10
    adivinhe(int(tentativas))
elif int(tentativas) == 0:
    print("Nenhuma tentativa? Ai não da para jogar!")
else : 
    adivinhe(int(tentativas))
