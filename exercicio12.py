"""
Uma possível resolução do exercício 12 do listão, utilizando:

- Apenas variáveis.
- Sem estruturas complexas 
- E nem funções
- Formatação de string com f""
"""

# =================================
# Coleta dos dados
# =================================

print("Exercício 12 - Área do triângulo")

base_str = input("Informe a base do triângulo: ")
altura_str = input("Informe a altura do triângulo: ")

# =================================
# Ajuste do dado
# =================================

base = float(base_str)
altura = float(altura_str)

# =================================
# Calculando a área
# =================================

# Aqui precisa de parânteses no cálculo da área?
area_triangulo = base * altura / 2

# =================================
# Informando área com duas casas
# decimais.
# =================================

print(f"A área deste triângulo é {area_triangulo:0.2f}.")