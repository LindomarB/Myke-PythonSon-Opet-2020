'''Criar uma função que receba como parâmetro uma quantidade qualquer de inteiros. A
função deve retornar a soma do maior inteiro com o menor inteiro. Caso apenas um
inteiro seja passado como parâmetro, o mesmo deve ser retornado. Caso não seja
passado parâmetros para a função, retornar -1.'''



def calcula(*nums):
    maior =0
    menor =0
    for numero in nums:   
        if numero > maior:
            maior = numero
            
        if numero < menor:
            menor = numero
        if numero == maior and numero == menor:
            return numero    
       
    if maior == 0 and menor == 0:
            return -1
    return maior+menor           
#print("SOMA =",calcula(52,21,45,1,25,700))
#print("so um valor ",calcula(5))
print("Sem  valor =",calcula())
        
