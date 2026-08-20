def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    if b != 0:
        return a/b
    else:
        print("Não é possivel dividir por zero.")

a = float(input("Informe o primeiro valor: "))
b = float(input("Informe o segundo valor: "))

print("Entre as opções: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao_menu = int(input("Qual operação você gostaria de utilizar? "))

if opcao_menu == 1:
    resultado1 = soma(a,b)
    print(resultado1)

if opcao_menu == 2:
    resultado2 = subtracao(a,b)
    print(resultado2)

if opcao_menu == 3:
    resultado3 = multiplicacao(a,b)
    print(resultado3)

if opcao_menu == 4:
    resultado4 = divisao(a,b)
    print(resultado4)