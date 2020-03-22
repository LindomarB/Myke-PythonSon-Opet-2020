'''Criar uma função que recebe como parâmetro dois inteiros e retorna uma String com a
junção destes inteiros; Exemplo: 50 e 30 retorna 5030.'''
def junta(a,b):
    c = str(a)
    d = str(b)
    return c+d

n1 = input("Digite um numero inteiro: ")

n2 = input("Digite outro numero inteiro: ")
print(junta(n1,n2))
