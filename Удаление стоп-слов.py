# Имеются лексемизированные текстовые данные, из которых требуется удалить
# чрезвычайно общеупотребительные слова (например, a, is, o f on), несущие в себе
# мало информации.

# Использовать функцию stopwords библиотеки N LTK :
from nltk.corpus import stopwords

tokenized_words = ['i',
                   'am',
                   'going',
                   'to',
                   'go',
                   'to',
                   'the',
                   'store',
                   'and',
                   'park']

# Загрузить стоп-слова
stop_words = stopwords.words('english')
print([word for word in tokenized_words if word not in stop_words])

# Для удаления русских стоп-слов следует просто поменять аргумент функции:

# Обратите внимание, что функция stopwords библиотеки N L T K исходит из того, что
# все лексемизированные слова находятся в нижнем регистре.
