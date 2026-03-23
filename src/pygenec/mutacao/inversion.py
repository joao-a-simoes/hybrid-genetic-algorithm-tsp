import numpy as np
from .mutacao import Mutacao

class Inversion(Mutacao):

    def inverter(self, array):
        novo = array.copy()
        ordem = np.random.choice(np.arange((self.ngen)+1), replace=False, size=2)
        ordem = np.sort(ordem)
        novo[ordem[0]:ordem[1]] = novo[ordem[0]:ordem[1]][::-1]
        return novo

    def mutacao(self):
        nmut = self.selecao()
        for i in nmut:
            self.populacao[i,:] = self.inverter(self.populacao[i,:])