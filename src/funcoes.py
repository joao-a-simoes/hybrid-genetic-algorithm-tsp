from PIL import Image
import glob
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

def Criar_Gif(caminho, nome_documento):
    """
    Cria um arquivo GIF a partir de uma sequência de imagens PNG.

    Parâmetros
    ----------
    caminho : str
        Caminho com padrão das imagens (ex: "../outputs/imagens/*.png").

    nome_documento : str
        Caminho e nome do arquivo de saída (sem extensão).

    Retorna
    -------
    None
        Salva um arquivo .gif no local especificado.
    """

    files = glob.glob(caminho)

    files = sorted(files, key=lambda x: int(os.path.basename(x).split(".")[0]))

    frames = [Image.open(f) for f in files]

    frames.extend([frames[-1]] * 30)

    frames[0].save(
        f"{nome_documento}",
        save_all=True,
        append_images=frames[1:],
        duration=200,
        loop=1
    )


def limpar_pasta(caminho):
    for arquivo in os.listdir(caminho):
        caminho_arquivo = os.path.join(caminho, arquivo)

        if os.path.isfile(caminho_arquivo):
            os.remove(caminho_arquivo)


def Imagens_para_gif(evolucao, dados, tamanho_populacao, titulo):
    """
    Cria imagens para gerar GIF.

    Parâmetros
    ----------
    evolucao : class
        evolução do algoritimo para acessar o histórico.

    dados : pandas
        arquivo pandas com as codernadas x e y.

    tamanho_populacao : int
        valor numerico com o tamanhdo da populacao

    titulo : str
        Titulo do gráfico

    Retorna
    -------
    None
        Salva um arquivo .gif no local especificado.
    """
    ROOT = os.path.abspath(os.path.join(".."))
    pasta = os.path.join(ROOT, "outputs", "imagens")

    limpar_pasta(pasta)

    Melhor_fitness = evolucao.historico["Melhor_fitness"]
    Mutacao_adaptativa = evolucao.historico["Mutacao_adaptativa"]
    if not Mutacao_adaptativa:
        Mutacao_adaptativa = np.full(
            len(Melhor_fitness), evolucao.mutacao.pmut)
    else:
        for i in range(len(Mutacao_adaptativa)):
            if Mutacao_adaptativa[i] >= 1.0:
                Mutacao_adaptativa[i] = 1.0
    Melhores_individuos = evolucao.historico["Melhores_individuos"]

    numero = 0
    for melhor in Melhores_individuos:
        melhor_solucao = melhor
        x = list(dados["x"])
        y = list(dados["y"])
        x_shortest = []
        y_shortest = []
        for cidade in melhor_solucao:
            x_value, y_value = x[cidade], y[cidade]
            x_shortest.append(x_value)
            y_shortest.append(y_value)

        x_shortest.append(x_shortest[0])
        y_shortest.append(y_shortest[0])
        fig, ax = plt.subplots()
        ax.plot(x_shortest, y_shortest, '--go',
                label='Melhor rota', linewidth=2.5)
        plt.legend()

        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                ax.plot([x[i], x[j]], [y[i], y[j]],
                        'k-', alpha=0.04, linewidth=1)

        plt.title(label=titulo,
                  fontsize=25,
                  color="k")
        str_params = (
            f"\nGeração {numero + 1}\n"
            f"Tamanho da população: {tamanho_populacao}\n"
            f"Cruzamento: {0.8}\n"
            f"Mutação: {round(Mutacao_adaptativa[numero], 2)}")

        plt.suptitle("Distância total: " +
                     str(round(Melhor_fitness[numero], 3)) +
                     str_params, fontsize=18, y=1.047)
        fig.set_size_inches(16, 12)
        plt.savefig(os.path.join(pasta, F"{numero+1}.png"),
                    dpi=300, bbox_inches="tight")
        plt.close()
        numero += 1


def Ate_convergir(array):
    minimo = round(min(array), 6)
    ger = 0
    for i in array:
        i = round(i, 6)
        if i == minimo:
            break
        ger += 1

    return ger


def Melhor_rota(evolucao, dados, tamanho_populacao,Nome ,titulo, Alpha =0.04 ):

    ROOT = os.path.abspath(os.path.join(".."))
    pasta = os.path.join(ROOT, "outputs", "Melhor_rota")

    Melhor_fitness = evolucao.historico["Melhor_fitness"]
    numero = len(Melhor_fitness)

    if not evolucao.historico["Mutacao_adaptativa"]:
        Mutacao_adaptativa = evolucao.mutacao.pmut
    else:
        Mutacao_adaptativa = evolucao.historico["Mutacao_adaptativa"][-1]
        if Mutacao_adaptativa >= 1.0:
            Mutacao_adaptativa = 1.0

    melhor_solucao = evolucao.historico["Melhores_individuos"][-1]

    x = list(dados["x"])
    y = list(dados["y"])

    x_shortest = []
    y_shortest = []

    for cidade in melhor_solucao:
        x_shortest.append(x[cidade])
        y_shortest.append(y[cidade])


    x_shortest.append(x_shortest[0])
    y_shortest.append(y_shortest[0])

    fig, ax = plt.subplots()

    ax.plot(x_shortest, y_shortest, '--go',
            label='Melhor rota', linewidth=2.5)

    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            ax.plot([x[i], x[j]], [y[i], y[j]],
                    'k-', alpha=Alpha, linewidth=1)

    ax.legend()

    plt.title(
        titulo,
        fontsize=25,
        color="k"
    )

    str_params = (
        f"\nGeração {numero}\n"
        f"Tamanho da população: {tamanho_populacao}\n"
        f"Cruzamento: {0.8}\n"
        f"Mutação: {round(Mutacao_adaptativa, 2)}"
    )

    plt.suptitle(
        "Distância total: "
        + str(round(Melhor_fitness[-1], 3))
        + str_params,
        fontsize=18,
        y=1.047
    )

    fig.set_size_inches(16, 12)

    plt.savefig(
        os.path.join(pasta, f"{Nome}.png"),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

def Numero_de_geracoes(n_cidades):

    if n_cidades <= 60:
        ger = 100
    elif n_cidades <= 100:
        ger = 200
    elif n_cidades <= 250:
        ger = 400
    elif n_cidades <= 500:
        ger = 1000
    else:
        ger = int(2 * n_cidades) 

    return ger

def Arredondar_cima(n):
    if n == 0:
        return 0
    
    ordem = 10 ** math.floor(math.log10(abs(n)))
    return math.ceil(n / ordem) * ordem