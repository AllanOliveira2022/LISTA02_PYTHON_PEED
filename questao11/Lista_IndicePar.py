def main():
    lista_num = []

    print("Digite os 10 números da lista: ")
    for i in range(0, 10):
        lista_num.append(int(input(f"Número {i+1}: ")))
    print("Números com o índice par: ")
    for i in range(0,10):
        if i % 2 != 0:
            print(lista_num[i], end=", ")
        

if __name__ == "__main__":
    main() 
