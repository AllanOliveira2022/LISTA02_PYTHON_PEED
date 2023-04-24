def main():
    nomes = []
    
    for i in range(0,3):
        nomes.append(str(input(f"Digite o {i+1}º nome :")))
    
    nomes_tupla= tuple(nomes) 
    print("Lista de nomes : ")
    for i in nomes_tupla:
        print(i, end=", ")
    print("")    
    pos = int(input("Qual o nome da tupla você deseja alterar? -- informe a posição --"))
    novo_nome = str(input("Digite o novo nome para a tupla: "))

    lista = list(nomes_tupla)
    pos = pos -1
    lista[pos] = novo_nome
    nomes_tupla = tuple(lista)

    print("Lista de nomes editada: ")
    for i in nomes_tupla:
        print(i, end=", ")

if __name__ == "__main__":
    main()