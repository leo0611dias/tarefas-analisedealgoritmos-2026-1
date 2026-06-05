import heapq
import networkx as nx
import matplotlib.pyplot as plt


def arvore_geradora_minima(grafo, vertice_inicial):
    """
    Encontra a Árvore Geradora Mínima (AGM) utilizando o algoritmo de Prim.

    Retorna:
        - lista com as arestas selecionadas
        - custo total da árvore
    """

    visitados = {vertice_inicial}
    arestas_agm = []
    custo_total = 0

    # Fila de prioridade contendo as arestas disponíveis
    fila_prioridade = []

    for destino, peso in grafo[vertice_inicial].items():
        fila_prioridade.append((peso, vertice_inicial, destino))

    heapq.heapify(fila_prioridade)

    while fila_prioridade:
        peso, origem, destino = heapq.heappop(fila_prioridade)

        if destino in visitados:
            continue

        visitados.add(destino)
        arestas_agm.append((origem, destino, peso))
        custo_total += peso

        # Adiciona novas possibilidades de conexão
        for vizinho, custo in grafo[destino].items():
            if vizinho not in visitados:
                heapq.heappush(
                    fila_prioridade,
                    (custo, destino, vizinho)
                )

    return arestas_agm, custo_total


# Representação do grafo
grafo = {
    "A": {"B": 2, "C": 6, "D": 3},
    "B": {"A": 2, "D": 5},
    "C": {"A": 6, "D": 4},
    "D": {"A": 3, "B": 5, "C": 4}
}

# Execução do algoritmo
agm, custo = arvore_geradora_minima(grafo, "A")

# Exibição dos resultados
print("\n===== RESULTADO DO ALGORITMO DE PRIM =====")

for origem, destino, peso in agm:
    print(f"{origem} --> {destino} (peso = {peso})")

print(f"\nCusto total da AGM: {custo}")
print("=" * 40)

# ---------------- VISUALIZAÇÃO ----------------

rede = nx.Graph()

for origem, conexoes in grafo.items():
    for destino, peso in conexoes.items():
        rede.add_edge(origem, destino, weight=peso)

# Posições dos vértices
coordenadas = {
    "A": (0.5, 1),
    "B": (0, 0.5),
    "C": (1, 0.5),
    "D": (0.5, 0)
}

plt.figure(figsize=(8, 6))
plt.title("Árvore Geradora Mínima obtida pelo Algoritmo de Prim")

# Grafo completo
nx.draw(
    rede,
    coordenadas,
    with_labels=True,
    node_size=1800,
    node_color="skyblue",
    edge_color="silver",
    width=2,
    font_size=14
)

# Destaca as arestas da AGM
arestas_destacadas = [(u, v) for u, v, _ in agm]

nx.draw_networkx_edges(
    rede,
    coordenadas,
    edgelist=arestas_destacadas,
    width=4,
    edge_color="green"
)

# Exibe os pesos
rotulos = nx.get_edge_attributes(rede, "weight")
nx.draw_networkx_edge_labels(
    rede,
    coordenadas,
    edge_labels=rotulos
)

plt.axis("off")
plt.show()
