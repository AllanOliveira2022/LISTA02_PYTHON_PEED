def main():
    lista_Num = []
    for i in range(0,5):
        lista_Num.append(int(input(f"Digite o {i+1}º número: ")))
    
    print("Números da lista : ")
    for i in lista_Num:
        print(i, end=", ") 
    print("")  
    lista_Num.append(input("Digite mais um número para a lista: ")) 
    print("Números da lista : ")
    for i in lista_Num:
        print(i, end=", ")


if __name__ == "__main__":
    main()