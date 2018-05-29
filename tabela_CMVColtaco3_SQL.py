#! /usr/bin/env/ python
import string

arquivo = open('taco_CMVCol.csv','r')
arquivoSQL =open('insert_CMVColtaco3.sql','wr')
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
   dados="INSERT INTO CMVColtaco3 (id, categoria, numeroAlimento, descricaoAlimento, umidade, energiaKcal, energiaKj, proteina, lipideos, colesterol, carboidrato, fibraAlimentar, cinzas, calcio, magnesio, manganes, fosforo, ferro, sodio, potassio, cobre, zinco, retinol, re, rae, tiamina, riboflavina, piridoxina, niacina, vitaminaC, created_at, updated_at) VALUES (''"
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
