'''Desenvolver uma aplicação em Python que implemente uma classe representando um
personagem em um jogo de RPG
Os dados do jogador consistem em:
• Nome do Jogador
• Classe (Guerreiro ou Mago)
• HP inicial: 200 se guerreiro; 100 se mago.
• Mana inicial: 100 se guerreiro, 200 se mago.
• Nível: 1
• XP atual: 0
• XP para próximo nível: 100''' 
class Personagem():
    maxHp = 250
    def __init__(self,lvl,xpAtual,proximo,hp,mp,nome):#constructor
        self.lvl = lvl
        self.xpatual = xpAtual
        self.xpProximolvl= proximo
        self.hp =hp
        self.mp= mp
        self.nome = nome
        
           
    #metodos da classe
    def addHp(self,valor):
        if self.hp+valor < self.maxHp:
            self.hp+=valor

    def subHp(self,valor):
        self.hp-=valor 
    def __repr__(self):
        return "Nome : "+self.nome+"\nLevel : "+str(self.lvl)+"\nHP : "+str(self.hp)+"\nMP : "+str(self.mp)+"\nXP : "+str(self.xpatual)+"\nXp Proximo lvl:"+str(self.xpProximolvl)
    def upar(self):
        self.lvl = self.lvl + 1 
    def ganharXP(self):
        self.xpatual = self.xpatual+50
        print("Xp ATUAL",self.xpatual)
        if self.xpatual >= self.xpProximolvl:
            self.upar()
            self.xpProximolvl= self.xpProximolvl*2   
        print("Xp para upar",self.xpProximolvl)    
class Warrior(Personagem):
    
    def __init__(self,nome):
        super().__init__(lvl=1,xpAtual =0,proximo=100,hp=200,mp=100,nome=nome)
    '''• Caso seja guerreiro, cada ataque do jogador causa 5 + 5 * nível e gasta 10 de
         mana. O nome do ataque é “Espada Flamenjante”
       '''
    def atacar(self):
        if self.mp !=0 :
            dps = 5+5*int(self.lvl)
            msg = "Warrior "+self.nome+" utiliza o ataque Espada flamejante e causa "
            self.mp = self.mp-10
            return msg+str(dps)+" pts de dano"
        else:
            msg = "Sem mana"
            return msg

class Mage(Personagem):
   # • Caso seja mago, cada ataque do jogador causa 10 + 10 * nível e gasta 20 de mana.
   #O nome do ataque é “Bola de Fogo”.
    def atacar(self):
        if self.mp !=0 :
            dps = 10+10*int(self.lvl)
            msg = "Mage "+self.nome+" utiliza o ataque Bola de fogo e causa "
            self.mp = self.mp-20
            return msg+str(dps)+" pts de dano"
        else:
            msg = "Sem mana"
            return msg

    def __init__(self,nome):
       super().__init__(lvl=1,xpAtual =0,proximo=100,hp=100,mp=200,nome=nome)
   



j1 =  Warrior("Jão Reluzente") 

j2 =  Mage("Ze do Oso")  
print(j2)
print("mp antes",j2.mp)
print(j2.atacar())
print(j2.atacar())
print("antes lvl",j2.lvl)
j2.upar()
print("upou")
print("depois lvl",j2.lvl)
j2.ganharXP()
j2.ganharXP()
j2.ganharXP()
print("depois lvl",j2.lvl)
print("mp depois",j2.mp)
print(j2)
print("=-="*20)
print(j1) 
print("mp antes",j1.mp)
print(j1.atacar())
print(j1.atacar())
print("antes lvl",j1.lvl)
j1.upar()
print("upou")
print("depois lvl",j1.lvl)
j1.ganharXP()
j1.ganharXP()
j1.ganharXP()
print("depois lvl",j1.lvl)
print("mp depois",j1.mp)
print(j1)







'''
• Caso seja guerreiro, cada ataque do jogador causa 5 + 5 * nível e gasta 10 de
mana. O nome do ataque é “Espada Flamenjante”
• Caso seja mago, cada ataque do jogador causa 10 + 10 * nível e gasta 20 de mana.
O nome do ataque é “Bola de Fogo”.
• O nível sobe na seguinte progressão:
o Se XP para próximo nível >= XP atual:
▪ Nivel = Nivel + 1
▪ XP para próximo nível = XP para próximo nível x 2
A classe deve implementar a função de atribuir XP, que deverá calcular
automaticamente se o nível do personagem aumenta.
Toda vez que for usado um ataque, exibir a mensagem:
“Guerreiro/Mago usou <Nome do ataque, dependendo da classe> e causou <x> de
dano”.
Caso o personagem não tenha mais mana, exibir “O Guerreiro/Mago está esgotado”.
Você pode usar herança, caso tenha compreendido o conceito. Senão o problema pode
ser resolvido com condicionais.'''

