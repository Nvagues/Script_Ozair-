"""
Uma possível solução para o exercício 19 utilizando:

- Funções 
- Condicionais com if.

"""


# =================================
# Funções do script
# =================================


def calcular_comissao(valor_venda):
    if valor_venda < 1000:
        percentual_comissao = 0
    elif valor_venda < 5000:
        percentual_comissao = 0.1
    elif valor_venda < 10000:
        percentual_comissao = 0.2
    elif valor_venda < 50000:
        percentual_comissao = 0.25
    else:
        percentual_comissao = 0.3

    valor_comissao = valor_venda * percentual_comissao

    return valor_comissao


def coletar_valor_venda():
    valor_venda_str = input("Qual é o valor da venda? ")
    return float(valor_venda_str)


def informar_valor_comissao(valor_comissao):
    if valor_comissao == 0:
        print("Não há comissão para esta venda")
    else:
        print(
            f"O valor da comissão será $ {valor_comissao:0.2f}.")


def principal():
    valor_venda = coletar_valor_venda()
    valor_comissao = calcular_comissao(valor_venda)
    informar_valor_comissao(valor_comissao)


# =================================
# 'Corpo' do script
# =================================

principal()
