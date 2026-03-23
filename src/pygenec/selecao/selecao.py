from numpy import array

class Selecao:
	def __init__(self, populacao):
		self.populacao = populacao
	
	def selecionar(self, fitness):
		raise NotImplementedError('A ser implemetado')
		
	def selecao(self,n,fitness=None):
		progenitores = array([self.selecionar(fitness) for _ in range(n)])
		return self.populacao.populacao[progenitores] 