"""
Uma possível resolução do exercício 15 do listão, utilizando:

- Apenas variáveis.
- Formatação de string com f""
"""

# =================================
# Coleta dos dados
# =================================

print("Exercício 13 - 'Racha' conta")

total_pessoas_str = input("Quantos pessoas há na casa? ")
valor_conta_str = input("Qual é o valor do aluguel? ")

# =================================
# Ajustes nos valores
# =================================

total_pessoas = int(total_pessoas_str)
valor_conta = float(valor_conta_str)

# =================================
# Calculando o valor para cada pessoa
# =================================

valor_entre_pessoas = valor_conta / total_pessoas

# =================================
# Mostrando
# =================================

mensagem = f"""
Para um aluguel de $ {valor_conta:0.2f}
entre {total_pessoas} pessoa(s), cada um deverá
pagar uns $ {valor_entre_pessoas:0.2f}.
"""

print(mensagem)