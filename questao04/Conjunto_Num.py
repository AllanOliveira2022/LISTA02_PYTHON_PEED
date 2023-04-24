def main():
    numeros = set()
    print("Adicione os valores ao conjunto: ")
    for i in range(0,5):
        valor= int(input(f"Numero {i+1}: "))
        numeros.add(valor)
    print("Valores digitados: ")
    print(numeros, end=", ")    
    print("")

    apagar = int(input("Diga o número que você quer apagar: "))

    if apagar in numeros:
        numeros.remove(apagar)

    print("Valores depois de remover: ")
    print(numeros, end=", ")    
    print("")
if __name__ == "__main__":
    main()