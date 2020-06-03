import matplotlib.pyplot as plt
import random
l1 =[]
l2=[]
l3 =[]
for i in range (1000):
    l1.append(random.random())
    l2.append(random.random())
    l3.append(random.random())
fig, ax = plt.subplots()
        ####dias##################dados ou %#############
ax.plot([12,13,14,15],[1,2,3,4],marker="o",color='green',linestyle='solid') 
#ax.plot([l1],[l2],marker="o",color='green',linestyle='solid')
#ax.plot([l1],[l3],marker='o',color='red') 
ax.set_xlabel('dia da pesquisa')#nome da label horizontal
ax.set_ylabel('aumento da filhadaputagem')#nome da label vertical




plt.show()    