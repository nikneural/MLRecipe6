# Даны текстовые данные с элементами HTML, и требуется извлечь только текст.

from bs4 import BeautifulSoup

html = """
       <div class='full_name'><span style='font-weight:bold'>
       Masego</span> Azra</div>"""

# Выполнить разбор html
soup = BeautifulSoup(html, 'lxml')

# Найти элемент div с классом "full_name", показать текст
print(soup.find("div", {"class": "full_name"}).text)