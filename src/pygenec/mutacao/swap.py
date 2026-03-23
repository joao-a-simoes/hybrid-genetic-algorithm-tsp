import numpy as np
from .mutacao import Mutacao

class Swap(Mutacao):

    def mutacao(self):
        nmut = self.selecao()
        gen1 = [np.random.randint(0, self.ngen) for _ in nmut]
        gen2 = [np.random.randint(0, self.ngen) for _ in nmut]
        
        for i in range(len(nmut)):
            if gen1[i] == gen2[i]:
                while gen1[i] == gen2[i]:
                    gen2[i] = np.random.randint(0, self.ngen)
					
        self.populacao[nmut, gen1] , self.populacao[nmut, gen2] = self.populacao[nmut, gen2] , self.populacao[nmut, gen1]
		

		
		