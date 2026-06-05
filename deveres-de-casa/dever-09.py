import networkx as nx
import matplotlib.pyplot as plt


def calcular_menores_caminhos(arestas, quantidade_vertices, origem):
    """
    Aplica o algoritmo de Bellman-Ford para determinar
    os menores caminhos a partir de um vértice de origem.

    Retorna:
        - distâncias mínimas
        - predecessores
        - indicação de ciclo negativo
    """

    # Inicializa todas as distâncias com infinito
    distancias = {
        vertice: float("inf")
        for vertice in range(quantidade_vertices)
    }

    predecessores = {
        vertice: None
        for vertice in range(quantidade_vertices)
    }

    distancias[origem] = 0

    # Relaxamento das arestas
    for _ in range(quantidade_vertices - 1):

        houve_alteracao = False

        for origem_aresta, destino_aresta, peso in arestas:

            nova_distancia = (
                distancias[origem_aresta] + peso
            )

            if nova_distancia < distancias[destino_aresta]:
                distancias[destino_aresta] = nova_distancia
                predecessores[destino_aresta] = origem_aresta
                houve_alteracao = True

        # Encerramento antecipado se nada mudou
        if not houve_alteracao:
            break

    # Verificação de ciclos negativos
    possui_ciclo_negativo = False

    for origem_aresta, destino_aresta, peso in arestas:
        if distancias[origem_aresta] + peso < distancias[destino_aresta]:
            possui_ciclo_negativo = True
            break

    return distancias, predecessores, possui_ciclo_negativo


# -----------------------------------
# Definição do grafo
# -----------------------------------

arestas_grafo = [
    (0, 1, 5),
    (1, 2, 1),
    (1, 3, 2),
    (2, 4, 1),
    (4, 3, -1)
]

num_vertices = 5
vertice_inicial = 0

# Execução do algoritmo
distancias, predecessores, ciclo_negativo = calcular_menores_caminhos(
    arestas_grafo,
    num_vertices,
    vertice_inicial
)

# -----------------------------------
# Exibição dos resultados
# -----------------------------------

print("\n===== ALGORITMO DE BELLMAN-FORD =====")
print(f"Ciclo negativo encontrado? {ciclo_negativo}")

print("\nMenores distâncias a partir do vértice 0:")

for vertice in range(num_vertices):
    print(
        f"Vértice {vertice} | "
        f"Distância: {distancias[vertice]} | "
        f"Anterior: {predecessores[vertice]}"
    )

print("=" * 40)

# -----------------------------------
# Visualização do grafo
# -----------------------------------

grafo_visual = nx.DiGraph()

for origem, destino, peso in arestas_grafo:
    grafo_visual.add_edge(origem, destino, weight=peso)

# Organização dos vértices
posicoes = {
    0: (0, 1),
    1: (1, 2),
    2: (1, 0),
    3: (3, 2),
    4: (3, 0)
}

plt.figure(figsize=(10, 6))
plt.title("Resultado do Algoritmo de Bellman-Ford")

# Desenha os vértices
nx.draw_networkx_nodes(
    grafo_visual,
    posicoes,
    node_color="lightyellow",
    node_size=1800,
    edgecolors="black"
)

nx.draw_networkx_labels(
    grafo_visual,
    posicoes,
    font_size=13,
    font_weight="bold"
)

# Todas as arestas do grafo
nx.draw_networkx_edges(
    grafo_visual,
    posicoes,
    edge_color="gray",
    width=2,
    arrows=True,
    arrowsize=20
)

# Caminhos mínimos encontrados
arestas_menor_caminho = [
    (origem, destino)
    for destino, origem in predecessores.items()
    if origem is not None
]

nx.draw_networkx_edges(
    grafo_visual,
    posicoes,
    edgelist=arestas_menor_caminho,
    edge_color="green",
    width=4,
    arrows=True,
    arrowsize=25
)

# Destaca arestas com peso negativo
arestas_negativas = [
    (u, v)
    for u, v, peso in arestas_grafo
    if peso < 0
]

nx.draw_networkx_edges(
    grafo_visual,
    posicoes,
    edgelist=arestas_negativas,
    edge_color="orange",
    style="dashed",
    width=4,
    arrows=True,
    arrowsize=25
)

# Exibe os pesos das arestas
rotulos = nx.get_edge_attributes(
    grafo_visual,
    "weight"
)

nx.draw_networkx_edge_labels(
    grafo_visual,
    posicoes,
    edge_labels=rotulos,
    font_size=11
)

plt.axis("off")
plt.show()
