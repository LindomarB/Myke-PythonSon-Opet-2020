'''Fornecida uma String de entrada, verificar se esta String é um palindromo. 
Exemplo: ARARA é um palindromo. Converter a String para UPPERCASE e remover pontuação, se houver.
 Exemplo 2: "Socorram-me, subi no ônibus em Marrocos." é um palindromo, 
porém deve-se remover virgulas e pontos para verificar a frase invertida.'''
#Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
        print('e um palindromo')
else:
        print('nao e um palindromo')
print(junto, inverso)
# inverso = junto[::-1] tbm resolve o problema de ler de traz para frente
# utilizando fatiamento de string.