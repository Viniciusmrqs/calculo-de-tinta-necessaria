larg1 = float(input('digite a largura da parede 1: '))
alt = float(input("digite a altura das paredes: "))
larg2 = float(input('digite a largura da parede 2: '))


larg_p = float(input('digite a largura da porta: '))
alt_p = float(input('digite a altura da porta: '))

larg_j = float(input('digite a largura da janela: '))
alt_j = float(input('Digite a altura da janela: '))

area = (((larg1*alt)*2)+((larg2*alt)*2))-((larg_p*alt_p)+(larg_j+alt_j))

print ('A área total das paredes é {}m²'.format(area))


vol = float (input('Digite o volume da lata: '))
rend = float (input('Digite o rendimento: '))
demao = float (input('Digite a quantidade de demãos: '))
litro =rend/vol
uso = area*demao/litro
print('A quantidade necessaria de tinta é {}L'.format(uso))
#uso = area*demao/(vol/rend)
#print('a quantidade de tinta necessaria para pintar a área de {}m² é {}L'.format(area,uso))