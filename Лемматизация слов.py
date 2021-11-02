# Даны лексемизированные слова, которые требуется собрать в синонимические
# ряды.

from nltk.stem import WordNetLemmatizer

# Создать лексемы слов
tokenized_words = ['go', 'went', 'gone', 'am', 'are', 'is', 'was', 'were']

# Создать лемматизатор
lemmatizer = WordNetLemmatizer()

# Применить лемматизатор
print([lemmatizer.lemmatize(word, pos='v') for word in tokenized_words])