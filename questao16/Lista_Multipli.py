def main():
    listaNum = []
    print("Digite os 10 números da lista: ")
    for i in range(0, 10):
        listaNum.append(int(input(f"Número {i+1}: ")))
    print("Lista normal: ")

    for i in listaNum:
        print(i, end=", ")
    print("")
    print("Lista com as multiplicações: ")
    novaLista = []
    for num in listaNum:
        multi = num * 2
        novaLista.append(multi)
    for i in novaLista:
        print(i, end=", ")


if __name__ == "__main__":
    main()
