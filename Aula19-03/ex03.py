'''Criar uma função que receba como parâmetro uma lista com o salário pago para os
funcionários de uma empresa. A função deve retornar o maior e menor salário, além
da média e soma dos salários.'''


salario = []
res = 1
cont =0
while res!=0:
  salario.append(int(input('digite o salario do {}° funcionario: '.format(cont+1))))
  cont+=1
  res= int(input("add salario de funcionario? 0 para sair"))
print("tamanho da lista",len(salario))
print("lista",salario)
def calcula(sal):
    maior = 0
    menor = 999
    soma = 0
    for c in range(0,len(sal)):
        if sal[c] > maior:
            maior = sal[c]
        if sal[c]< menor:
            menor = sal[c]
        soma = soma+sal[c]
        media = soma/len(sal)

    return maior,menor,soma,media,        
print("maior :", calcula(salario)[0])
print("menor :", calcula(salario)[1])
print("soma  :", calcula(salario)[2])
print("media :", calcula(salario)[3])








    





  
