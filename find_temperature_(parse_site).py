'''
До начала запуска выполнить:
pip install bs4
pip install lxml
'''
from bs4 import BeautifulSoup #библиотека, которая позволяет работать с HTML- и XML-кодом
import requests #помогает сделать запрос на нужный нам адрес сайта

#Сохраняем в переменную URL-адрес страницы, с которой мы планируем парсить информацию
url = 'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526'
response = requests.get(url)
#выводим код всей страницы
bs4 = BeautifulSoup(response.text,"lxml")
print(bs4)
#выводим необходимый тэг со страницы, где указана температура (определяем через F12 на нашей странице и наводим на нужный раздел в дереве тэгов)
temp = bs4.find('span', 'temp__value temp__value_with-unit')
print(temp)
#выведем только температуру без лишней информации
print(temp.text)
