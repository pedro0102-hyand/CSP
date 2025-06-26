from gerador import gerar_instancias
from solver import first_fit_decreasing, exibir_resultado
import random
import math
import copy

def calcular_custo(barras):
    return len(barras)  # custo = número de barras

#cria copia da solucao atual
def gerar_vizinho(solucao, L):
    vizinho = copy.deepcopy(solucao)

    # Seleciona duas barras diferentes aleatórias
    if len(vizinho) < 2:
        return vizinho

    #escolhe barras para tentar mover pecas entre elas
    i, j = random.sample(range(len(vizinho)), 2)
    if not vizinho[i] or not vizinho[j]:
        return vizinho

    # Move uma peça de i para j (se couber)
    peca = random.choice(vizinho[i])
    if sum(vizinho[j]) + peca <= L:
        vizinho[i].remove(peca)
        vizinho[j].append(peca)
        if not vizinho[i]:  # se barra i ficou vazia
            vizinho.pop(i)

    return vizinho

def simulated_annealing(instancia, T_inicial=100.0, T_final=0.1, alpha=0.95, iter_por_temp=100):

    #extrair dados das instancias
    L = instancia["comprimento_barra"]
    pecas = instancia["pecas"]

    #geracao das solucoes
    solucao_atual = first_fit_decreasing(instancia)
    melhor_solucao = copy.deepcopy(solucao_atual)

    #calculo de custo da solucao
    custo_atual = calcular_custo(solucao_atual)
    melhor_custo = custo_atual

    T = T_inicial

    #algoritmo entra em loop até a temperatura esfriar o suficiente
    while T > T_final:

        #gera varias iteracoes para cada temperatura
        for _ in range(iter_por_temp):

            vizinho = gerar_vizinho(solucao_atual, L)
            custo_vizinho = calcular_custo(vizinho)
            delta = custo_vizinho - custo_atual


            #atualizacao da solucao atual
            if delta < 0 or random.random() < math.exp(-delta / T):
                solucao_atual = vizinho
                custo_atual = custo_vizinho
                if custo_atual < melhor_custo:
                    melhor_solucao = copy.deepcopy(solucao_atual)
                    melhor_custo = custo_atual
                    
        T *= alpha  # reduz a temperatura

    return melhor_solucao

if __name__ == "__main__":
    instancia = gerar_instancias(seed=42)

    print("Instância gerada:")
    for peca in instancia["pecas"]:
        print(f"{peca['tipo']}: tamanho={peca['tamanho']}, quantidade={peca['quantidade']}")

    print("\nExecutando Simulated Annealing...\n")
    solucao_final = simulated_annealing(instancia)
    exibir_resultado(instancia, solucao_final)
