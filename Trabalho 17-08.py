# Aluno: Thiago Vinícius Pereira Borges.
# Enunciado: Programa em Python no qual proporciona o resultado das operações de União(U), Interseção(I),...
# ...Diferença(D), Produto Cartesiano(C), por meio da leitura de um arquivo .txt contendo na primeira linha...
# ...a quantidade de operações, nas próximas a sequência de Operação, Conjunto 1 e Conjunto 2.


def uniao(conjunto1, conjunto2):

    junção = []

    vetor = []

    junção.extend(conjunto1)
    junção.extend(conjunto2)

    for a in junção:
        if a not in vetor:
            vetor.append(a)

    return vetor


def intersecao(conjunto1, conjunto2):

    vetor = []

    for a in conjunto1:
        for b in conjunto2:
            if a == b:
                vetor.append(a)

    return vetor


def diferenca(conjunto1, conjunto2):

    vetor = []

    vetor.extend(conjunto1)

    for a in conjunto1:
        for b in conjunto2:
            if a == b:
                vetor.remove(a)

    return vetor


def prod_cartesiano(conjunto1, conjunto2):

    vetor = []

    for a in conjunto1:
        for b in conjunto2:

            # Colocando os pares conforme a formatação solicitada
            if (a + ", " + b) not in vetor:
                vetor.append(a + ", " + b)

    return vetor


# Arquivo de Texto
file = open("Teste1.txt", "r")
operacoes = file.readline().strip()


# Laço de repetição para garantir que a quantidade de operações definidas no arquivo .txt sejam efetuadas
for i in range(0, int(operacoes)):

    decisao = file.readline().strip()

    conjunto1 = file.readline().strip().split(", ")
    conjunto2 = file.readline().strip().split(", ")

    # Variável que armazena o valor final de cada operação por meio das funções
    resultado = []


    if decisao == "U":

        resultado = uniao(conjunto1, conjunto2)

        # Exibição do Conjunto 1 na formatação exigida
        tamanho1 = len(conjunto1)
        print("União:", end="")
        print(" conjunto 1", "{", end="")

        for index1 in range(tamanho1):
            if index1 != tamanho1 - 1:

                print(conjunto1[index1], end=",")
            else:
                print(str(conjunto1[index1]) + "}", end=", ")

        # Exibição do Conjunto 2 na formatação exigida
        tamanho1 = len(conjunto2)
        print("conjunto 2", "{", end="")

        for index1 in range(tamanho1):
            if index1 != tamanho1 - 1:

                print(conjunto2[index1], end=",")
            else:
                print(str(conjunto2[index1]) + "}", end=". ")

        # Exibição do Resultado na formatação exigida
        tamanho1 = len(resultado)
        print("Resultado:", "{", end="")

        for index1 in range(tamanho1):
            if index1 != tamanho1 - 1:

                print(resultado[index1], end=",")
            else:
                print(str(resultado[index1]) + "}")


    elif decisao == "I":

        resultado = intersecao(conjunto1, conjunto2)

        # Exibição do Conjunto 1 na formatação exigida
        tamanho1 = len(conjunto1)
        print("Interseção:", end="")
        print(" conjunto 1", "{", end="")

        for index1 in range(tamanho1):
            if index1 != tamanho1 - 1:

                print(conjunto1[index1], end=",")
            else:
                print(str(conjunto1[index1]) + "}", end=", ")

        # Exibição do Conjunto 2 na formatação exigida
        tamanho1 = len(conjunto2)
        print("conjunto 2", "{", end="")

        for index1 in range(tamanho1):
            if index1 != tamanho1 - 1:

                print(conjunto2[index1], end=",")
            else:
                print(str(conjunto2[index1]) + "}", end=". ")

        # Exibição do Resultado na formatação exigida
        tamanho1 = len(resultado)
        print("Resultado:", "{", end="")

        for index1 in range(tamanho1):
            if index1 != tamanho1 - 1:

                print(resultado[index1], end=",")
            else:
                print(str(resultado[index1]) + "}")


    elif decisao == "D":

        resultado = diferenca(conjunto1, conjunto2)

        # Exibição do Conjunto 1 na formatação exigida
        tamanho1 = len(conjunto1)
        print("Diferença:", end="")
        print(" conjunto 1", "{", end="")

        for index1 in range(tamanho1):
            if index1 != tamanho1 - 1:

                print(conjunto1[index1], end=",")
            else:
                print(str(conjunto1[index1]) + "}", end=", ")

        # Exibição do Conjunto 2 na formatação exigida
        tamanho1 = len(conjunto2)
        print("conjunto 2", "{", end="")

        for index1 in range(tamanho1):
            if index1 != tamanho1 - 1:

                print(conjunto2[index1], end=",")
            else:
                print(str(conjunto2[index1]) + "}", end=". ")

        # Exibição do Resultado na formatação exigida
        tamanho1 = len(resultado)
        print("Resultado:", "{", end="")

        for index1 in range(tamanho1):
            if index1 != tamanho1 - 1:

                print(resultado[index1], end=",")
            else:
                print(str(resultado[index1]) + "}")


    elif decisao == "C":

        resultado = prod_cartesiano(conjunto1, conjunto2)

        # Exibição do Conjunto 1 na formatação exigida
        tamanho1 = len(conjunto1)
        print("Produto Cartesiano:", end="")
        print(" conjunto 1", "{", end="")

        for index1 in range(tamanho1):
            if index1 != tamanho1 - 1:

                print(conjunto1[index1], end=",")
            else:
                print(str(conjunto1[index1]) + "}", end=", ")

        # Exibição do Conjunto 2 na formatação exigida
        tamanho1 = len(conjunto2)
        print("conjunto 2", "{", end="")

        for index1 in range(tamanho1):
            if index1 != tamanho1 - 1:

                print(conjunto2[index1], end=",")
            else:
                print(str(conjunto2[index1]) + "}", end=". ")

        # Exibição do Resultado na formatação exigida
        tamanho1 = len(resultado)
        print("Resultado:", "{", end="")


        for index2 in range(tamanho1):

            print("(", end="")
            print(resultado[index2], end="")

            if index2 == tamanho1 - 1:
                print(")", end="} \n")

            else:
                print(")", end=", ")
