"""
Uma possível resolução do exercício 13 do listão, utilizando:

- Apenas variáveis.
- Com listas
- Laço de repetição: while
- Função interna: sum() e len()
- Formatação de string com f""
"""

# =================================
# Variáveis globais
# (É verdade que neste script todas
# as variáveis são globais)
# =================================

# Total de pessoas para coletar as idades
TOTAL_PESSOAS = 3

# =================================
# Coleta dos dados
# =================================

print("Exercício 13 - Média idades")

# Lista que conterá a idade de cada pessoa
idades_pessoas = []
# Número da pessoa 'atual'
numero_pessoa = 1
while numero_pessoa <= TOTAL_PESSOAS:
    idade_atual_str = input(f"Informe a idade da {numero_pessoa}ª pessoa: ")
    idade_atual = int(idade_atual_str)
    # 'Guardando' a idade atual
    idades_pessoas.append(idade_atual)
    # 'Passando' para a próxima pessoa
    numero_pessoa += 1

# =================================
# Calculando a média
# =================================

media_idades = sum(idades_pessoas) / TOTAL_PESSOAS

# =================================
# Mostrando a média
# =================================

print(f"A média das idades é {media_idades:0.2f}.")