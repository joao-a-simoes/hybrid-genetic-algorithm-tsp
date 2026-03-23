from numpy import array
from numpy.random import randint ,random

class Mutacao:
    """
    Classe base para operadores de mutação:
    Entrada:
        pmut - probabilidade de ocorrer uma mutação.
    """

    def __init__(self, pmut):
        self._pmut = pmut
        self._populacao = None
        self.npop = None
        self.ngen = None
        self._variavel = 1

    @property
    def pmut (self):
        return (self._pmut * self.variavel)
    
    @property
    def populacao(self):
        return self._populacao

    @property
    def variavel(self):
        return self._variavel
    
    @variavel.setter
    def variavel(self,var):
        if 35 <= var < 50:
            modificador = 1.5

        elif var >= 50:
            modificador = 4
            
        else:
            modificador = 1

        self._variavel = modificador

    @populacao.setter
    def populacao(self, populacao):
        self._populacao = populacao
        self.npop = self._populacao.shape[0]
        self.ngen = self._populacao.shape[1]

    def selecao(self):
        nmut = array([i for i in range(self.npop) if random() < self.pmut])
        return nmut
        

    def mutacao(self):
        raise NotImplementedError("A ser implementado")