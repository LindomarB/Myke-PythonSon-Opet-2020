'''Criar uma função que recebe como parâmetros as medidas de um chão (largura e
profundidade) e o preço do metro quadrado do azulejo. A função deve retornar
quanto a pessoa pagará para colocar lajota em todo o chão''' #Alt+0178 = ²
'''
o Exercicio e muito vago entao estarei utilizando os valores informados no site abaixo somente do azuleijo simples
https://www.cronoshare.com.br/blog/quanto-custa-colocar-azulejo-cozinha/
Taco: R$120,00;
Frio R$20,00;
Cimentício R$60,00;
Laminado R$50,00;
Vinílico R$60,00;
Porcelanato R$45,00;
Azulejo simples R$35,00.
'''
alt = float(input("Informe a altura do azulezo em m²: "))
base = float(input("Informe a base do azulezo   em m²: "))
print(base*alt)

res = int(input("Qual o azuleijo deseja utilizar ? \n[1]Taco: R$120,00;\n[2]Frio R$20,00;\n[3]Cimentício R$60,00;\n[4]Laminado R$50,00;\n[5]Vinílico R$60,00;\n[6]Porcelanato R$45,00;\n[7]Azulejo simples R$35,00. "))
if(res==1):
    print("wtf")
elif(res==2):
    preco = 20.00
elif(res==3):
    preco = 60.00
elif(res==4):
    preco = 50.00
elif(res==5):
    preco = 60.00
elif(res==6):
    preco = 45.00
elif(res==7):
    preco = 35.00
else:
 print('\033[31m'+'ERRO DIGITE UM NUMERO DE 1 A 7'+'\033[0;0m')  
 res = int(input("Qual o azuleijo deseja utilizar ? \n[1]Taco: R$120,00;\n[2]Frio R$20,00;\n[3]Cimentício R$60,00;\n[4]Laminado R$50,00;\n[5]Vinílico R$60,00;\n[6]Porcelanato R$45,00;\n[7]Azulejo simples R$35,00. ")) 
 
def calcula(height,widthd,price):
    return (height*widthd)*price

print('total da compra \033[1;42m',calcula(alt,base,preco),'\033[0;0m')                                
    
      