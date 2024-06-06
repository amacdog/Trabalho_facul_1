#Informações Base
matriz=[]
areaUnidade= float(input("Indique o valor de uma unidade de quadrado(em m^2):"))
linhas = int(input("Indique o numero de linhas desejado:"))
colunas = int(input("Indique o numero de colunas desejado:"))

#Criando a matriz base
for i in range(linhas):
    L=[]
    for j in range(colunas):
        L.append(str(input("Indique se há Agua(A) ou oleo(O):")))
    matriz.append(L) 

#Contador e localizador de óleo
QO=0
listaO=[]
for lin in range(linhas):
    for col in range(colunas):
      t= matriz[lin][col]
      if t=='O':
        QO+=1
        listaO.append(str(lin+1) + ':' + str(col+1))


#Impressão final
O = QO * areaUnidade
T = linhas * colunas * areaUnidade
for linha in matriz:
    print(' '.join(linha))
print(f'Area total:{T}m^2')
print(f'Area total de oleo:{O}m^2')
if len(listaO) == 0:
  print('Nao há manchas de óleo')
else:
  print('Locais com óleo:',listaO )