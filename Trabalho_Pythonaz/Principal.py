from produtos import Produto
from datetime import datetime
p=[]
x = 1
while x !=0:
    nome = input("Digite o nome do Produto : ")
    lote = int(input("Digite o lote : "))
    qntLote =input("Quantidade do lote : ")
    print("Data de fabricaçao")
    dia = int(input("Informe o dia de fabricação : "))
    mes = int(input("Informe o mes de fabricação : "))
    ano = int(input("Informe o ano de fabricação : "))
    dataFabricacao = datetime(ano,mes,dia)
    validade =int(input("Qual a quantides de dias de validade do produto : "))
    tipo =input("Digite o tipo de produto comida/bebida/outros: ")
    expira = ""
    p.append(Produto(nome,lote,qntLote,dataFabricacao,validade,tipo,expira))
    x= int(input("Deseja continuar? 1 para sim 0 para sair"))
print("=-="*20)  
escolha = int(input("O que voce deseja fazer?\n1: Consultar um produto pelo número do lote.\n2: Consultar os produtos dentro de um intervalo da data de fabricação.\n3: Consultar os produtos que não expiraram.\n4: Consultar os produtos expirados.\n5: Adicionar outro produto.\n0: Sair e exibir Autores \n"))
while escolha !=0:
    if escolha ==1:
        procuralote= int(input("qual o lote do produto: "))
        for i in range (len(p)):
            if procuralote == p[i].lote:
                print(p[i].pesquisaLote(procuralote))

        escolha = int(input("O que voce deseja fazer?\n1: Consultar um produto pelo número do lote.\n2: Consultar os produtos dentro de um intervalo da data de fabricação.\n3: Consultar os produtos que não expiraram.\n4: Consultar os produtos expirados.\n5: Adicionar outro produto.\n0: Sair e exibir Autores \n"))
   
   
    if escolha ==2 :
        print("digite a primeira data")
        dia = int(input("informe o dia da primeira data : "))
        mes = int(input("informe o mes da primeira data : "))
        ano = int(input("informe o ano da primeira data : "))
        data1 = datetime(ano,mes,dia)
        print("digite a primeira data")
        dia = int(input("informe o dia da segunda data : "))
        mes = int(input("informe o mes da segunda data : "))
        ano = int(input("informe o ano da segunda data : "))
        data2 = datetime(ano,mes,dia)
        for c in range(len(p)):
            print(p[c].pesquisaDataFabricaçao(data1,data2))
        escolha = int(input("O que voce deseja fazer?\n1: Consultar um produto pelo número do lote.\n2: Consultar os produtos dentro de um intervalo da data de fabricação.\n3: Consultar os produtos que não expiraram.\n4: Consultar os produtos expirados.\n5: Adicionar outro produto.\n0: Sair e exibir Autores \n"))
   
    if escolha == 3 :
        print("-=-=-=-=Produtos no prazo de validade=-=-=-=")
        for c in range(len(p)):
            if p[c].vencido == False:
                print(p[c].produtosNaoexpirados()) 
        print("-="*20)          
        escolha = int(input("O que voce deseja fazer?\n1: Consultar um produto pelo número do lote.\n2: Consultar os produtos dentro de um intervalo da data de fabricação.\n3: Consultar os produtos que não expiraram.\n4: Consultar os produtos expirados.\n5: Adicionar outro produto.\n0: Sair e exibir Autores \n"))
    if escolha == 4 :
        print("-=-=-=-=Produtos fora do prazo de validade=-=-=-=")
        for c in range(len(p)):
            if p[c].vencido == True:
                print(p[c].produtosNaoexpirados()) 
        print("-="*20)          
        escolha = int(input("O que voce deseja fazer?\n1: Consultar um produto pelo número do lote.\n2: Consultar os produtos dentro de um intervalo da data de fabricação.\n3: Consultar os produtos que não expiraram.\n4: Consultar os produtos expirados.\n5: Adicionar outro produto.\n0: Sair e exibir Autores \n"))
    if escolha == 5:
        nome = input("Digite o nome do Produto : ")
        lote = int(input("Digite o lote : "))
        qntLote =input("Quantidade do lote : ")
        print("Data de fabricaçao")
        dia = int(input("Informe o dia de fabricação : "))
        mes = int(input("Informe o mes de fabricação : "))
        ano = int(input("Informe o ano de fabricação : "))
        dataFabricacao = datetime(ano,mes,dia)
        validade =int(input("Qual a quantides de dias de validade do produto : "))
        tipo =input("Digite o tipo de produto comida/bebida/outros: ")
        expira = ""
        p.append(Produto(nome,lote,qntLote,dataFabricacao,validade,tipo,expira))
        escolha = int(input("O que voce deseja fazer?\n1: Consultar um produto pelo número do lote.\n2: Consultar os produtos dentro de um intervalo da data de fabricação.\n3: Consultar os produtos que não expiraram.\n4: Consultar os produtos expirados.\n5: Adicionar outro produto.\n0: Sair e exibir Autores \n"))
print("Lindomar Bassetti 120-1900-046\nMayara Dourada 120-1900-082")
'''O usuário poderá:
• Salvar um novo produto.
•1 Consultar um produto pelo número do lote.
•2Consultar os produtos dentro de um intervalo da data de fabricação.
•3 Consultar os produtos que não expiraram.
•4 Consultar os produtos que já expiraram.
O produto deve ser armazenado utilizando uma classe. Deverão ser criadas funções de acordo
com a necessidade avaliada pela equipe. Poderá ser utilizado qualquer tópico dos conteúdos já
vistos nas aulas.
O trabalho pode ser feito individualmente, em grupos de dois ou três integrantes. Deverá ser
entregue um zip com os códigos em Python do sistema e o nome de todos os integrantes.'''