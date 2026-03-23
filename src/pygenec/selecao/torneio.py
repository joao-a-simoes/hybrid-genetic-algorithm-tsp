import numpy as np
from .selecao import Selecao

class Torneio(Selecao):
	def __init__(self, populacao, tamanho=2):
		super().__init__(populacao)
		self.tamanho = tamanho
		
		
	def selecionar(self,fitness):
		if fitness is None:
			fitness = self.populacao.avaliar()
		
		grupo = np.random.choice(np.arange(len(fitness)),size= self.tamanho, replace=True)
		secundario = np.full(len(fitness),np.nan)
		secundario[grupo] = fitness[grupo]
		campeao = np.nanmin(secundario)
		retorno = np.where(secundario == campeao)[0][0]
		return retorno