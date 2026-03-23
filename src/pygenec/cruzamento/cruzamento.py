from numpy import array, ndarray
from numpy.random import randint, random

class NoCompatibleIndividualSize(Exception):
    pass

class Cruzamento:

    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao

    def cruzamento(self, progenitor1, progenitor2):
        raise NotImplementedError("A ser implementado")

    def descendentes(self, subpopulacao, pcruz):

        nova_populacao = []
        pop_existente_set = set(map(tuple,nova_populacao))
        npop = len(subpopulacao)

        while len(nova_populacao) < self.tamanho_populacao:

            i = randint(0, npop - 1)
            j = randint(0, npop - 1)

            while j == i:
                j = randint(0, npop - 1)

            cruzar = random()

            if cruzar < pcruz:
                desc1, desc2 = self.cruzamento(subpopulacao[i], subpopulacao[j])

                parada = 0
                while tuple(desc1) in pop_existente_set and (parada < 10):
                    desc1, _ = self.cruzamento(subpopulacao[i], subpopulacao[j])
                    parada += 1
                nova_populacao.append(desc1)

                if len(nova_populacao) < self.tamanho_populacao and isinstance(desc2, ndarray):
                    parada = 0
                    while tuple(desc2) in pop_existente_set and (parada < 10):
                        _, desc2 = self.cruzamento(subpopulacao[i], subpopulacao[j])
                        parada += 1
                    nova_populacao.append(desc2)

        return array(nova_populacao)
