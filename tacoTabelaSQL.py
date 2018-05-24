#! /usr/bin/env/ python
import string

arquivo = open('tacop.csv','r')
arquivoSQL =open('taco.sql','wr')
conteudo=arquivo.readlines()

tamanhoLista= len(conteudo)
print 'tamanho da lista: ',tamanhoLista
i=0
for item in conteudo:
    item=item.strip()
    print item

listaSQL = []
for item in conteudo:
   item.replace("\n"," ")
   item=item.strip()
   linha=string.split(item,"	")
   dados="INSERT INTO CMVColtaco3 (id, descricaoAlimento, umidade, energiaKcal, energiaKj) VALUES (''"
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
