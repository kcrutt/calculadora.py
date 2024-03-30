def calculadora():
    numA = int(input())
    operacao = input()
    numB = int(input())


    if operacao == "+":
        resultado = numA + numB
    elif operacao == "-":
        resultado = numA - numB
    elif operacao == "*":
        resultado = numA * numB
    elif operacao == "/":
        if numB != 0:
            resultado = numA / numB
        else:
            print("Error! Divisão por 0")
    elif operacao == "%":
        resultado = (numB / 100) * numA
    else:
        print("Error")
    
    print(resultado)

calculadora()