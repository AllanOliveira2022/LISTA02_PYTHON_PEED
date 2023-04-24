def main():
    dicionario = {}
    print("Adicione os elemento do dicionario (chave - valor): ")
    for i in range(0, 3):
        dicionario.update(
            {input("Digite a chave: "): input("Digite o valor: ")})

    print(dicionario)
    print("Chave 'Idade': ", dicionario['Idade'])


if __name__ == "__main__":
    main()
