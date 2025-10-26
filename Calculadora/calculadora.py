def soma (num1, num2):
    resultado = num1 + num2
    return resultado

def subtracao (num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicacao (num1, num2):
    resultado = num1 * num2
    return resultado

def divisao (num1, num2):
    
    if num2 == 0:
        return "Erro: Não é possível dividir por zero!"
    else:
        resultado = num1 / num2
        return resultado

while True:
    operacao = int(input("\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Sair\nEscolha uma opção: "))

    if operacao == 5:
        print ("\nAté logo!")
        break
    
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    

    if operacao == 1:
        print(f"Resultado: {soma(num1, num2)}")
    
    elif operacao == 2:
        print(f"Resultado: {subtracao(num1, num2)}")
        
    elif operacao == 3:
        print(f"Resultado: {multiplicacao(num1, num2)}")
    elif operacao == 4:
        print(f"Resultado: {divisao(num1, num2)}")
    else:
        print ("Operação invalida!")
