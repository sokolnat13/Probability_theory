import random
import numpy as np
import matplotlib.pyplot as plt

def toss_coin():
    return random.choice([0, 1])  # 0 - выпала решка, 1 - орёл

target_Ns = [10, 100, 500, 1000, 10000]
for N in target_Ns:
    heads = 0
    for _ in range(N):
        heads += toss_coin()
    freq = heads / N
    print(f"P({N}) = {freq:.4f}")

print(f"Классическая вероятность: 0.5000")

N_values = np.array(range(10, 10001, 50))
frequencies = []

for N in N_values:
    heads = 0
    for _ in range(N):
        heads += toss_coin()
    freq = heads / N
    frequencies.append(freq)

plt.figure(figsize=(8, 5))
plt.plot(N_values, frequencies, 'b-', label='Частота выпадения орла', linewidth=2)
plt.axhline(y=0.5, color='r', linestyle='--', label='Вероятность (0.5)', linewidth=2)
plt.xlabel('N')
plt.ylabel('P(A)')
plt.title('Моделирование связи частотного и классического определения вероятности \n на примере подбрасывания монетки')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
