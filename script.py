caixa1= 10
caixa2= 20
caixa3= caixa1+caixa2
print (caixa3)


somar com laço d repetição - Usar o for 

lista = [1,2,3,4,5,6,7,8,9,10] 
soma = 0 
for valor in lista:
soma = soma+valor 
print("Resultado:", soma)

#inicio do bloco ou conjunto de instruções a serem executadors pelo laço 
de repetição. 
#fim do for

#outro jeito de somar:

soma = sum (lista)
print("Resultado por sum():",soma)


#numeros pares 

lista = [1,2,3,4,5,6,7,8,9,10] 

soma = 0 
for valor in lista:
if valor % 2 == 0 :
soma = soma+valor 
print("Resultado:", soma) 

#outra forma 

dicionario (chave e valor) - Caixa com varios compartimentos rotulados


dicionario {}
print("Dicionario vazio:",dicionario)
dicionario = {
1: "Natalia"
2: "Debora"
3: "Juliana"

print("dicionario chaves numericas",dicionario)
print("Chave 3:", dicionario[3])
existe_chave_5 = 5 in dicionario
if existe_chave_5:
print("Chave 5:", dicionario[5])
else:
print("Chave 5 não existe")

#Não existe posição 
ex: catalogando nomes  

get -  

Chave e tipo pode ser do jeito que quiser

funções - organizar, estrutrurar 
Pensa no geral depois da vida aos detalhes 
