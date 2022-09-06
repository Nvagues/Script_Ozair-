"""
Uma possível solução para o exercício 16 utilizando:

- variáveis

"""

# =================================
# Coleta dos dados
# =================================

print("Exercício 16 - Juros do banco")

valor_emprestimo_str = input("Informe o valor do empréstimo: ")
valor_taxa_str = input("Informe o valor da taxa: ")
valor_tempo_str = input("Informe o tempo em meses: ")

# =================================
# 'Ajuste' dos dados
# =================================

valor_emprestimo = float(valor_emprestimo_str)
taxa = float(valor_taxa_str)
tempo = float(valor_tempo_str)

# =================================
# Cálculo do valor
# =================================

valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)

# =================================
# Apresentando valor final
# =================================

print(f"O valor final será $ {valor_final:0.2f}.")
