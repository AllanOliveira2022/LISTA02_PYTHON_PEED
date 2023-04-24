def main():
    nomes = ()
    listaNomes = []
    print("Digite os nomes: ")
    for i in range(0, 3):
        listaNomes.append(str(input(f"nome {i+1}: ")))

    nomes = tuple(listaNomes)
    print(f"O nome 'Maria' apareceu {nomes.count('Maria')} vez(es)")
    print("Tupla completa: ")
    print(nomes, end=", ")


if __name__ == "__main__":
    main()
