'''Criar uma aplicação em Python que simule um controle do lote de um produto de uma empresa.
O controle deve armazenar os seguintes dados:
• Nome do produto
• Número do lote
• Quantidade no lote
• Data da fabricação
• Data de validade (deve somar uma quantidade de dias a partir da data de fabricação)
• Tipo de produto (Bebida, Alimento, etc...)
• Expirado: caso a data de validade esteja ultrapassada.'''
import datetime

class Produto:
    def __init__(self,nome,lote,qntLote,dataFabricacao,validade,tipo,expira):
        self.nome = nome
        self.lote = lote
        self.qntLote =qntLote
        self.dataFabricacao=dataFabricacao
        novaData = self.dataFabricacao + datetime.timedelta(days=validade)
        self.validade = novaData
        self.tipo =tipo
        self.sishora = datetime.datetime.now()
        #self.expira = "Produto Vencido" if self.validade < self.sishora else "produto na validade "
        if self.validade < self.sishora:
            self.expira = "Produto Vencido"
            self.vencido = True
        if self.validade > self.sishora :
            self.expira = "Produto dentro do prazo de validade"
            self.vencido = False
    def __repr__(self):
        return 'nome= {}\nlote= {}\nquantidade = {}\ndata de fabricaçao = {}\nvalidade ={}\ntipo = {}\nexpirado ={}\n'.format(self.nome,self.lote,self.qntLote,self.dataFabricacao.strftime("%d/%m/%Y"),self.validade.strftime("%d/%m/%Y"),self.tipo,self.expira) 


    def pesquisaLote(self,lote):
        if self.lote == lote:
            return self
        else:
            return "nao tem esse produto"   
    def pesquisaDataFabricaçao(self,data1,data2):
        if self.dataFabricacao>=data1 and self.dataFabricacao<=data2:
            return self
        else:
            return "Não ha protudos entre as datas {} e {}".format(data1,data2)    
    def produtosNaoexpirados(self):
        return self    




'''sishora = datetime.datetime.now()
print('Data atual',sishora.strftime("%d/%m/%Y"))


print("=-=")
dias= int(input("Digite o numero de dias para adicionar a data atual : "))
novaData = sishora + datetime.timedelta(days=dias)
print("nova data = ",novaData)
print('Data com acrescimo ',novaData.strftime("%d/%m/%Y"))'''