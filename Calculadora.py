class Calc:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    print("---\nTipos de operação: \n( 1 ) Soma\n( 2 ) Subtração\n( 3 ) Multiplicação\n( 4 ) Divisão")

    op = int(input("Escolha o tipo de operação: "))

    if op == 1:
        print("A soma deu: ", n1 + n2)
    elif op == 2:
        print("A subtração deu: ", n1 - n2)
    elif op == 3:
        print("A multiplicação deu: ", n1 * n2)
    elif op == 4:
        if n2 != 0:
            print("A divisão deu: ", n1 / n2)
        else:
            print("Impossível dividir por zero")5
    else:
        print("Inválido")