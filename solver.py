from gerador import gerar_instancias

def first_fit_decreasing(instancia):

    L = instancia["comprimento_barra"]
    pecas = instancia["pecas"]

    # Expande as peças conforme suas quantidades
    todas_pecas = []
    for peca in pecas:
        todas_pecas.extend([peca["tamanho"]] * peca["quantidade"])

    # Ordena em ordem decrescente
    todas_pecas.sort(reverse=True)

    # Lista de barras (cada uma é uma lista de cortes alocados)
    barras = []

    for tamanho in todas_pecas:
        colocado = False
        for barra in barras:
            if sum(barra) + tamanho <= L:
                barra.append(tamanho)
                colocado = True
                break
        if not colocado:
            barras.append([tamanho])  # nova barra

    return barras


def exibir_resultado(instancia, barras):
   
    L = instancia["comprimento_barra"]
    print(f"\nComprimento da barra: {L}")
    print(f"Número total de barras utilizadas: {len(barras)}\n")
    for i, barra in enumerate(barras, 1):
        uso = sum(barra)
        desperdicio = L - uso
        print(f"Barra {i:02d}: {barra} | Uso: {uso} | Desperdício: {desperdicio}")

if __name__ == "__main__":
    instancia = gerar_instancias(seed=42)

    print("Peças a serem cortadas:")
    for peca in instancia["pecas"]:
        print(f"{peca['tipo']}: tamanho={peca['tamanho']}, quantidade={peca['quantidade']}")

    barras = first_fit_decreasing(instancia)
    exibir_resultado(instancia, barras)




    

