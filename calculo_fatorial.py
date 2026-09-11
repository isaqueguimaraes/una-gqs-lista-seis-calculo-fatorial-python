def calcular(numero: int) -> int:
    """Calcula o fatorial de um número inteiro utilizando um loop for."""
    resultado = 1  # Começa em 1 porque estamos multiplicando
    
    # Loop que vai de 1 até o número escolhido
    for i in range(1, numero + 1):
        resultado *= i  # Multiplica o resultado pelo número atual
        
    return resultado

if __name__ == "__main__":
    numero_escolhido = 5
    valor_final = calcular(numero_escolhido)
    print(f"O fatorial de {numero_escolhido} é: {valor_final}")