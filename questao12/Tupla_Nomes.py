def main():
    nomes = ()
    lista_nomes = []
    print("Digite os 3 nomes para a tupla: ")
    for i in range(0, 3):
        lista_nomes.append(str(input(f"Nome {i +1}: ")))

    nomes = tuple(lista_nomes)
    if 'Maria' in nomes:
        print("O nome 'Maria' está na tupla !")
    if 'Maria' not in nomes:
        print("'maria' não está na tupla !")
    
    print("Veja a tupla: ")
    print(nomes, end=", ")
    print("")


if __name__ == "__main__":
    main()
