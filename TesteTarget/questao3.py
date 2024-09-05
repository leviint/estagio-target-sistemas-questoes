# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
# faça um programa, na linguagem que desejar, que calcule e retorne: 
# • O menor valor de faturamento ocorrido em um dia do mês; 
# • O maior valor de faturamento ocorrido em um dia do mês; 
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

with open('dados.json', 'r') as file: #aqui abre o json no modo leitura
    dados = json.load(file)

valores_dia = [item['valor'] for item in dados]

menor_faturamento = min(valores_dia)
maior_faturamento = max(valores_dia)

media_mensal = sum(valores_dia) / len(valores_dia) #Divide a soma de todos os valores com a quantidade de valores

dias_acima_media = sum(1 for valor in valores_dia if valor > media_mensal) #soma um dia para cada valor que esteja acima da média

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")

#Arthur Lemos Bendini
