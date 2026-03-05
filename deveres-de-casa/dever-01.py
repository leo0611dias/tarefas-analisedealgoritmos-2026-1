import random
import time

def insertion_sort(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = atual

tamanhos = [1000, 5000, 10000, 20000, 50000]

for n in tamanhos:
    lista = [random.randint(0, 100000) for _ in range(n)]

    lista1 = lista.copy()
    lista2 = lista.copy()

    inicio = time.time()
    insertion_sort(lista1)
    fim = time.time()
    tempo_insertion = fim - inicio

    inicio = time.time()
    sorted(lista2)
    fim = time.time()
    tempo_sorted = fim - inicio

    print(f"n = {n}")
    print(f"Insertion Sort: {tempo_insertion:.5f} s")
    print(f"sorted() (Timsort): {tempo_sorted:.5f} s")
    print("-" * 30)
