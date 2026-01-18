import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# черный фон размером 4x3
fig, ax = plt.subplots(figsize=(6, 4.5))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# границы 4x3
ax.set_xlim(0, 4)
ax.set_ylim(0, 3)

# Координаты центров нот
notes = 
[
    (0.5, 0.75),  # 1/16
    (1.75, 0.75),  # 1/16
    (3, 0.75)  # 1/8
]


heads_width = 0.4 * 1.5
heads_height = 0.3 * 1.5

for x, y in notes:
    head = patches.Ellipse((x, y), heads_width, heads_height,
                           facecolor='cyan', edgecolor='cyan', linewidth=1.5 * 1.25)
    ax.add_patch(head)

# Штили
stem_length = 1.15 * 1.5
stem_width = 0.05 * 1.5

for i, (x, y) in enumerate(notes):
    stem_x = x + heads_width / 2 - stem_width
    stem_y = y
    stem = patches.Rectangle((stem_x, stem_y), stem_width, stem_length,
                             facecolor='cyan', edgecolor='cyan')
    ax.add_patch(stem)

# Короткое ребро
beam1_y = notes[0][1] + stem_length - (0.3 * 1.5)
beam1_x_start = notes[0][0] + heads_width / 2 - stem_width
beam1_x_end = notes[1][0] + heads_width / 2
beam1_length = beam1_x_end - beam1_x_start
beam1_height = 0.1 * 1.5  # 0.15

beam1 = patches.Rectangle((beam1_x_start, beam1_y), beam1_length, beam1_height,
                          facecolor='cyan', edgecolor='cyan')
ax.add_patch(beam1)

# Длинное ребро
beam2_y = beam1_y + beam1_height + (0.1 * 1.5)
beam2_x_start = notes[0][0] + heads_width / 2 - stem_width
beam2_x_end = notes[2][0] + heads_width / 2
beam2_length = beam2_x_end - beam2_x_start
beam2_height = 0.1 * 1.5  # 0.15

beam2 = patches.Rectangle((beam2_x_start, beam2_y), beam2_length, beam2_height,
                          facecolor='cyan', edgecolor='cyan')
ax.add_patch(beam2)

ax.set_aspect('equal')


# проверка попадания в ноты
def is_in_notes(x, y):
    # головки
    for note_x, note_y in notes:
        dx = (x - note_x) / (heads_width / 2)
        dy = (y - note_y) / (heads_height / 2)
        if dx ** 2 + dy ** 2 <= 1:
            return True

    # штили
    for note_x, note_y in notes:
        stem_left = note_x + heads_width / 2 - stem_width
        stem_right = stem_left + stem_width
        stem_bottom = note_y
        stem_top = note_y + stem_length
        if stem_left <= x <= stem_right and stem_bottom <= y <= stem_top:
            return True

    # рёбра
    if (beam1_x_start <= x <= beam1_x_start + beam1_length and
            beam1_y <= y <= beam1_y + beam1_height):
        return True

    if (beam2_x_start <= x <= beam2_x_start + beam2_length and
            beam2_y <= y <= beam2_y + beam2_height):
        return True

    return False


num_darts = 1000  # количество дротиков

# случайные координаты дротиков по всей площади фона
X = np.random.uniform(0, 4, num_darts)
Y = np.random.uniform(0, 3, num_darts)

# Отслеживаем попадания
hits = 0
hit_x = []
hit_y = []
miss_x = []
miss_y = []

for i in range(num_darts):
    if is_in_notes(X[i], Y[i]):
        hits += 1
        hit_x.append(X[i])
        hit_y.append(Y[i])
    else:
        miss_x.append(X[i])
        miss_y.append(Y[i])

hit_rate = hits / num_darts

# Попадания
if hit_x:
    ax.scatter(hit_x, hit_y, color='red', s=10, marker='o', alpha=0.7, label='Попадания')

# Промахи
if miss_x:
    ax.scatter(miss_x, miss_y, color='gray', s=5, marker='o', alpha=0.3, label='Промахи')

# легенда
ax.legend(loc='upper right', fontsize=9, facecolor='black', edgecolor='white', labelcolor='white')

plt.tight_layout()
plt.show()


print(f"Всего бросков дротиков: {num_darts}")
print(f"Попаданий в ноты: {hits}")
print(f"Доля попаданий: {hit_rate:.4f} ({hit_rate:.2%})")


# Площадь всей области
total_area = 4 * 3

# площадь нот
note_head_area = np.pi * (heads_width / 2) * (heads_height / 2)
stem_area = stem_length * stem_width
beam1_area = beam1_length * beam1_height
beam2_area = beam2_length * beam2_height
notes_area = (3 * note_head_area) + (3 * stem_area) + beam1_area + beam2_area
theoretical_prob = notes_area / total_area

print(f"Площадь всей области: {total_area}")
print(f"Площадь фигуры: {notes_area:.4f}")
print(f"Теоретическая вероятность: {theoretical_prob:.4f} ({theoretical_prob:.2%})")
print(f"Разница с моделированием: {abs(hit_rate - theoretical_prob):.4f}")
