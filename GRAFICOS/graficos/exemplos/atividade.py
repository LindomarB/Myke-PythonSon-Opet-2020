'''Lindomar bassetti

Sua empresa foi contratada para medir o alcance de três produtos (Produto X, Produto Y e Produto Z) 
no periodo de 6 meses. Para isto, sua equipe precisa desenvolver um programa em Python que, para cada mês
leia a opinião de 50 pessoas. Cada pessoa pode escolher 1 dos 3 produtos citados como preferido.
 Ao final desta votação, você deve gerar o gráfico que mostra a aceitação deste produto no periodo citado.
O gráfico deve possuir um titulo, rótulos nos eixos X e Y, 
além de uma legenda indicando qual linha pertence a cada um dos produtos.
Os dados devem ser lidos pelo teclado. Pode-se utilizar dados pré-registrados para teste, 
porém o programa deve ser completamente funcional sem tais dados.
Pode ser feito em duplas. Enviar o Script em Python e
 adicionar o nome da dupla como comentário na primeira linha do código.'''
import matplotlib.pyplot as plt
import random
print("shit")



pesquisa1=[]
pesquisa2=[]
pesquisa3=[]
produtox=0
produtoy=0
produtoz=0
meses=['jan','fev','mar','abr','mai','jun']
escolha = 1
for mes in meses:
    print("fazendo perquisa do mes de :",mes)
    for i in range(50):
        #produto = random.randint(1,3)
            produto = int(input("digite valor de 1 a 3: "))
            if produto ==1:
                produtox = produtox + 1
            if produto ==2:
                produtoy = produtoy + 1
            if produto ==3:
                produtoz = produtoz + 1     
    pesquisa1.append(produtox)
    produtox=0
    pesquisa2.append(produtoy)
    produtoy =0
    pesquisa3.append(produtoz)
    produtoz=0
   
    
        
        
        
               
print("X:",produtox,"Y: ",produtoy,"Z: ",produtoz)  

             


fig, ax = plt.subplots()
ax.plot(["jan","fev","mar","abr","mai","jun"],[pesquisa1[0],pesquisa1[1],pesquisa1[2],pesquisa1[3],pesquisa1[4],pesquisa1[5]],label='produto X',marker='o',color='green',linestyle='solid') 
ax.plot(["jan","fev","mar","abr","mai","jun"],[pesquisa2[0],pesquisa2[1],pesquisa2[2],pesquisa2[3],pesquisa2[4],pesquisa2[5]],label='produto Y',marker='o',color='red',linestyle='solid')
ax.plot(["jan","fev","mar","abr","mai","jun"],[pesquisa3[0],pesquisa3[1],pesquisa3[2],pesquisa3[3],pesquisa3[4],pesquisa3[5]],label='produto Z',marker='o',color='blue',linestyle='solid')
ax.set_xlabel('mes da pesquisa')#nome da label horizontal
ax.set_ylabel('taxa aceitaçao')#nome da label vertical
ax.set_title('Pesquisa de aceitação ')#titulo
ax.legend()
plt.show()  