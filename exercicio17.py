"""
Uma possível solução para o exercício 17 utilizando:

- variáveis
- condicional if.
"""

# ====================================
# Coleta dos valores
# ====================================

print("17 - Fórmula Bhaskara")
print("Para a equação de segundo grau: ")
print("  ax^2 + bx + c = 0")
print(" Informe os coeficientes: ")

a_str = input("  a: ")
b_str = input("  b: ")
c_str = input("  c: ")

# ====================================
# Ajuste dos valores
# ====================================

a = float(a_str)
b = float(b_str)
c = float(c_str)

# ====================================
# Cálculo das raízes
# ====================================

delta = (b**2) - (4*a*c)
# Delta negativo quer dizer que não tem raizes.
ha_raiz = delta >= 0

if ha_raiz:
    raiz_delta = delta ** .5
    x1 = (-b - raiz_delta) / (2*a)
    x2 = (-b + raiz_delta) / (2*a)

# ====================================
# Apresentando os resultados
# ====================================

if ha_raiz:
    print("As raízes são: ")
    print(f"  - x1 = {x1:0.2f}")
    print(f"  - x2 = {x2:0.2f}")
else:
    print("Não há raizes para esta equação.")