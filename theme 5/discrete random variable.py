import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, geom, hypergeom
import math


print("ПРИМЕРЫ ДСВ")
print("Количество посетителей кафе за день в разных условиях")

fig = plt.figure(figsize=(16, 12))

print("\n")
print("1. БИНОМИАЛЬНОЕ РАСПРЕДЕЛЕНИЕ")
print("Каждый из n прохожих независимо решает зайти в кафе с вероятностью p")

n_binom = 100
p_binom = 0.03
k_values_binom = np.arange(0, 21)
probs_binom = binom.pmf(k_values_binom, n_binom, p_binom)

M_binom = n_binom * p_binom
D_binom = n_binom * p_binom * (1 - p_binom)
sigma_binom = math.sqrt(D_binom)
mode_binom = math.floor((n_binom + 1) * p_binom)

ax1 = plt.subplot(2, 2, 1)
ax1.bar(k_values_binom, probs_binom, alpha=0.7, color='blue', edgecolor='black')
ax1.axvline(x=M_binom, color='red', linestyle='--', linewidth=2, alpha=0.7,label=f'M(X)={M_binom:.2f}')
ax1.set_title(f'Биномиальное распределение\nn={n_binom}, p={p_binom}', fontweight='bold')
ax1.set_xlabel('Число посетителей из 100 прохожих')
ax1.set_ylabel('P(X=k)')
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.legend()

print(f"Параметры: n={n_binom}, p={p_binom}")
print(f"M(X) = {M_binom:.4f}, D(X) = {D_binom:.4f}, σ = {sigma_binom:.4f}, Мода = {mode_binom}")

print("\n")
print("2. РАСПРЕДЕЛЕНИЕ ПУАССОНА")
print("Посетители приходят случайно со средней интенсивностью λ")

lam = 10
k_values_poisson = np.arange(0, 26)
probs_poisson = poisson.pmf(k_values_poisson, lam)

M_poisson = lam
D_poisson = lam
sigma_poisson = math.sqrt(lam)
mode_poisson = math.floor(lam)

ax2 = plt.subplot(2, 2, 2)
ax2.bar(k_values_poisson, probs_poisson, alpha=0.7, color='green', edgecolor='black')
ax2.axvline(x=M_poisson, color='red', linestyle='--', linewidth=2, alpha=0.7,label=f'M(X)={M_poisson:.2f}')
ax2.set_title(f'Распределение Пуассона\nλ={lam}', fontweight='bold')
ax2.set_xlabel('Число посетителей за день')
ax2.set_ylabel('P(X=k)')
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.legend()

print(f"Параметры: λ={lam}")
print(f"M(X) = {M_poisson:.4f}, D(X) = {D_poisson:.4f}, σ = {sigma_poisson:.4f}, Мода = {mode_poisson}")


print("\n")
print("3. ГЕОМЕТРИЧЕСКОЕ РАСПРЕДЕЛЕНИЕ")
print("Номер посетителя, который окажется первым VIP-клиентом")

p_geom = 0.1
k_values_geom = np.arange(1, 21)
probs_geom = geom.pmf(k_values_geom, p_geom)

M_geom = 1 / p_geom
D_geom = (1 - p_geom) / (p_geom ** 2)
sigma_geom = math.sqrt(D_geom)
mode_geom = 1

# Третий график
ax3 = plt.subplot(2, 2, 3)
ax3.bar(k_values_geom, probs_geom, alpha=0.7, color='red', edgecolor='black')
ax3.axvline(x=M_geom, color='red', linestyle='--', linewidth=2, alpha=0.7, label=f'M(X)={M_geom:.2f}')
ax3.set_title(f'Геометрическое распределение\np={p_geom}', fontweight='bold')
ax3.set_xlabel('Номер посетителя (первый VIP)')
ax3.set_ylabel('P(X=k)')
ax3.grid(True, alpha=0.3, linestyle='--')
ax3.legend()

print(f"Параметры: p={p_geom}")
print(f"M(X) = {M_geom:.4f}, D(X) = {D_geom:.4f}, σ = {sigma_geom:.4f}, Мода = {mode_geom}")

print("\n")
print("4. ГИПЕРГЕОМЕТРИЧЕСКОЕ РАСПРЕДЕЛЕНИЕ")
print("Число довольных посетителей среди случайной выборки опрошенных")

N = 50
K = 35
n = 10

k_min = max(0, n - (N - K))
k_max = min(n, K)
k_values_hyper = np.arange(k_min, k_max + 1)
probs_hyper = hypergeom.pmf(k_values_hyper, N, K, n)

M_hyper = n * (K / N)
D_hyper = n * (K / N) * ((N - K) / N) * ((N - n) / (N - 1))
sigma_hyper = math.sqrt(D_hyper)
mode_hyper = k_values_hyper[np.argmax(probs_hyper)]

ax4 = plt.subplot(2, 2, 4)
ax4.bar(k_values_hyper, probs_hyper, alpha=0.7, color='purple', edgecolor='black')
ax4.axvline(x=M_hyper, color='red', linestyle='--', linewidth=2, alpha=0.7, label=f'M(X)={M_hyper:.2f}')
ax4.set_title(f'Гипергеометрическое распределение\nN={N}, K={K}, n={n}', fontweight='bold')
ax4.set_xlabel('Число довольных среди опрошенных')
ax4.set_ylabel('P(X=k)')
ax4.grid(True, alpha=0.3, linestyle='--')
ax4.legend()

print(f"Параметры: N={N}, K={K}, n={n}")
print(f"M(X) = {M_hyper:.4f}, D(X) = {D_hyper:.4f}, σ = {sigma_hyper:.4f}, Мода = {mode_hyper}")

plt.suptitle('Многоугольники распределения дискретных случайных величин\n(Тема: Посетители кафе)', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()


header = f"{'Распределение':<25} {'Параметры':<30} {'M(X)':<10} {'D(X)':<10} {'σ(X)':<10} {'Мода':<10}"
print("\n" + header)
print("-" * 95)

distributions_info = \
[
    ("Биномиальное", f"n={n_binom}, p={p_binom}", M_binom, D_binom, sigma_binom, mode_binom),
    ("Пуассона", f"λ={lam}", M_poisson, D_poisson, sigma_poisson, mode_poisson),
    ("Геометрическое", f"p={p_geom}", M_geom, D_geom, sigma_geom, mode_geom),
    ("Гипергеометрическое", f"N={N}, K={K}, n={n}", M_hyper, D_hyper, sigma_hyper, mode_hyper)
]

for name, params, M, D, sigma, mode in distributions_info:
    print(f"{name:<25} {params:<30} {M:<10.3f} {D:<10.3f} {sigma:<10.3f} {mode:<10}")


plt.show()
