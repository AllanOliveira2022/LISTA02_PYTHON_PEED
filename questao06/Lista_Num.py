def main():
    lista = []
    print("Digite 10 números para a lista: ")
    for i in range(0,10):
        lista.append(int(input(f"Número {i+1}: ")))

    print("Lista com os números digitados: ")
    for i in lista:
        print(i, end=", ")    

if __name__ == "__main__":
    main()