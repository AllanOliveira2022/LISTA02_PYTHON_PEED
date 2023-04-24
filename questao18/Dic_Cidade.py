def main():
    dicionario = {}
    print("Digite os valores do dicionário: (Chave - valor)")
    for i in range(0, 2):
        dicionario.update({input(f"Digite a chave {i+1}:")
                          : input(f"Digite o valor {i+1}: ")})

    print("Agora digite a sua cidade onde nasceu para atualizar o dicionário: ")
    dicionario.update({"Cidade": input("Digite a cidade: ")})

    print(dicionario)


if __name__ == "__main__":
    main()
