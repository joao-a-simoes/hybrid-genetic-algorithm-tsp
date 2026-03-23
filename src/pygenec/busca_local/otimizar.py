import numpy as np

class InvalidListSizeError(Exception):
    pass

class Otimizador:

    def __init__(self, dist):
        self.dist = dist

    def metodo(self,individuo):
        raise NotImplementedError("A ser implementado")
    
    
    def otimizar(self,populacao):
        npop = len(populacao)
        nova_populacao = []

        for individuo in populacao:
            novo_individuo = self.metodo(individuo)
            nova_populacao.append(novo_individuo)

        
        nova_populacao = np.asarray(nova_populacao)
        nova_populacao = nova_populacao.astype(populacao.dtype)

        if  len(nova_populacao) != npop:
            raise InvalidListSizeError("Tamanho da população inválido")
        
        return nova_populacao
