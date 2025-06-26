from gerador import gerar_instancias
from solver import exibir_resultado
import random
import copy

def construir_solucao_grasp(pecas, L, alpha=0.3): #construcao do grasp gerando solucao inicial gulosa 

    #transforma o dicionario pecas em uma lista que contém todas as pecas
    todas_pecas = []  
    for peca in pecas:
        todas_pecas.extend([peca["tamanho"]] * peca["quantidade"])
    
    # Ordena decrescentemente
    todas_pecas.sort(reverse=True)
    
    #barras preenchidas com as pecas alocadas
    barras = []


    #loop de construcao : repete para cada peca alocada
    for _ in range(len(todas_pecas)):
        if not todas_pecas: #termina o loop se a peca estiver fazia
            break

        # Calcula o limite de cortes
        rcl = []
        max_len = todas_pecas[0]
        min_len = todas_pecas[-1]
        limite = min_len + alpha * (max_len - min_len)

        #preenche a lista com o limite de cortes
        for p in todas_pecas:
            if p >= limite:
                rcl.append(p)
            else:
                break  # como está ordenado, pode parar
        
        #define aleatoriedade das pecas
        if not rcl:
            rcl = todas_pecas
        selecionada = random.choice(rcl)
        todas_pecas.remove(selecionada)

        # lógica de alocacao das pecas nas barras
        colocado = False
        for barra in barras:
            if sum(barra) + selecionada <= L:
                barra.append(selecionada)
                colocado = True
                break
        if not colocado:
            barras.append([selecionada])

    return barras

#recebe uma solucao e tenta melhora-la localmente, a partir da realocacao das pecas
def busca_local(barras, L):

    # inicializacao
    melhor = copy.deepcopy(barras)
    melhor_usadas = len(melhor)
    melhoria = True

    while melhoria:
        melhoria = False

        #percorre todas as pecas de todas as barras
        for i in range(len(melhor)):
            for j in range(len(melhor[i])):
                peca = melhor[i][j]   #tenta mover cada peca de cada barra

                #tenta mover pecas para outras barras
                for k in range(len(melhor)):
                    if k != i and sum(melhor[k]) + peca <= L:

                        #cria novas solucoes e move as pecas
                        nova_solucao = copy.deepcopy(melhor)
                        nova_solucao[k].append(peca)
                        nova_solucao[i].pop(j)
                        if nova_solucao[i] == []:
                            nova_solucao.pop(i)

                        #verificacao de melhoria
                        if len(nova_solucao) < melhor_usadas:
                            melhor = nova_solucao
                            melhor_usadas = len(nova_solucao)
                            melhoria = True
                            break
                if melhoria:
                    break
            if melhoria:
                break
    return melhor


def grasp(instancia, max_iter=50, alpha=0.3):

    # extrai o tamanho da barra e lista de pecas
    L = instancia["comprimento_barra"]
    pecas = instancia["pecas"]
    melhor_solucao = None
    melhor_usadas = float('inf')

    #loop que inicializa busca local
    for _ in range(max_iter):
        solucao = construir_solucao_grasp(pecas, L, alpha)
        solucao = busca_local(solucao, L)

        #salva como melhor se a nova solucao usar menos barras
        if len(solucao) < melhor_usadas:
            melhor_usadas = len(solucao)
            melhor_solucao = solucao

    return melhor_solucao

if __name__ == "__main__":
    instancia = gerar_instancias(seed=42)

    print("Instância gerada:")
    for peca in instancia["pecas"]:
        print(f"{peca['tipo']}: tamanho={peca['tamanho']}, quantidade={peca['quantidade']}")

    print("\nExecutando GRASP com busca local...\n")
    solucao_final = grasp(instancia, max_iter=50, alpha=0.3)
    exibir_resultado(instancia, solucao_final)
