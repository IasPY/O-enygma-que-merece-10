dicionario = {
'6' : 'f',
'5' : 'e',
'50' : 'l',
'1' : 'i',
'26' : 'z',
'mm' : '2000',
'r' : '18',}
chave_procurada1 = '6'
chave_procurada2 = '5'
chave_procurada3 = '50'
chave_procurada4 = '1'
chave_procurada5 = '26'
chave_procurada6 = 'mm'
chave_procurada7 = 'r'
p = '6550126mmr'
print("mensagem codificada é:",p)
if chave_procurada1 in dicionario:
    valor_procurado1 = dicionario[chave_procurada1]
if chave_procurada2 in dicionario:
 valor_procurado2 = dicionario[chave_procurada2]
if chave_procurada3 in dicionario:
 valor_procurado3 = dicionario[chave_procurada3]  
if chave_procurada4 in dicionario:
 valor_procurado4 = dicionario[chave_procurada4]
if chave_procurada5 in dicionario:
 valor_procurado5 = dicionario[chave_procurada5]
if chave_procurada6 in dicionario:
 valor_procurado6 = dicionario[chave_procurada6]
if chave_procurada7 in dicionario:
 valor_procurado7 = dicionario[chave_procurada7]
troca1 = valor_procurado6.replace('2000', ' 20')
pre_juntar = (valor_procurado1, valor_procurado2, valor_procurado3, valor_procurado4, valor_procurado5, troca1, valor_procurado7)
juntado = ''.join(pre_juntar)
print("mensagem decodificada é:",juntado)
#código supremo do Isaias 2B