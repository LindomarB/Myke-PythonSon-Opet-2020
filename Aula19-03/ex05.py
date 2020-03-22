''' Uma lanchonete possui a seguinte tabela de valores:
ID  Produto     Valor Unitário
1   Sanduiche   5,00
2   Pastel      4,00
3   Refri       3,00
4   Suco        3,50
5   Água        2,00
Criar uma função que recebe como parâmetros duas listas de mesmo tamanho e um
booleano. A primeira lista é composta dos ID’s dos produtos consumidos pelo cliente e
a segunda lista possui a quantidade de produtos consumidos pelo cliente, o booleano
indica se a pessoa pagará os 10% da taxa de serviço, que deverá ter como valor padrão
False se o parâmetro não for informado. A função deve retornar o total gasto pela
pessoa.'''

itemId=[]
itemQntd=[]
res=1
while res!=0:
    itemId.append(int(input(" Qual item deseja adicionar ao seu pedido 1-5 ? \nID  Produto     Valor Unitário\n1   Sanduiche   5,00\n2   Pastel      4,00\n3   Refri       3,00\n4   Suco        3,50\n5   Água        2,00\n itemID :  ")))
    itemQntd.append(int(input("Quantidade de produtos ?:  ")))
    res=int(input("deseja continuar adicionado produtos ao seu pedido?: 0 para sair: "))
desconto = input("deseja pagar a gorjeta ?: S/N :  ").upper()
desconto = True if desconto =="S" else False     


def comanda(itemid, itemqntd, desc=False): 
    total=0
    for c in range (0,len(itemqntd)):
        if itemid[c]==1:
            itemqntd[c]= itemqntd[c]*5.00
            total= total+itemqntd[c]
            print("Sanduba:",itemqntd[c])    
        elif itemid[c]==2:
            itemqntd[c]= itemqntd[c]*4.0
            total= total+itemqntd[c]
            print("Patel: ",itemqntd[c])
        elif itemid[c]==3:
            itemqntd[c]= itemqntd[c]*3.0
            total= total+itemqntd[c]
            print("CocaColaPapai: ",itemqntd[c])
        elif itemid[c]==4:
            itemqntd[c]= itemqntd[c]*3.5
            total= total+itemqntd[c]
            print("AÇuco: ",itemqntd[c])     
        elif itemid[c]==5:
            itemqntd[c]= itemqntd[c]*2.0
            total= total+itemqntd[c]
            print("apumApum: ",itemqntd[c]) 
    if desc == True:
        total = total + ((total*10)/100)         
        return total
    else:
        return total

    
   
print("Total da Compra R$:  ",comanda(itemId,itemQntd,desconto))



