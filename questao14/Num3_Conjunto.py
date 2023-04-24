def main():
    numeros = set()
    print("Digite os 3 números do conjunto: ")
    for i in range(0,3):
        num = int(input(f"Número {i+1}: "))
        numeros.add(num)
        
    if 3 in numeros:
        print("O número '3' EXISTE !")
    if 3 not in numeros:
        print("O número '3' NÃO existe!")    
    print("veja o conjunto: ")
    print(numeros, end=", ")

if __name__ == "__main__":
    main()
