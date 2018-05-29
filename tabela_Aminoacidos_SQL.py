#! /usr/bin/env/ python
import string

arquivo = open('taco_Aminoacidos.csv','r')
arquivoSQL =open('insert_Aminoacidostaco3.sql','wr')
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
   dados="INSERT INTO Aminoacidostaco3 (id, numeroAlimento, descricaoAlimento, triptofano, treonina, isoleucina, leucina, lisina, metionina, cistina, fenilalanina, tirosina, valina, arginina, histidina, alanina, acidoAspartico, acidoClutamico, glicina, prolina, serina, created_at, updated_at) VALUES (''"
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
