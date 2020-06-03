'''Criar um programa no qual o usuário informe o valor de um angulo em GRAUS 
e possa escolher se deseja exibir o calculo do Seno, Cosseno ou Tangente deste angulo. 
PS: Não se esqueça que os cálculos trigonométricos são feitos em RADIANOS.'''
import math
a = float(input('digite o angulo que voce deseja:'))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('o angulo de {} tem seno de {:.2f}'.format(a, sen))
print('o angulo de {} tem cosseno de {:.2f}'.format(a, cos))
print('o angulo de {} tem tangente de {:.2f}'.format(a, tg))
print('pronto desgraça!!!!!')