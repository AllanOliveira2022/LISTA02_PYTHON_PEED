def main():
    dicionario = {} 
    print("Digite as chaves e valores para o dicionário: ")
    for i in range(0,2):
        dicionario.update({input("Digite a chave do dicionario: ") : input("Digite o valor dessa chave: ")})
    
    if 'Profissão' in dicionario.keys():
        print("A chave 'Profissão' existe no dicionário !")
    if 'Profissão' not in dicionario.keys():
        print("'Profissão' NÃO  existe no dicionário !")    
        
    print("Veja o dicionário: ")
    print(dicionario)    
    
if __name__ == "__main__":
    main()
