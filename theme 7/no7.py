import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
x = np.linspace(0, 5, 1000)

sigma_fixed = 0.5
for mu in [-0.5, 0, 0.5]:
    pdf = stats.lognorm.pdf(x, s=sigma_fixed, scale=np.exp(mu)) # s = σ, scale = exp(μ)
    axes[0].plot(x, pdf, label=f'μ={mu}, σ={sigma_fixed}')
axes[0].set_title('Влияние параметра μ (σ фиксировано)')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend()
axes[0].grid(True)

mu_fixed = 0
for sigma in [0.3, 0.7, 1.2]:
    pdf = stats.lognorm.pdf(x, s=sigma, scale=np.exp(mu_fixed))
    axes[1].plot(x, pdf, label=f'σ={sigma}, μ={mu_fixed}')
axes[1].set_title('Влияние параметра σ (μ фиксировано)')
axes[1].set_xlabel('x')
axes[1].set_ylabel('f(x)')
axes[1].legend()
axes[1].grid(True)
plt.tight_layout()
plt.show()

mu_true, sigma_true = 0.5, 0.8
sample = np.random.lognormal(mean=mu_true, sigma=sigma_true, size=20000)

# Теоретические значения (переименовано)
M_teor = np.exp(mu_true + sigma_true**2 / 2)
D_teor = (np.exp(sigma_true**2) - 1) * np.exp(2*mu_true + sigma_true**2)

# Выборочные значения (переименовано)
M_vybor = np.mean(sample)
D_vybor = np.var(sample)

print("LogN(μ=0.5, σ=0.8)")
print(f"μ_ln = {mu_true}, σ_ln = {sigma_true}")

print(f"M(x) = exp(μ + σ²/2) = {M_teor:.4f}")
print(f"D(x) = [exp(σ²)-1]*exp(2μ+σ²) = {D_teor:.4f}")
print(f"σ(X) = {np.sqrt(D_teor):.4f}")

print(f"M(x) ≈ {M_vybor:.4f}")
print(f"D(x) ≈ {D_vybor:.4f}")
print(f"σ(X) ≈ {np.sqrt(D_vybor):.4f}")

print("Погрешность:")
print(f"M_теор - M_выб = {abs(M_teor - M_vybor):.4f}")
print(f"D_теор - D_выб = {abs(D_teor - D_vybor):.4f}")

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(sample, bins=100, density=True, alpha=0.6, color='skyblue', label='Гистограмма X')
x_fine = np.linspace(0, np.max(sample)*0.8, 500)
pdf_fine = stats.lognorm.pdf(x_fine, s=sigma_true, scale=np.exp(mu_true))
plt.plot(x_fine, pdf_fine, 'r-', lw=2, label=f'LogN(μ={mu_true},σ={sigma_true})')
plt.title('Распределение X (логарифмически нормальное)')
plt.xlabel('x')
plt.ylabel('Плотность')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
log_sample = np.log(sample)
plt.hist(log_sample, bins=80, density=True, alpha=0.6, color='lightgreen', label='Гистограмма ln(X)')
x_norm = np.linspace(np.min(log_sample), np.max(log_sample), 300)
pdf_norm = stats.norm.pdf(x_norm, mu_true, sigma_true)
plt.plot(x_norm, pdf_norm, 'b-', lw=2, label=f'N(μ={mu_true},σ={sigma_true})')
plt.title('Распределение ln(X) (нормальное)')
plt.xlabel('ln(x)')
plt.ylabel('Плотность')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
