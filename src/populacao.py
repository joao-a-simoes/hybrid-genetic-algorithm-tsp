import numpy as np

class Populacao:
    """
      """

    def __init__(self,avaliacao,cromossomo_totais,tamanho_da_populacao):
        self.avaliacao = avaliacao
        self.cromossomo_totais = cromossomo_totais
        self.tamanho_da_populacao = tamanho_da_populacao
        
        
    def gerar_populacao(self):
        self.populacao = np.array([np.random.permutation(np.arange(self.cromossomo_totais)) for _ in range(self.tamanho_da_populacao )])
        
        
    def avaliar(self):
        u, indices = np.unique(self.populacao, return_inverse = True, axis= 0)
        valores = self.avaliacao(u)
        valores = valores[indices]
        ind = np.argsort(valores)
        self.populacao[:] = self.populacao[ind]
        return valores[ind]