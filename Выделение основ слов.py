# Даны лексемизированные слова, которые требуется преобразовать в их корневые
# формы.

from nltk.stem.porter import PorterStemmer

# Создать лексемы слов
tokenized_words = ['i', 'am', 'humbled', 'by', 'this', 'traditional', 'meeting']

# Создать стеммер
porter = PorterStemmer()

print([porter.stem(word) for word in tokenized_words])

# Для слов русского языка используется стеммер snowball
