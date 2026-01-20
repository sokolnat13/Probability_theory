import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', encoding='windows-1251', sep=';')

# print(df.shape)
# print(df.head())

# удалить пробелы
df.columns = df.columns.str.strip()

# print(df.columns.tolist())

print('Простые вероятности')
print('Вероятность испытывать разные уровни стресса:')
for freq in sorted(df['How often do you feel stressed due to studies?'].unique()):
    P_freq = (df['How often do you feel stressed due to studies?'] == freq).mean()
    print(f"P('{freq}') = {P_freq:.3f}")

print('\nУсловные вероятности')

print('Вероятность часто испытывать стресс, будучи женщиной')
print('1. По формуле: P(Often | Female) = P(Often & Female) / P(Female)')
P_Female = (df['Gender'] == 'Female').mean()
P_Often_and_Female = ((df['How often do you feel stressed due to studies?'] == 'Often') & (df['Gender'] == 'Female')).mean()
P_Often_if_Female = P_Often_and_Female / P_Female
print(f'{P_Often_if_Female:.3f} ({P_Often_if_Female:.1%})')

print('2. Через фильтрацию датасета')
women = df[df['Gender'] == 'Female']
P_Often_if_Female_filter = (women['How often do you feel stressed due to studies?'] == 'Often').mean()
print(f"{P_Often_if_Female_filter:.3f} ({P_Often_if_Female_filter:.1%})")

print('Вероятность часто испытывать стресс, будучи мужчиной')
print('1. По формуле: P(Often | Male) = P(Often & Male) / P(Male)')
P_Male = (df['Gender'] == 'Male').mean()
P_Often_and_Male = ((df['How often do you feel stressed due to studies?'] == 'Often') & (df['Gender'] == 'Male')).mean()
P_Often_if_Male = P_Often_and_Male / P_Male
print(f'{P_Often_if_Male:.3f} ({P_Often_if_Male:.1%})')

print('2. Через фильтрацию датасета')
men = df[df['Gender'] == 'Male']
P_Often_if_Male_filter = (men['How often do you feel stressed due to studies?'] == 'Often').mean()
print(f"{P_Often_if_Male_filter:.3f} ({P_Often_if_Male_filter:.1%})")

print('\nПолная вероятность')
print('Вероятность часто испытывать стресс')
print('1. По формуле P(Often) = P(Often|Female) × P(Female) + P(Often|Male) × P(Male)')
P_Female_Often = P_Often_if_Female * P_Female
P_Male_Often = P_Often_if_Male * P_Male
P_Often = P_Female_Often + P_Male_Often
print(f"{P_Often:.3f} ({P_Often:.1%})")
print('2. Через фильтрацию датасета')
P_Often_direct = (df['How often do you feel stressed due to studies?'] == 'Often').mean()
print(f'{P_Often_direct:.3f} ({P_Often:.1%})')

print('\nФормула Байеса\nКакова вероятность того, что причина частого стресса - экзамены?')
print('P(Exams | Often) = P(Often | Exams) × P(Exams) / P(Often)')

df['Clean_Cause'] = df['What is the main cause of your academic stress?'].str.lower()
df['Is_Exam'] = df['Clean_Cause'].str.contains('exam|test|grade|testing|paper')

P_Often = (df['How often do you feel stressed due to studies?'] == 'Often').mean()
P_Exam = df['Is_Exam'].mean()
P_Often_given_Exam = df[df['Is_Exam']]['How often do you feel stressed due to studies?'].eq('Often').mean()

P_Exam_given_Often = (P_Often_given_Exam * P_Exam) / P_Often

print(f'P(Often) = {P_Often:.3f}')
print(f'P(Экзамены) = {P_Exam:.3f}')
print(f'P(Often | Экзамены) = {P_Often_given_Exam:.3f}')
print(f'P(Экзамены | Often) = [{P_Often_given_Exam:.3f} × {P_Exam:.3f}] / {P_Often:.3f}= {P_Exam_given_Often:.3f} ({P_Exam_given_Often:.1%})')
