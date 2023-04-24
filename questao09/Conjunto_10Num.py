def main():
    num = set()
    print("Digite os 10 números para o conjunto: ")
    for i in range(0, 10):
        numeros = int(input(f"Número {i+1}: "))
        num.add(numeros)
    print("Lista dos 10 números: ")
    print(num, end=", ")
    print("")

    lista = list(num)
    for valor in lista:
        if valor % 2 == 0:
            lista.remove(valor)
    num = set(lista)

    print("Lista sem os números pares: ")
    print(num, end=", ")
    print("")


if __name__ == "__main__":
    main()
