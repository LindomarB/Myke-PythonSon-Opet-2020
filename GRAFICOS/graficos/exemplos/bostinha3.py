
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1,2,3,4],[10,45,20,35],label='can1') 
ax.plot([1,2,3,4],[10,30,25,44],label='can2') 
ax.plot([1,2,3,4],[55,50,57,60],label='can3')
ax.set_xlabel('dia da pesquisa')#nome da label horizontal
ax.set_ylabel('intewnçao de voto')#nome da label vertical
ax.set_title('Corrida pelo roubo municipal')#titulo
ax.legend()


plt.show()    