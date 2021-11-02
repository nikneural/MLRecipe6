# Даны текстовые данные, и требуется создать набор признаков, указывающих на
# количество вхождений определенного слова в текст наблюдения.

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

text_data = np.array(["Бразилия - моя любовь. Бразилия!",
                      "Швеция - лучше",
                      "Германия бьет обоих"])

# Создать матрицу признаков на основе мешка слов
count = CountVectorizer()
bag_of_words = count.fit_transform(text_data)

print(bag_of_words.toarray())
print(count.get_feature_names())