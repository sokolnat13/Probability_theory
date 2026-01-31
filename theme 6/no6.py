import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_continuous, skew, kurtosis
from scipy import integrate


class TriangleDistribution(rv_continuous):
    def __init__(self):
        super().__init__(a=0, b=2, name='triangle_dist')

    def _pdf(self, x):
        """Плотность распределения: f(x) = (3/4)*x*(2-x) на [0, 2]"""
        result = np.zeros_like(x)
        mask = (x >= self.a) & (x <= self.b)
        result[mask] = 0.75 * x[mask] * (2 - x[mask])
        return result

    def _cdf(self, x):
        """Функция распределения"""
        result = np.zeros_like(x)

        # Для x < 0
        result[x < self.a] = 0

        # Для 0 ≤ x ≤ 2
        mask = (x >= self.a) & (x <= self.b)
        x_masked = x[mask]
        result[mask] = 0.75 * (x_masked ** 2 - x_masked ** 3 / 3)

        # Для x > 2
        result[x > self.b] = 1

        return result

    def _ppf(self, q):
        """Обратная функция распределения (квантильная функция)"""
        from scipy.optimize import fsolve

        result = np.zeros_like(q)
        for i, qi in enumerate(q):
            func = lambda x: 0.75 * (x ** 2 - x ** 3 / 3) - qi
            result[i] = fsolve(func, 1)[0]
        return result


# Создаем экземпляр распределения
tri_dist = TriangleDistribution()

# Генерация выборки
np.random.seed(42)
sample = tri_dist.rvs(size=10000)

print('f(x) = (3/4)*x*(2-x)')

# 1. Проверка условия нормировки
integral, error = integrate.quad(tri_dist.pdf, 0, 2)
print(f"Интеграл плотности на [0, 2]: {integral:.6f}")

# 2. Построение графиков
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

# График плотности
x_plot = np.linspace(-0.5, 2.5, 1000)
ax1.plot(x_plot, tri_dist.pdf(x_plot), 'b-', linewidth=2, label='Теоретическая PDF')
ax1.hist(sample, bins=50, density=True, alpha=0.5, color='orange', label='Выборка')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.set_title('Плотность вероятности')
ax1.legend()
ax1.grid(True, alpha=0.3)

# График функции распределения
ax2.plot(x_plot, tri_dist.cdf(x_plot), 'r-', linewidth=2, label='Теоретическая CDF')
ax2.hist(sample, bins=50, density=True, cumulative=True,
         alpha=0.5, color='orange', label='Выборка')
ax2.set_xlabel('x')
ax2.set_ylabel('F(x)')
ax2.set_title('Функция распределения')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 3. Вероятность попадания в интервал
# Вероятность попадания в интервал [0.5, 1.5]
prob = tri_dist.cdf(1.5) - tri_dist.cdf(0.5)
print(f"Вероятность P(0.5 ≤ X ≤ 1.5): {prob:.6f}")

#4. Числовые характеристики
mean_val = tri_dist.mean()
var_val = tri_dist.var()
std_val = tri_dist.std()

print(f"Математическое ожидание: {mean_val:.6f}")
print(f"Дисперсия: {var_val:.6f}")
print(f"Среднее квадратическое отклонение: {std_val:.6f}")

# 5. Квантили и p%-ные точки
# Квантиль уровня q = 0.25
quantile_025 = tri_dist.ppf(0.25)
print(f"Квантиль уровня q=0.25: {quantile_025:.6f}")

# p%-ная точка для x = 0.25
p_point = tri_dist.cdf(0.25) * 100
print(f"P%-ная точка для x=0.25: P(X ≤ 0.25) = {p_point:.2f}%")

#6. Коэффициент асимметрии и эксцесс
skew_val = tri_dist.stats(moments='s')
kurt_val = tri_dist.stats(moments='k')

print(f"Коэффициент асимметрии: {skew_val:.6f}")
print(f"Эксцесс: {kurt_val:.6f}")
