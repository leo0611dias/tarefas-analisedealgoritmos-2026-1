import heapq

# =========================================================
# Sistema simples de triagem hospitalar usando Max-Heap
# =========================================================
# Cada paciente possui um nível de dor de 1 a 10.
# Quanto maior o nível de dor, maior será a prioridade
# de atendimento.
#
# Como o heapq do Python trabalha com Min-Heap,
# utilizamos valores negativos para simular um Max-Heap.
# =========================================================

# Lista de pacientes (Nome, nível de dor)
pacientes = [
    ("Maria", 3),
    ("João", 9),
    ("Ana", 5),
    ("Pedro", 10),
    ("Carlos", 7)
]

# Criação da fila de prioridade
fila_prioridade = []

print("=== Adicionando pacientes à fila de atendimento ===\n")

# Inserindo pacientes no heap
for nome, dor in pacientes:
    
    # Inserção usando valor negativo da dor
    # Isso faz com que o maior nível de dor
    # tenha maior prioridade no atendimento
    heapq.heappush(fila_prioridade, (-dor, nome))
    
    print(f"{nome} entrou na fila com nível de dor {dor}")

print("\n=== Ordem de atendimento ===\n")

# Atendimento dos pacientes
while fila_prioridade:
    
    # Remove o paciente com maior prioridade
    dor_negativa, nome = heapq.heappop(fila_prioridade)
    
    # Convertendo novamente para valor positivo
    dor_real = -dor_negativa

    print(f"Atendendo paciente: {nome}")
    print(f"Nível de dor: {dor_real}")
    print("-" * 35)
