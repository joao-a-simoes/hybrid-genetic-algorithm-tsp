import numpy as np
from .otimizar import Otimizador

class Opt_2(Otimizador):


    def metodo(self, individuo):
        n = len(individuo)
        melhor_rota = individuo.copy()
        melhorou = True

        while melhorou:
            melhorou = False

            for i in range(1, n-1):
                for j in range(i+1, n):

                    a = melhor_rota[i-1]
                    b = melhor_rota[i]
                    c = melhor_rota[j-1]
                    d = melhor_rota[(j) % n]

                    custo_antigo = self.dist[a][b]
                    if j < n:
                        custo_antigo += self.dist[c][d]

                    custo_novo = self.dist[a][c]
                    if j < n:
                        custo_novo += self.dist[b][d]

                    if custo_novo < custo_antigo:
                        melhor_rota[i:j] = melhor_rota[i:j][::-1]
                        melhorou = True

        return melhor_rota