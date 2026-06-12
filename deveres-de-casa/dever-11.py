class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def adicionar_aresta(self, origem, destino, peso):
        self.grafo.append([origem, destino, peso])

    def buscar_raiz(self, pai, vertice):
        if pai[vertice] != vertice:
            pai[vertice] = self.buscar_raiz(pai, pai[vertice])
        return pai[vertice]

    def unir_conjuntos(self, pai, rank, x, y):
        if rank[x] < rank[y]:
            pai[x] = y
        elif rank[x] > rank[y]:
            pai[y] = x
        else:
            pai[y] = x
            rank[x] += 1

    def arvore_geradora_maxima(self):
        resultado = []

        # Ordena as arestas do maior para o menor peso
        self.grafo.sort(key=lambda aresta: aresta[2], reverse=True)

        pai = [i for i in range(self.V)]
        rank = [0] * self.V

        for origem, destino, peso in self.grafo:

            raiz_origem = self.buscar_raiz(pai, origem)
            raiz_destino = self.buscar_raiz(pai, destino)

            if raiz_origem != raiz_destino:
                resultado.append((origem, destino, peso))
                self.unir_conjuntos(
                    pai,
                    rank,
                    raiz_origem,
                    raiz_destino
                )

            if len(resultado) == self.V - 1:
                break

        return resultado


# Exemplo de uso
g = Grafo(4)

g.adicionar_aresta(0, 1, 10)
g.adicionar_aresta(0, 2, 6)
g.adicionar_aresta(0, 3, 5)
g.adicionar_aresta(1, 3, 15)
g.adicionar_aresta(2, 3, 4)

arvore_maxima = g.arvore_geradora_maxima()

print("\n" + "=" * 40)
print(" ÁRVORE GERADORA MÁXIMA ".center(40, "="))
print("=" * 40)

print(f"{'Origem':<10}{'Destino':<10}{'Peso':<10}")
print("-" * 40)

custo_total = 0

for origem, destino, peso in arvore_maxima:
    custo_total += peso
    print(f"{origem:<10}{destino:<10}{peso:<10}")

print("-" * 40)
print(f"Custo Total da Árvore: {custo_total}")
print("=" * 40)
