# Algoritmo Genético

## Introdução

O **Travelling Salesman Problem (TSP)** é um problema clássico de **otimização combinatória**, cujo objetivo é encontrar a menor rota que visite todas as cidades exatamente uma vez e retorne à origem.

Esse problema pertence à classe **NP-hard**, pois o número de possíveis rotas cresce fatorialmente com o número de cidades, tornando métodos exatos inviáveis para instâncias maiores.

Para lidar com esse desafio, neste projeto desenvolve-se um **Algoritmo Genético Híbrido**, incorporando operadores especializados, **mutação adaptativa**, **Burst Mutation** e **busca local**.

**Objetivo:** Desenvolver um framework de algoritmo genético híbrido para o TSP, sem o uso de bibliotecas especializadas, utilizando principalmente `NumPy`.

---

## Diferenciais do Projeto

- Implementação de um **Algoritmo Genético Híbrido (Memético)**
- Uso do operador **Edge Recombination (ERX)** específico para TSP
- Estratégia de **Mutação Adaptativa**
- Mecanismo de **Burst Mutation** para escape de ótimos locais
- Integração com **busca local (2-opt)** nas fases finais
- Controle de **diversidade populacional**

---

## Fundamentação Teórica

### Conceitos Fundamentais

- **Indivíduo**: representa uma solução candidata para o problema.
- **Gene**: menor unidade do indivíduo, representando uma cidade.
- **Cromossomo**: conjunto de genes que representa um indivíduo completo.
- **População**: conjunto de indivíduos em uma geração.
- **Função fitness**: mede o quão boa é cada solução (distância total percorrida).
- **Seleção**: escolhe os melhores indivíduos para reprodução.
- **Crossover**: combina genes de dois pais para gerar descendentes.
- **Mutação**: altera genes aleatoriamente para manter diversidade.
- **Elitismo**: garante que os melhores indivíduos passem para a próxima geração.
- **Geração**: uma iteração completa do algoritmo.
- **Critério de parada**: condição para encerramento (número de gerações, convergência, etc.).

---

### Representação para o TSP

Cada indivíduo da população corresponde a uma **rota completa**, indicando a ordem em que as cidades são visitadas.

Exemplo:
```[0, 3, 1, 4, 2]```


Esse vetor indica que o caixeiro viaja da cidade **0 → 3 → 1 → 4 → 2 → 0**, retornando ao ponto inicial.

A qualidade de cada indivíduo é avaliada por meio da **função fitness**, que corresponde à **distância total da rota**.

A função fitness é definida como:

$$
f(\pi) = \sum_{i=1}^{n-1} d(\pi_i, \pi_{i+1}) + d(\pi_n, \pi_1)
$$

onde:

- $\pi$ representa a permutação das cidades (rota)
- $d(i,j)$ é a distância entre as cidades $i$ e $j$
- o último termo garante o **retorno à cidade inicial**

O objetivo do algoritmo é **minimizar a função fitness**, ou seja, encontrar a rota com **menor distância total**.

---

## Algoritmo Híbrido

### Seleção

O método de seleção utilizado é o **torneio de tamanho 2**.

Nesse método, dois indivíduos da população são selecionados aleatoriamente e comparados entre si. O indivíduo com **melhor valor de fitness** (menor distância) é escolhido para reprodução.

O procedimento ocorre da seguinte forma:

1. Selecionar dois indivíduos aleatórios da população  
2. Comparar os valores de fitness  
3. Selecionar o indivíduo com melhor fitness como **pai**  

Esse processo é repetido sempre que um novo indivíduo precisa ser selecionado.

---

### Cruzamento

O operador de cruzamento utilizado é o **Edge Recombination (ERX)**, específico para problemas de permutação como o TSP. Esse método busca preservar **arestas presentes nos pais**, aumentando a qualidade das soluções geradas.

Além disso, o algoritmo implementa um mecanismo de **controle de diversidade**:

1. Um descendente é gerado  
2. Verifica-se se ele já existe na subpopulação de descendentes  
3. Caso exista, são feitas até **10 tentativas** de gerar um indivíduo diferente  
4. Se não for possível, o descendente é adicionado mesmo assim  

Essa estratégia reduz duplicatas e melhora a exploração do espaço de busca.

---

### Mutação

A etapa de mutação é composta por dois mecanismos principais:

#### 1. Adaptive Mutation Probability Strategy

Para evitar que o algoritmo fique preso em **ótimos locais**, a probabilidade de mutação é ajustada dinamicamente:

- Entre **35 e 50 gerações sem melhoria** → multiplicada por **1.5**  
- Acima de **50 gerações sem melhoria** → multiplicada por **4**  
- Ao encontrar uma melhoria → retorna ao valor original  

Isso aumenta a **exploração** quando o algoritmo entra em estagnação.

---

#### 2. Burst Mutation

A **Burst Mutation** aumenta drasticamente a diversidade da população:

1. A probabilidade de mutação é definida como **1 (100%)**  
2. Mantida por **5 gerações consecutivas**  
3. Retorna ao valor padrão após esse período  

Essa estratégia ajuda o algoritmo a escapar de regiões de estagnação.

---

### Busca Local (2-opt)

O **2-opt** é uma heurística de busca local utilizada no TSP. Ele funciona trocando duas arestas da rota e invertendo o segmento intermediário, reduzindo o comprimento total.

Uma das principais vantagens do 2-opt é remover **cruzamentos de arestas**, frequentemente gerando soluções melhores.

Neste projeto, o 2-opt é aplicado nas **últimas 10% das gerações**, atuando como refinamento final das soluções.

Com isso, o método pode ser classificado como um **Algoritmo Memético**, pois combina:

- Busca global (**Algoritmo Genético**)  
- Busca local (**2-opt**)  

---

# Código

## Implementação

O framework foi desenvolvido majoritariamente utilizando **NumPy**, garantindo eficiência nas operações numéricas.

Bibliotecas auxiliares utilizadas:

- **NumPy** → operações numéricas  
- **Matplotlib** → visualização de gráficos  
- **Pandas** → manipulação de dados  
- **SciPy** → métricas estatísticas (skewness e kurtosis)  
- **time** → medição de tempo  
- **os / sys** → manipulação do sistema  

---

## Estrutura do Projeto

```
PROJECT_AG_TSP
│
├── config/
│
├── data/
│ ├── kangle/
│ └── TSPLIB/
│
├── notebooks/
│ ├── berlin52.ipynb
│ ├── eil76.ipynb
│ ├── kroA100.ipynb
│ ├── tsp225.ipynb
│ └── main.ipynb
│
├── outputs/
│ ├── gifs/
│ ├── graficos/
│ ├── imagens/
│ └── Melhor_rota/
│
├── src/
│ ├── pygene/
│ │ ├── busca_local/
│ │ ├── cruzamento/
│ │ ├── mutacao/
│ │ ├── selecao/
│ │
│ ├── evolucao_tsp_classico.py
│ ├── evolucao.py
│ ├── funcoes.py
│ └── populacao.py
│
└── README.md
```


---

## Descrição das Pastas

### `config`
Arquivos de configuração do projeto.

### `data`
Conjuntos de dados utilizados no TSP.

- **kangle** → datasets adicionais  
- **TSPLIB** → instâncias clássicas  

### `notebooks`
Notebooks para experimentação:

- `berlin52.ipynb`  
- `eil76.ipynb`  
- `kroA100.ipynb`  
- `tsp225.ipynb`  
- `main.ipynb`  

### `outputs`
Resultados gerados:

- `gifs` → animações  
- `graficos` → evolução do fitness  
- `imagens` → visualizações  
- `Melhor_rota` → melhores soluções  

### `src`
Código-fonte principal.

#### Módulos

- `pygene` → implementação do algoritmo genético  
  - `busca_local` → heurísticas (AG híbrido)  
  - `cruzamento` → operadores de crossover  
  - `mutacao` → operadores de mutação  
  - `selecao` → métodos de seleção  

#### Arquivos principais

- `evolucao_tsp_classico.py` → AG clássico  
- `evolucao.py` → AG híbrido  
- `funcoes.py` → funções auxiliares  
- `populacao.py` → estrutura da população  

---

## Fluxo do Algoritmo

1. Gerar população inicial  
2. Avaliar fitness  
3. Selecionar indivíduos  
4. Aplicar crossover  
5. Aplicar mutação  
6. Realizar substituição  
7. Verificar estagnação  
8. Aplicar Burst Mutation (se necessário)  
9. Aplicar 2-opt nas últimas 10% das gerações  
10. Retornar a melhor solução  

### Número de Gerações

O número de gerações é definido com base no tamanho do problema (quantidade de cidades), aumentando conforme a complexidade:

- Até 60 cidades → 100 gerações  
- Até 100 cidades → 200 gerações  
- Até 250 cidades → 400 gerações  
- Até 500 cidades → 1000 gerações  
- Acima de 500 cidades → proporcional ao tamanho (`2 × n_cidades`)  

Esse critério busca equilibrar **custo computacional** e **qualidade das soluções**.

---

### Tamanho da População

O tamanho da população é definido como:
`3 x número de genes`


Esse valor permite manter uma boa diversidade populacional sem elevar excessivamente o custo computacional.

---

## Comparação de Resultados (Kaggle)

### Algoritmo Genético Clássico

O **Algoritmo Genético Clássico (AG Clássico)** utilizado como baseline segue a estrutura tradicional de um AG, sem mecanismos avançados de intensificação ou adaptação.

As principais características são:

- **Seleção**: torneio de tamanho 2  
- **Crossover**: cruzamento de **um ponto**  
- **Mutação**: operador **swap** (troca de duas cidades na rota) com probabilidade fixa  
- **Elitismo**: preservação dos melhores indivíduos  
- **Sem busca local** (não utiliza 2-opt)  
- **Sem estratégias adaptativas** (não utiliza mutação adaptativa ou burst mutation)  

Dessa forma, o AG Clássico serve como referência para avaliar o impacto das melhorias introduzidas no **AG Híbrido**.

---

### Algoritmo Genético Híbrido

O **Algoritmo Genético Híbrido (AG Híbrido)** estende o modelo clássico com mecanismos adicionais para melhorar a exploração e intensificação da busca:

- **Crossover especializado**: Edge Recombination (ERX)  
- **Mutação adaptativa**  
- **Burst Mutation**  
- **Busca local (2-opt)**  
- **Controle de diversidade populacional**  

Essas modificações permitem maior capacidade de escapar de ótimos locais e encontrar soluções de melhor qualidade, especialmente em instâncias maiores.

Foram avaliadas duas instâncias: uma **small** (~30 cidades) e outra **medium** (~100 cidades), comparando o **Algoritmo Genético Clássico (AG Clássico)** e o **Algoritmo Genético Híbrido (AG Híbrido)**.

---

### Instância Small

- **AG Híbrido**
  - Tempo: 7.11 s  
  - Gerações: 91  
  - Melhor fitness: **59.3890**

- **AG Clássico**
  - Tempo: 3.36 s  
  - Gerações: 98  
  - Melhor fitness: **82.8056**

O AG Híbrido encontrou uma solução significativamente melhor (**menor fitness**), porém com maior tempo de execução.

---

### Instância Medium

- **AG Híbrido**
  - Tempo: 533.35 s  
  - Gerações: 198  
  - Melhor fitness: **7.7053**

- **AG Clássico**
  - Tempo: 22.34 s  
  - Gerações: 198  
  - Melhor fitness: **23.8067**

Em problemas maiores, o AG Híbrido se destaca ainda mais na **qualidade da solução**, porém com um custo computacional significativamente superior.

---

## Conclusão

- O **AG Clássico** é mais rápido e eficiente em termos de tempo.  
- O **AG Híbrido** produz soluções melhores (menor fitness), especialmente em instâncias maiores.  

Existe um claro **trade-off entre tempo de execução e qualidade da solução**.

---

### Fitness

**Small**
<p align="center">
  <img src="outputs/graficos/AG Híbrido Small.png" width="35%">
  <img src="outputs/graficos/AG Clássico Small.png" width="35%">
</p>

**Medium**
<p align="center">
  <img src="outputs/graficos/AG Híbrido Medium.png" width="35%">
  <img src="outputs/graficos/AG Clássico Medium.png" width="35%">
</p>

---

# Benchmark

Os experimentos foram realizados utilizando instâncias clássicas do **Travelling Salesman Problem (TSP)**, amplamente utilizadas na literatura para avaliação de algoritmos de otimização combinatória.

As instâncias utilizadas foram:

| Problema   | Nº de cidades | Tipo           |
|-----------|--------------|----------------|
| **berlin52** | 52  | pequeno        |
| **eil76**    | 76  | pequeno-médio  |
| **kroA100**  | 100 | médio          |
| **tsp225**   | 225 | médio-grande   |

Esses conjuntos de dados permitem avaliar o desempenho dos algoritmos em diferentes níveis de complexidade.

O objetivo dos testes foi comparar o desempenho do **AG Clássico** com o **AG Híbrido**, considerando:

- Qualidade da solução (fitness)  
- Proximidade do ótimo global (gap)  
- Tempo de execução  
- Comportamento de convergência  

---

## Resultados

---

## Instância: berlin52

**Ótimo Global:** 7544.3659

| Algoritmo | Melhor Fitness | Gap | Tempo (s) | Gerações |
| :--- | :--- | :--- | :--- | :--- |
| **AG Clássico** | 13591.2383 | 6046.8724 | 4.99 | 97 |
| **AG Híbrido**  | **7544.3659** | **0.0000** | 27.28 | 97 |

### Evolução das rotas
<p align="center">
  <img src="outputs/gifs/AG Híbrido berlin52.gif" width="600">
</p>

### Híbrido vs Clássico

**Rota**
<p align="center">
  <img src="outputs/Melhor_rota/AG Híbrido berlin52.png" width="35%">
  <img src="outputs/Melhor_rota/AG Clássico berlin52.png" width="35%">
</p>

**Evolução do Fitness**
<p align="center">
  <img src="outputs/graficos/AG Híbrido berlin52.png" width="35%">
  <img src="outputs/graficos/AG Clássico berlin52.png" width="35%">
</p>

---

## Instância: eil76

**Ótimo Global:** 545.3876

| Algoritmo | Melhor Fitness | Gap | Tempo (s) | Gerações |
| :--- | :--- | :--- | :--- | :--- |
| **AG Clássico** | 1177.7486 | 632.3610 | 24.73 | 199 |
| **AG Híbrido**  | **550.7862** | **5.3986** | 158.56 | 192 |

### Evolução das rotas
<p align="center">
  <img src="outputs/gifs/AG Híbrido eil76.gif" width="600">
</p>

### Híbrido vs Clássico

**Rota**
<p align="center">
  <img src="outputs/Melhor_rota/AG Híbrido eil76.png" width="35%">
  <img src="outputs/Melhor_rota/AG Clássico eil76.png" width="35%">
</p>

**Evolução do Fitness**
<p align="center">
  <img src="outputs/graficos/AG Híbrido eil76.png" width="35%">
  <img src="outputs/graficos/AG Clássico eil76.png" width="35%">
</p>

---

## Instância: kroA100

**Ótimo Global:** 21285.4432

| Algoritmo | Melhor Fitness | Gap | Tempo (s) | Gerações |
| :--- | :--- | :--- | :--- | :--- |
| **AG Clássico** | 83310.5343 | 62025.0911 | 80.29 | 191 |
| **AG Híbrido**  | **21402.7593** | **117.3161** | 342.10 | 189 |

### Híbrido vs Clássico

**Rota**
<p align="center">
  <img src="outputs/Melhor_rota/AG Híbrido kroA100.png" width="35%">
  <img src="outputs/Melhor_rota/AG Clássico kroA100.png" width="35%">
</p>

**Evolução do Fitness**
<p align="center">
  <img src="outputs/graficos/AG Híbrido kroA100.png" width="35%">
  <img src="outputs/graficos/AG Clássico kroA100.png" width="35%">
</p>

---

## Instância: tsp225
**Ótimo Global:** 3859.0000

| Algoritmo | Melhor Fitness | Gap | Tempo de Execução (s) | Gerações até Convergir |
| :--- | :--- | :--- | :--- | :--- |
| **AG Clássico** | 20819.3884 | 16960.3884 | 282.86 | 389 |
| **AG Híbrido** | **4051.0850** | **192.0850** | 7130.58 | 391 |

#### Híbrido x Clássico

**Rota**
<p align="center">
  <img src="outputs/Melhor_rota/AG Híbrido tsp225.png" width="35%">
  <img src="outputs/Melhor_rota/AG Clássico tsp225.png" width="35%">
</p>

**Evolução Fitness**
<p align="center">
  <img src="outputs/graficos/AG Híbrido tsp225.png" width="35%">
  <img src="outputs/graficos/AG Clássico tsp225.png" width="35%">
</p>

