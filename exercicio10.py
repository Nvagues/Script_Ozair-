"""
Uma possível resolução do exercício 10 do listão, utilizando:

- Apenas variáveis.
- Sem estruturas complexas 
- E nem funções
- Formatação de string com f""
"""

# =================================
# Coleta dos dados
# =================================

print("Exercício 10")

nome = input("Qual é o seu nome? ")
cidade = input("Em qual cidade você nasceu? ")
ano_str = input("Em que ano você nasceu? ")

# =================================
# Ajuste de alguns dados ('Perfurmaria')
# =================================

nome = nome.strip()
cidade = cidade.strip()
ano = int(ano_str)

# =================================
# Mostrando os dados coletados com
# mensagens amigáveis ;-) 
# =================================

print(f"Olá {nome}!")
print(f"Você nasceu em {cidade}.")
print(f"{ano} foi o ano que você nasceu.")

# =================================
# Informar idade em 2030
# =================================

idade_em_2030 = 2030 - ano
print(f"Torcemos que em 2030 você terá {idade_em_2030} anos!")
