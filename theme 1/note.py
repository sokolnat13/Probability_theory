import matplotlib.pyplot as plt
import matplotlib.patches as patches

# чёрный фон 4х3
fig, ax = plt.subplots(figsize=(4, 3))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# границы 4x3
ax.set_xlim(0, 4)
ax.set_ylim(0, 3)


# Координаты цертров нот
notes = [
    (0.5, 0.75),  # 1/16
    (1.75, 0.75),  # 1/16
    (3, 0.75)   # 1/8
]

heads_width = 0.4 * 1.5
heads_height = 0.3 * 1.5

for x, y in notes:
    head = patches.Ellipse((x, y), heads_width, heads_height, facecolor='cyan', edgecolor='cyan', linewidth=1.5 * 1.25)
    ax.add_patch(head)

# для штилей
stem_length = 1.15 * 1.5
stem_width = 0.05 * 1.5

for i, (x, y) in enumerate(notes):
    stem_x = x + heads_width/2 - stem_width
    stem_y = y
    stem = patches.Rectangle((stem_x, stem_y), stem_width, stem_length, facecolor='cyan', edgecolor='cyan')
    ax.add_patch(stem)

# короткое ребро (между 1/16)
beam1_y = notes[0][1] + stem_length - (0.3 * 1.5)
beam1_x_start = notes[0][0] + heads_width/2 - stem_width
beam1_x_end = notes[1][0] + heads_width/2
beam1_length = beam1_x_end - beam1_x_start
beam1_height = 0.1 * 1.5  # 0.125

beam1 = patches.Rectangle((beam1_x_start, beam1_y), beam1_length, beam1_height, facecolor='cyan', edgecolor='cyan')
ax.add_patch(beam1)

# длинное ребро
beam2_y = beam1_y + beam1_height + (0.1 * 1.5)
beam2_x_start = notes[0][0] + heads_width/2 - stem_width
beam2_x_end = notes[2][0] + heads_width/2
beam2_length = beam2_x_end - beam2_x_start
beam2_height = 0.1 * 1.5  # 0.125

beam2 = patches.Rectangle((beam2_x_start, beam2_y), beam2_length, beam2_height, facecolor='cyan', edgecolor='cyan')
ax.add_patch(beam2)


ax.set_aspect('equal')

plt.tight_layout()
plt.show()
