import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[10,45,20,35],label='can1') 
plt.plot([1,2,3,4],[10,30,25,44],label='can2') 
plt.plot([1,2,3,4],[55,50,57,60],label='can3')
plt.xlabel('dia da pesquisa')#nome da label horizontal
plt.ylabel('intewnçao de voto')#nome da label vertical
plt.title('Corrida pelo roubo municipal')#titulo
plt.legend()


plt.show()    