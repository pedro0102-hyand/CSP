# ⚽ Cutting Stock Problem com Metaheurísticas 🧠

Este projeto visa resolver o **Problema de Corte de Barras (Cutting Stock Problem)**, aplicado à **construção de estádios de futebol**, utilizando algoritmos baseados em **metaheurísticas**, como **Simulated Annealing** e **GRASP**, além de heurísticas clássicas como **First Fit Decreasing**.

---

## 📌 Objetivo

O problema consiste em cortar barras de comprimento fixo para atender demandas de peças de diferentes tamanhos, minimizando o número total de barras utilizadas. Essa situação aparece, por exemplo, na fabricação de estruturas metálicas para estádios, onde há necessidade de corte eficiente de tubos ou vigas metálicas.

---

## ⚙️ Tecnologias utilizadas

- 🐍 Python 3
- 📊 Pandas
- 🎲 Random / Math
- 📄 Organização modular com scripts por heurística

---

## 📂 Estrutura do Projeto

```
.
├── gerador.py        # Geração de instâncias aleatórias do problema
├── solver.py         # Heurística First Fit Decreasing (solução inicial)
├── grasp.py          # Implementação da metaheurística GRASP
├── SA.py             # Implementação da metaheurística Simulated Annealing
```

---

## 🧩 Descrição dos Arquivos

### `gerador.py`  
Gera instâncias do problema com base em parâmetros como:
- Tamanho da barra padrão (`L`)
- Número de tipos de peças
- Tamanhos e quantidades aleatórios dentro de intervalos definidos
- Semente para reprodutibilidade

> Retorna um dicionário com `comprimento_barra` e lista de peças (`tipo`, `tamanho`, `quantidade`).

---

### `solver.py`  
Implementa a **heurística First Fit Decreasing (FFD)**, que:
- Ordena as peças em ordem decrescente
- Aloca cada peça na primeira barra que tiver espaço
- Cria nova barra se necessário

> Serve como uma **solução inicial** (não ótima), usada por outras heurísticas/metaheurísticas.

---

### `grasp.py`  
Implementa a **metaheurística GRASP (Greedy Randomized Adaptive Search Procedure)**:
- Constrói soluções de forma gulosa e aleatória
- Utiliza um parâmetro `α` para limitar a escolha de peças (RCL)
- Reavalia e otimiza localmente as soluções

> Foco na **diversidade de soluções** e escape de ótimos locais.

---

### `SA.py`  
Implementa a **metaheurística Simulated Annealing (SA)**:
- Parte de uma solução inicial (FFD)
- Gera vizinhos alterando a alocação de peças entre barras
- Aceita piores soluções com probabilidade controlada pela temperatura
- Temperatura decai exponencialmente até o critério final

> Foco na **busca global** e exploração do espaço de soluções.


---


## 🧠 Sobre as Heurísticas

| Heurística               | Tipo            | Vantagem                             |
|--------------------------|------------------|----------------------------------------|
| First Fit Decreasing     | Gulosa           | Simples, rápida, solução base          |
| GRASP                    | Metaheurística   | Geração diversificada de soluções      |
| Simulated Annealing      | Metaheurística   | Exploração ampla do espaço de soluções |

---



## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir **Issues** ou enviar **Pull Requests**.

---

## ✍️ Autores

- Pedro Júlio Sucupira
- Pedro Poiares Barros

