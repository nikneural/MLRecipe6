# Даны текстовые данные, и требуется пометить каждое слово или символ своей
# частью речи.

from nltk import pos_tag
from nltk import word_tokenize

text_data = "Chris loved outdoor running"

text_tagged = pos_tag(word_tokenize(text_data))

# Показать части речи
print(text_tagged)

# NNP Имя собственное, единственное число
# NN Существительное, единственное число или неисчисляемое
# RB Наречие
# VBD Глагол, прошедшее время
# VBG Глагол, герундий или причастие настоящего времени
# JJ Прилагательное
# PRP Личное местоимение

# После того как текст был помечен, метки можно использовать для поиска определенных частей речи. Вот, например,
# все существительные:
print([word for word, tag in text_tagged if tag in ["NN", "NNS", "NNP", "NNPS"]])

# Более реалистичной является ситуация, когда есть данные, где каждое наблюдение
# содержит твит, и мы хотим преобразовать эти предложения в признаки отдельных
# частей речи (например, признак с 1, если присутствует собственное существительное, и 0 в противном случае):

import nltk
from sklearn.preprocessing import MultiLabelBinarizer

tweets = ["I am eating a burrito for breakfast",
          "Political science is an amazing field",
          "San Francisco is an awesom city"]

tagged_tweets = []
for tweet in tweets:
    tweet_tag = nltk.pos_tag(word_tokenize(tweet))
    tagged_tweets.append([tag for word, tag in tweet_tag])

# Применить кодирование с одним активным состоянием, чтобы конвертировать метки в признаки
one_hot_multi = MultiLabelBinarizer()
print(one_hot_multi.fit_transform(tagged_tweets))

# Применив атрибут classes , мы увидим, что каждый признак является меткой части
# речи:
print(one_hot_multi.classes_)