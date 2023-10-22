import random
import pandas as pd

# Генерация исходного DataFrame
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получение уникальных значений в столбце 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создание новых столбцов для каждого уникального значения и заполнение их нулями
for value in unique_values:
    data[value] = 0

# Присваивание единиц в соответствующие столбцы на основе значений в 'whoAmI'
for idx, value in enumerate(data['whoAmI']):
    data.at[idx, value] = 1

# Удаление исходного столбца 'whoAmI'
data = data.drop(columns=['whoAmI'])

# Вывод результата
data.head()

print(data.head())
