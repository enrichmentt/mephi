import pickle
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline

with open('model.pkl', mode='rb') as f:
    load_model = pickle.load(f)

load_model
print(f"1. Тип объекта: {type(load_model).__name__}")
print(f"2. Это Pipeline? {type(load_model).__name__ == 'Pipeline'}")


# Загружаем модель
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Получаем значения атрибутов (если их нет, будет ошибка)
try:
    dict_to_save = {
        'a': model.a,
        'b': model.b
    }

    # Сохраняем в файл
    with open('dictionary.pkl', 'wb') as f:
        pickle.dump(dict_to_save, f)

    print("Словарь успешно сохранён!")
    print(f"Содержимое: {dict_to_save}")

except AttributeError as e:
    print(f"Ошибка: в модели нет необходимых атрибутов - {e}")
    print("Доступные атрибуты модели:")
    print([attr for attr in dir(model) if not attr.startswith('_')])
