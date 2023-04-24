def main():
    numeros_tupla = ()
    numeros_lista= []
    print("Informe os 5 valores da tupla: ")
    for i in range(0,5):
        numeros_lista.append(int(input(f"Valor {i+1}:")))

    numeros_tupla = tuple(numeros_lista)    

    print("Números da tupla: ")
    print(numeros_tupla)
    print("O primeiro valor da tupla: ", numeros_tupla[0])

if __name__ == "__main__":
    main()