lista = []

def editaDado(i, dado):
    lista[i] = dado

def adicionaDado(dado):
    lista.append(dado)
def removeDado(dado):
    lista.remove(dado)
def imprimeDados():
    print(lista)

print("este script faz a interação de uma lista de dados inseridos pelo usuario")
print("*****************")

opcao = 8
while opcao != 0:
    print("escolha uma opcao 1->adicionar;2->editar,;3->remover;4->imprimir;0->sair")

    opcao = input('digite uma opcao ')

    if not opcao.lstrip('-').isdigit():
        print("opcao invalida invalido")
    
    opcao = int(opcao)

    if opcao == 1:
        print("Você escolheu a opção adicionar")
        dado = input("Digite o dado que deseja adicionar ")
        adicionaDado(dado)
    elif opcao == 2:
        print("Você escolheu a opção editar")
        indice = input('digite o indice do dado que deseja editar')
        dado = input("Digite o dado que deseja editar")
        editaDado(int(indice),dado)
    elif opcao == 3:
        print("voce escolheu a opção remover")
        dado = input("digite o dado que deseja remover")
        removeDado(dado)
    elif opcao == 4:
        print('voce escolheu a opção imprimir')
        imprimeDados()
    


