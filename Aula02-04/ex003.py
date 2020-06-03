'''Criar um programa que a partir da data atual e do numero de dias, 
que é fornecidos pelo usuário, indique se a nova data cairá em um fim de semana.'''
import datetime
import locale
locale.setlocale(locale.LC_TIME,"pt_BR")

def diaSemana(dia):
    if dia==0:
        print("segunda e dia de semana vai trabalhar ")
    if dia == 1:
        print("terça e dia de semana bora trabalhar") 
    if dia == 2: 
        print("quarta e dia de semana so falta 2 dias para sabado") 
    if dia == 3: 
        print("quinta e dia de semana volta a labuta") 
    if dia== 4: 
        print("sexta e dia de semana porem SEXTOU") 
    if dia == 5: 
        print("sabado é FINAL DE SEMANA") 
    if dia == 6: 
        print(" È DOMINGO CUMPADI BORA TOMAR UMA")  
sishora = datetime.datetime.now()
print('Data atual',sishora.strftime("%d/%m/%Y"))

dia = int(sishora.weekday())
diaSemana(dia)



print("="*40)
dias= int(input("Digite o numero de dias para adicionar a data atual : "))
novaData = sishora + datetime.timedelta(days=dias)
print("nova data = ",novaData)
print('Data com acrescimo ',novaData.strftime("%d/%m/%Y"))

dia = int(novaData.weekday())
diaSemana(dia)



   