'''DESAFIO: Seguindo as regras básicas do jogo General
(https://pt.wikipedia.org/wiki/General_(jogo)#Regras_b%C3%A1sicas)
Criar uma função que receba como parâmetro QUATRO valores que representam a
face de cada um dos quatro dados. A função deve retornar uma lista com as 6
possibilidade de jogadas definidas pela regra para o quinto dado, e indicar qual o valor
do quinto dado que maximiza a pontuação para a combinação fornecida.
https://www.youtube.com/watch?v=hsiosOpcf0g'''

''' pensa nessa merda com varias funçoes seu babaca
VERSAO 2'''


from random import randint

def rolarDado(*dados):
    for dado in dados:
       return randint(1,6)
     
jogaDado=int(input("qual dado deseja jogar? "))
dado1=0
dado2=0
dado3=0
dado4=0
dado5=0
dado6=0
if jogaDado ==1:
    dado1 = rolarDado(dado1)
if jogaDado ==2:
    dado2 = rolarDado(dado1)
if jogaDado ==3:
    dado3 = rolarDado(dado1)
if jogaDado ==4:
    dado4 = rolarDado(dado1)
if jogaDado ==5:
    dado5 = rolarDado(dado1)
if jogaDado ==6:
    dado6 = rolarDado(dado6)    
if jogaDado ==7:     
    dado1=rolarDado(dado1) 
    dado2=rolarDado(dado2) 
    dado3=rolarDado(dado3) 
    dado4=rolarDado(dado4) 
    dado5=rolarDado(dado5) 
    dado6=rolarDado(dado6)
print("[dado 1 : {}] [dado 2 : {}] [dado 3 : {}] [dado 4 : {}] [dado 5 : {}] [dado 6 : {}]".format(dado1,dado2,dado3,dado4,dado5,dado6))










'''VERSAO 1
  from random import randint
jogada = 1
while jogada !=0:
    soma = 0
    rejogarDado = 3
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    dado3 = randint(1,6)
    dado4 = randint(1,6)
    dado5 = randint(1,6)
    print('dado1 = {} ,dado2 = {},dado3 = {} ,dado4 = {},dado 5= {}'.format(dado1,dado2,dado3,dado4,dado5))
    
    
    
    resp="S"
    while resp != "N":
        print("voce pode rejogar os dados {} vezes nesta rodada".format(rejogarDado))
        resp=input("Deseja rejogar algum dado?: S/N").upper()
        
        rejogarDado = rejogarDado-1
        if rejogarDado==0:
            print("OPA VOCE NAO PODE MAIS REJOGAR OS DADOS")
            resp = "N"

    
    jogada = int(input("Deseja continuar 0 para sair: "))'''
    
