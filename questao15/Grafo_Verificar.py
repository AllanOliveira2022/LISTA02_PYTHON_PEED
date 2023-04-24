def main():
    grafo = {}
    vertices = input('Digite os vértices do grafo separados por espaço: ').split()

    for chave in vertices:
        grafo[chave] = []
    num_aresta = int(input("Quantas arestas vai ter o grafo: "))
    for i in range(0,num_aresta):
        partida, chegada = input('Digite os vértices da aresta separados por espaço : ').split()
        
        grafo[partida].append(chegada)
        grafo[chegada].append(partida)



    print("Grafo montado: ")
    for v in grafo:
        print(v, '->', grafo[v])
        
    if 'C' in grafo['A']:
        print('A aresta (A, C) está presente no grafo')
    else:
        print('A aresta (A, C) NÃO está presente no grafo')
if __name__ == "__main__":
    main()
