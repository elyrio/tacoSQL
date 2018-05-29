#! /usr/bin/env/ python
import string

arquivo = open('taco_AG.csv','r')
arquivoSQL =open('insert_AGtaco3.sql','wr')
conteudo=arquivo.readlines()

tamanhoLista= len(conteudo)
print 'tamanho da lista: ',tamanhoLista
i=0
for item in conteudo:
    item=item.strip()
    #print item

listaSQL = []
for item in conteudo:
   item.replace("\n"," ")
   item=item.strip()
   linha=string.split(item,";")
   dados="INSERT INTO AGtaco3 (id, categoria, numeroAlimento, descricaoAlimento, saturados, monoinsaturados, poliinsaturados, 12_0, 14_0, 16_0, 18_0, 20_0, 22_0, 24_0, 14_1, 16_1, 18_1, 20_1, 18_2N_6, 18_3N_3, 20_4, 20_5, 22_5, 22_6, 18_1t, 18_2t, created_at, updated_at) VALUES (''"
   t=0
   while (t < len(linha)):
       dados = dados+",'"+linha[t]+"'"
       t=t+1
   dados = dados+");\n"
   arquivoSQL.writelines(dados)
   i = i + 1
   print 'feito a linha: ', i
print '** FINALIZADO! Favor, verifique o aqruivo. **'
arquivoSQL.close()
arquivo.close()
