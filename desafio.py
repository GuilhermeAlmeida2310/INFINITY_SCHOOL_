# Crie uma calculadora com opções de soma, multiplicação, subtração, divisão e sair. (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.) Utilize funções de rotina para cada operação e funções de unidade lógica para realizar os cálculos.

def menu_calculadora():
    print('Menu Calculadora')
    print('1-) Somar')
    print('2-) Subtrair')
    print('3-) Multiplicar')
    print('4-) Dividir')
    print('5-) Sair')

def somar():
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite um número: '))
    resultado = num1 + num2
    print(f'Resultado: {resultado}')
    return resultado

def subtrair():
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite um número: '))
    resultado = num1 - num2
    print(f'Resultado: {resultado}')
    return resultado

def mult():
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite um número: '))
    resultado = num1 * num2
    print(f'Resultado: {resultado}')
    return resultado

def dividir():
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite um número: '))
    if num1 <= 0 or num2 <= 0:
        print('Divisão não pode ser feita com o número 0!')
    else:
        resultado = num1 / num2
        print(f'Resultado: {resultado}')
        return resultado

while True:
    menu_calculadora()
    opcao = int(input('Insira uma opção: '))
    if opcao > 5 or opcao < 1:
        print('Insira uma opção válida!')
        continue
    elif opcao == 1:
        somar()
    elif opcao == 2:
        subtrair()
    elif opcao == 3:
        mult()
    elif opcao == 4:
        dividir()
    else:
        print('Enrrando o programa. Até a próxima :)')
        break


