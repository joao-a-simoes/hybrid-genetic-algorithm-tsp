class Evolucao:


    def __init__(self,populacao,selecao,cruzamento,mutacao,otimizador,porc_otm,geracoes_totais):
        self.populacao = populacao
        self.selecao = selecao
        self.cruzamento = cruzamento
        self.mutacao = mutacao
        self.otimizador = otimizador

        self.porc_otm = porc_otm
        self.geracoes_totais = geracoes_totais

        self._geracao = 0
        self._melhor_solucao = None
        self._nsele = None
        self._pcruz = None
        self._manter_melhor = True
        self._fitness = None
        self._first = True
        self._adaptativo = 0
        self._menor_valor = None
        self._burst_ativo = 0


        self._historico = {
            "Mutacao_adaptativa": [],
            "Melhores_individuos" : [],
            "Melhor_fitness": [] ,  
            "Media_fitness": []      
            }


    @property
    def historico(self):
        return self._historico

    @property
    def nsele(self):
        return self._nsele

    @property
    def pcruz(self):
        return self._pcruz
    
    @property
    def melhor_solucao(self):
        return self._melhor_solucao 
    
    @property
    def first(self):
        return self._first 

    @property
    def geracao(self):
        return self._geracao

    @first.setter
    def first(self,first):
        self._first = first

    @nsele.setter
    def nsele(self,nsele):
        self._nsele = nsele

    @pcruz.setter
    def pcruz(self,pcruz):
        self._pcruz = pcruz    

    def evoluir(self):

        if self._first:
            self._fitness = self.populacao.avaliar()
            self._first = False
        else:
            if self._menor_valor > self._fitness[0]:
                self._adaptativo = 0
            else:
                self._adaptativo += 1
                if self.mutacao.pmut >= 1:
                    self._burst_ativo += 1
                    if self._burst_ativo == 5:
                        self._adaptativo = 0
                        self._burst_ativo = 0


            

        self._menor_valor = self._fitness[0]
        self._melhor_solucao = self.populacao.populacao[0].copy()
        self._historico["Melhores_individuos"].append(self.melhor_solucao)
        self._historico["Melhor_fitness"].append(self._menor_valor)
        self._historico["Media_fitness"].append(self._fitness.mean())

        subpopulacao = self.selecao.selecao(self._nsele, fitness=self._fitness)
        populacao = self.cruzamento.descendentes(subpopulacao, pcruz=self._pcruz)
        
        if self._geracao >= round(self.geracoes_totais - (self.geracoes_totais*self.porc_otm)):
            populacao = self.otimizador.otimizar(populacao)
            self._adaptativo = 0
            print("Otimizador on")

        self.mutacao.populacao = populacao
        self.mutacao.variavel = self._adaptativo
        self.mutacao.mutacao()
        self._historico["Mutacao_adaptativa"].append(self.mutacao.pmut)
        self.populacao.populacao[:] = populacao[:]

        self._geracao += 1

        conjunto = set(map(tuple,self.populacao.populacao.copy()))

        if self._manter_melhor and (tuple(self._melhor_solucao) not in conjunto ) :
            self.populacao.populacao[-1] = self._melhor_solucao

        self._fitness = self.populacao.avaliar()

        return self._geracao, self._fitness[0], self._melhor_solucao 
