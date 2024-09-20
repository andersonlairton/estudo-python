import time
def contagemRegressiva(num):
    regressiva = num

    while regressiva > 0:
        print(regressiva)
        regressiva-=1

        if regressiva < 5:
            print("Ta quase lá galeraaaaaaaa!!!")
        if(regressiva == 0):
            print('Feliz ano novooooooo !!!!!!!!!')

            fogos = 'poow!!'
            for i in range(100):
                print(fogos)
                fogos+= 'pow! '
                time.sleep(0.1)

print("este script efetua a contagem regressiva e devolve a mensagem feliz ano novo")
print("************")

num = input("digite o numero ")

if not num.lstrip('-').isdigit():
    print("numero invalido")
else :
    contagemRegressiva(int(num))