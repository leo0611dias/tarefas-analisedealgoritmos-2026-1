Análise de Algoritmos – Dever 05
Cálculo de Complexidade
1) Algoritmo de Ordenação – Merge Sort
Divisão do problema:
Para i = 2 → (2 · m) / 2 = m
Para i = x → (x · m) / x = m
Altura da árvore:
log(n)
Custo total:
m · log(m)
Complexidade final:
O(n log n)
2) Multiplicação de Matrizes
A × B
A = M × P
B = P × N
Três loops aninhados:
→ n³
Complexidade:
O(n³)
Recorrência

T(n) = 16T(n/4) + n²

f(n) = n²
a = 16 (nº de subproblemas)
b = 4 (fator de divisão)
n^(log_b a) = n^(log₄16) = n²
Comparação:
n^(log_b a) = f(n)

→ Caso 2 do Teorema Mestre

Resultado:
T(n) = O(f(n) · log n)
T(n) = O(n² log n)
