import heapq
import networkx as nx
import matplotlib.pyplot as plt


def menor_caminho_dijkstra(grafo, origem, destino):
    """
    Determina o menor caminho entre dois vértices
    utilizando o algoritmo de Dijkstra.
    """

    # Guarda a menor distância conhecida para cada vértice
    custo = {v: float("inf") for v in grafo}
    custo[origem] = 0

    # Armazena o vértice anterior no caminho
    anterior = {v: None for v in grafo}

    # Fila de prioridade (menor custo primeiro)
    fila = [(0, origem)]

    while fila:

        distancia_atual, vertice_atual = heapq.heappop(fila)

        # Ignora entradas antigas da fila
        if distancia_atual != custo[vertice_atual]:
            continue

        # Destino encontrado
        if vertice_atual == destino:
            break

        for vizinho, peso in grafo[vertice_atual].items():

            novo_custo = custo[vertice_atual] + peso

            if novo_custo < custo[vizinho]:
                custo[vizinho] = novo_custo
                anterior[vizinho] = vertice_atual

                heapq.heappush(
                    fila,
                    (novo_custo, vizinho)
                )

    # Reconstrução do caminho
    caminho = []
    atual = destino

    while atual is not None:
        caminho.append(atual)
        atual = anterior[atual]

    caminho.reverse()

    return caminho, custo[destino]


# ----------------------------
# Definição do grafo
# ----------------------------

grafo = {
    0: {1: 4, 2: 1},
    1: {3: 1},
    2: {1: 2, 4: 5},
    3: {4: 1},
    4: {}
}

origem = 0
destino = 4

caminho_encontrado, custo_total = menor_caminho_dijkstra(
    grafo,
    origem,
    destino
)

# ----------------------------
# Resultado
# ----------------------------

print("\n===== DIJKSTRA =====")
print("Menor caminho:", " -> ".join(map(str, caminho_encontrado)))
print("Custo total:", custo_total)

# ----------------------------
# Visualização
# ----------------------------

rede = nx.DiGraph()

for origem_no, destinos in grafo.items():
    for destino_no, peso in destinos.items():
        rede.add_edge(origem_no, destino_no, weight=peso)

posicoes = {
    0: (0, 1),
    1: (1, 1.5),
    2: (1, 0.5),
    3: (2, 1.5),
    4: (3, 1)
}

plt.figure(figsize=(10, 6))
plt.title("Menor Caminho Encontrado pelo Algoritmo de Dijkstra")

nx.draw(
    rede,
    posicoes,
    with_labels=True,
    node_size=2200,
    node_color="lightgreen",
    edge_color="gray",
    width=2,
    arrows=True,
    arrowsize=20,
    font_weight="bold"
)

arestas_caminho = [
    (caminho_encontrado[i], caminho_encontrado[i + 1])
    for i in range(len(caminho_encontrado) - 1)
]

nx.draw_networkx_edges(
    rede,
    posicoes,
    edgelist=arestas_caminho,
    edge_color="red",
    width=4,
    arrows=True,
    arrowsize=25
)

pesos = nx.get_edge_attributes(rede, "weight")

nx.draw_networkx_edge_labels(
    rede,
    posicoes,
    edge_labels=pesos
)

plt.axis("off")
plt.show()
