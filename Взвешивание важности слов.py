# Требуется мешок слов, но со словами, взвешенными по их важности для наблюдения.

# Сравнить частоту слова в документе (твит, обзор видео, стенограмма выступления
# и т. д.) с частотой слова во всех других документах, используя статистическую
# меру словарной частоты— обратной документной частоты (tf-idf). Библиотека
# scikit-leam позволяет легко это делать с помощью класса TfidfVectorizer:

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

text_data = np.array(["Бразилия - моя любовь. Бразилия!",
                      "Швеция - лучше",
                      "Германия бьет обоих"])

# Создать матрицу признаков на основе меры tf-idf
tfidf = TfidfVectorizer()
feature_matrix = tfidf.fit_transform(text_data)

# Показать матрицу признаков на основе меры tf-idf
print(feature_matrix.toarray())
print(tfidf.vocabulary_)