# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado: 
# •	SP – R$67.836,43 
# •	RJ – R$36.678,66 
# •	MG – R$29.229,88 
# •	ES – R$27.165,48 
# •	Outros – R$19.849,53 

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado
#  teve dentro do valor total mensal da distribuidora.

estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "OUTROS": 19849.53
}

TOTAL = sum(estados.values())

def calculo_porcentagem(estado):
    estado_porcentagem = (estados[estado] / TOTAL) * 100
    print(f"{estado}: R${estados[estado]} | {estado_porcentagem:.2f}%") #Pega o nome do estado, seu faturamento e a porcentagem

print(f"Total: R${TOTAL:.2f}")

for estado in estados:
    calculo_porcentagem(estado)


#Arthur Lemos Bendini


