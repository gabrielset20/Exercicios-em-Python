def contar_letra_a(string):
    # Inicializa o contador para a letra 'a' (tanto maiúscula quanto minúscula)
    contador = 0
    
    # Itera por cada caractere da string
    for caractere in string:
        # Verifica se o caractere é 'a' ou 'A' e incrementa o contador se for
        if caractere == 'a' or caractere == 'A':
            contador += 1
    
    # Retorna o contador
    return contador

# Defina a string a ser verificada
string = "A evolução da IA é o próximo passo evolutivo da humanidade" 

# Chamar a função:
quantidade = contar_letra_a(string)

# Imprimr resultado:
if quantidade > 0:
    print(f"A letra 'a' aparece {quantidade} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")
