"""
Uma possível resolução do exercício 11 do listão, utilizando:

- Apenas variáveis.
- Sem estruturas complexas 
- E nem funções
- Formatação de string com f""
"""

# =================================
# Coleta dos dados
# =================================

print("Exercício 11 - Área do quadrado")

lado_str = input("Informe a medida de um lado do quarado: ")

# =================================
# Ajuste do dado
# =================================

lado = float(lado_str)

# =================================
# Calculando a área
# =================================

area_quadrado = lado ** 2

# =================================
# Informando área com duas casas
# decimais.
# =================================

print(f"A área deste quadrado é {area_quadrado:0.2f}.")