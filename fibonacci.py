def pertence_a_fibonacci(numero):
    # Inicializa os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Verifica se o número informado é um dos dois primeiros
    if numero == a or numero == b:
        return True

    # Gera a sequência de Fibonacci até que o valor gerado seja maior ou igual ao número informado
    while b < numero:
        # Atualiza os valores de 'a' e 'b' para o próximo par na sequência
        a, b = b, a + b

    # Retorna True se o número informado for encontrado na sequência
    return b == numero

# Defina o número a ser verificado, pode mudar o valor
numero = 144  

# Chama a função e armazena o resultado
resultado = pertence_a_fibonacci(numero)

# Imprimir resultado:
if resultado:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
