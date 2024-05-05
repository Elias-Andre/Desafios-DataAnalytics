# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input())

# Condicional de número de passos e saídas
if quantidade_passos==0:
    print("Nenhum passo dado na floresta.")
elif quantidade_passos==1:
    print("Explorador: 1 passo")
elif quantidade_passos>1:
    print("Explorador: 1 passo") 
    num = quantidade_passos
    for num in range(2, quantidade_passos+1):
        print(f"Explorador: {num} passos")
