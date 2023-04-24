def main():
    conjunto = set()
    contador = 0
    print("Digite os números no conjunto: ")
    for contador in range(0, 5):
        num = int(input("Digite um número: "))
        conjunto.add(num)
        contador += 1
    print("Números digitados: ")
    print(conjunto)
    print(f"Você digitou '{contador}' números")


if __name__ == "__main__":
    main()
