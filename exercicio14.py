"""
Uma possível resolução do exercício 14.
Nesta versão estendida iremos além de responder 'True' ou 'False,
iremos informar se foi a primeira ou a segunda que é a mais velha,
ou se elas possuem a mesma idade.

O que veremos aqui:

- laço de repetição for
- listas
- condicional if else
- nenhuma função
"""

# =================================
# Variáveis globais
# (É verdade que neste script todas
# as variáveis são globais)
# =================================

# Total de pessoas para coletar as idades
TOTAL_PESSOAS = 2

# =================================
# Coleta dos dados
# =================================

print("Exercício 13 - Pessoa mais velha")

# Lista que conterá a idade de cada pessoa
idades_pessoas = []
for numero_pessoa in range(1, TOTAL_PESSOAS + 1):
    idade_atual_str = input(f"Informe a idade da {numero_pessoa}ª pessoa: ")
    idade_atual = int(idade_atual_str)
    # 'Guardando' a idade atual
    idades_pessoas.append(idade_atual)

# =================================
# Determinando a mais velha
# =================================

idade_primeira_pessoa = idades_pessoas[0]
idade_segunda_pessoa = idades_pessoas[1]

# ordem_mais_velha indentifica quem possui
# a maior idade. Se for zero, então possuem
# a mesma idade.
if idade_primeira_pessoa == idade_segunda_pessoa:
    ordem_mais_velha = 0
elif idade_primeira_pessoa < idade_segunda_pessoa:
    ordem_mais_velha = 2
else:
    ordem_mais_velha = 1

# =================================
# Informando qual é a mais velha
# =================================

if ordem_mais_velha == 0:
    print("As duas pessoas possuem a mesma idade.")
else:
    print(f"A {ordem_mais_velha}ª pessoa é a mais velha.")