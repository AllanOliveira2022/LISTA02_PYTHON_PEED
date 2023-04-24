def main():
    dicionario = {}
    print("Adicione os elemento do dicionario (chave - valor): ")
    chave = input("Digite a chave desse dicionario: ")
    valor= input("Digite o valor dessa chave: ")

    dicionario.update({chave : valor})
    print("veja o dicionario: ")
    print(dicionario)
    print("")

    chave2 = input("digite outra chave para o dicionario: ")
    valor2= input("Digite um valor para essa outra chave: ")
    dicionario.update({chave2: valor2})

    print("veja o dicionario: ")
    print(dicionario)
    print("")


if __name__ == "__main__":
    main()