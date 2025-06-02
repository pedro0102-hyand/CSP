import pandas as pd 
import random 

def gerar_instancias(
    L=110,               # comprimento da barra padrão
    n=10,                # número de tipos de peças
    min_length=10,       # tamanho mínimo da peça
    max_length=100,      # tamanho máximo da peça
    min_demand=10,       # demanda mínima
    max_demand=50,       # demanda máxima
    seed=None            # semente para reprodutibilidade
):
    if seed is not None:
        random.seed(seed)

    pecas = []
    for i in range(n):
        while True:
            tamanho = random.randint(min_length, max_length)
            if tamanho < L:
                break
        quantidade = random.randint(min_demand, max_demand)
        pecas.append({"tipo": f"P{i+1}", "tamanho": tamanho, "quantidade": quantidade})

    return {
        "comprimento_barra": L,
        "pecas": pecas
    }

# Gerando uma instância
instancia = gerar_instancias(seed=42)
df = pd.DataFrame(instancia["pecas"])

print(f"Comprimento da barra: {instancia['comprimento_barra']}")
print(df)
