"""
Uma possível solução para o exercício 18 utilizando:

- Funções 
- Laços de repetição: while

"""

# =================================
# Variáveis globais
# =================================

# Menor nota que um aluno pode tirar.
MENOR_NOTA = 0
# Maior nota que um aluno pode tirar.
MAIOR_NOTA = 100

# =================================
# Funções do script
# =================================


def coletar_nota():
    # Validação da nota
    eh_valida_nota = False
    while not eh_valida_nota:
        nota_str = input("Qual é a nota do aluno? ")
        nota = float(nota_str)
        eh_valida_nota = MENOR_NOTA <= nota <= MAIOR_NOTA
        if not eh_valida_nota:
            print(
                "\nNota inválida! A nota deve ser entre "
                f"{MENOR_NOTA} e {MAIOR_NOTA}.")
    return nota


def informar_resultado_aluno(nota):
    if nota > 60:
        print("A pessoa foi aprovada!")
    else:
        print("A pessoa foi reprovada!")


def principal():
    nota = coletar_nota()
    informar_resultado_aluno(nota)


# =================================
# 'Corpo' do script
# =================================

principal()
