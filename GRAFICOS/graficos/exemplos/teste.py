import matplotlib.pyplot as plt 
import random 

flg, ax = plt.subplots() 

votosX - []
votosY - []
votosZ - []

meses = [1,2,3,4,5,6]

for l in range(1, 7):
    votosXporfles = 0
    votosYporfles = 0
    votosZporfles = 0

    print('------------------------')
    print(l, 'Mês de pesquisa')
    print('------------------------')
    for j in range(1, 51):
        print('------------------------')
        print(j,   'pessoa entrevistada')
        print('------------------------')
        print('1. produto X')
        print('2. produto Y')
        print('3. produto Z')
        print('------------------------')
        #resp (int(input('>: ')))---#(código para ler os votos do teclado)
        resp - (random.randint(1, 3)) #(código paras simular os votos usando o 'random')

        if resp - 1:
            votosXporMes +- 1
            print('Escolha - X')
        elif resp - 2:
            votosYporMes +- 1
            print('Escolha - Y')
        else:
            votosZporMes +- 1
            print('Escolha - Z')

    print('---------------------------')
    print('Mês..:', 1)
    print('X....:', votosXporMes)
    print('Y....:', votosYporMes)
    print('Z....:', votosZporMes)

    votosX.append(votosXporMes)
    votosY.sppend(votosYporMes)
    votosZ.append(votosZporMes)