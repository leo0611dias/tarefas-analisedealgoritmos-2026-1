def F(n):
    """
    Função recursiva que calcula F(n) = 2F(n-1) + n²
    Caso base: F(1) = 2
    """
    if n == 1:
        return 2
    else:
        return 2 * F(n - 1) + n ** 2

def main():
    try:
        # Solicita o valor de n ao usuário
        n = int(input("Digite o valor de n: "))
        
        # Verifica se n é válido (maior ou igual a 1)
        if n < 1:
            print("Erro: n deve ser maior ou igual a 1")
        else:
            # Calcula e exibe o resultado
            resultado = F(n)
            print(f"F({n}) = {resultado}")
            
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")

# Executa o programa
if __name__ == "__main__":
    main()
