import numpy as np
from .cruzamento import Cruzamento,NoCompatibleIndividualSize

class Edge_recombination(Cruzamento):

    def dic_adjacencias(self,progenitor1,progenitor2):
        n1 = len(progenitor1)
        n2 = len(progenitor2)

        if n1 != n2:
            msg = "Tamanho dos indivíduos incompativeis"
            raise NoCompatibleIndividualSize(msg)
		
        dic = {}

        for i in range(n1):
            vizinhos = set()
            
            vizinhos.add(progenitor1[i-1])

            if i ==  n1-1:
                vizinhos.add(progenitor1[0])
            else: 
                vizinhos.add(progenitor1[i+1])
            
            dic[progenitor1[i]] = vizinhos

        for i in range(n2):
            vizinhos = set()
            
            vizinhos.add(progenitor2[i-1])
            if i ==  n2-1:
                vizinhos.add(progenitor2[0])
            else: 
                vizinhos.add(progenitor2[i+1])

            if progenitor2[i] in dic:
                dic[progenitor2[i]] = dic[progenitor2[i]].union(vizinhos)
            else:
                dic[progenitor2[i]] = vizinhos


        for k in dic:
            dic[k] = list(dic[k])

        return dict(sorted(dic.items()))
		
    def primeiro(self,progenitor1,progenitor2):
        escolha = np.random.choice([progenitor1[0],progenitor2[0]])
        return escolha

    def cruzamento(self,progenitor1,progenitor2):
        ngem = len(progenitor1)
        dicionario = self.dic_adjacencias(progenitor1,progenitor2)
        prim = self.primeiro(progenitor1,progenitor2)
        descendente = []

        while True:
            for i in range(ngem):
                try:
                    dicionario[i].remove(prim)
                except ValueError:
                    pass
        
            descendente.append(prim)

            if len(descendente) == ngem:
                break

            contador = [len(dicionario[x]) for x in dicionario[prim]]
            if not contador:
                lista = [i for i in dicionario.keys() if i not in descendente]
                prim = np.random.choice(lista)
            else:
                indice = [i for i,v in enumerate(contador)if v == min(contador) ]
               
                if len(indice) > 1:
                    indice = np.random.choice(indice)
                    prim = dicionario[prim][indice]

                else:
                    indice = indice[0]
                    prim = dicionario[prim][indice]

        descendente = np.asarray(descendente)
        descendente = descendente.astype(progenitor1.dtype)
        return descendente, 0