def converteFahrenheit(temperatura) : 
    temperaturaConvertida = (temperatura * 9/5)+32
    return temperaturaConvertida
def converteKelvin(temperatura):
    temperaturaConvertida = temperatura+273.15
    return temperaturaConvertida

print("script faz a conversao de temperatura celcius para fahrenheit ou kevin")
print("***********************")
print("escolha a opção 1->Fahrenheit;2->Kelvin")
opcao = int(input("Digite a opção : "))
temperatura = input('Digite a temperatura em celcius: ')

if not temperatura.isdigit():
    print('temperatura deve ser um numero')
else:
    temperatura = float(temperatura)
    if(opcao == 1):
        print(round(converteFahrenheit(temperatura),2))
    elif(opcao == 2):
        print(round(converteKelvin(temperatura),2))
    else:
        print("opção invalida")
