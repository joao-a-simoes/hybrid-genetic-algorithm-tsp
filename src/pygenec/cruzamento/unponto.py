import numpy as np
from .cruzamento import Cruzamento,NoCompatibleIndividualSize

class UmPonto(Cruzamento):

    def cruzamento(self,progenitor1,progenitor2):

        n1 = len(progenitor1)
        n2 = len(progenitor2)
		
        if n1 != n2:
            msg = "Tamanho dos indivíduos incompativeis"
            raise NoCompatibleIndividualSize(msg)
			
        ponto = np.random.randint(1,(n1-1))
	
        desc1 = progenitor1.copy()
        desc2 = progenitor2.copy()
		
        desc1 = desc1[:ponto]
        desc2 = desc2[:ponto]
		
        i =0 

        while len(desc1) < n1  or len(desc2) < n2:
		
            if progenitor1[i] not in desc2 and len(desc2) < n2:
                desc2 = np.append(desc2, progenitor1[i])
		
		
            if progenitor2[i] not in desc1 and len(desc1) < n1:
                desc1 = np.append(desc1, progenitor2[i])
		
		
            i += 1

        return  desc1,desc2 
	    