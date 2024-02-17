# Парсер номеров с Web-страниц на Python

Этот проект представляет собой скрипт на языке Python, который позволяет извлекать и парсить номера телефонов с Web-страниц. Для этого используются библиотеки re, requests и beautifulsoup4.

## Установка зависимостей

Для установки необходимых зависимостей можно воспользоваться следующими командами:

`pip3 install -r requirements.txt`


## Использование

1. Сначала необходимо загрузить Web-страницу, с которой вы хотите извлечь номера телефонов, с помощью библиотеки requests, просто указав URL.
2. Затем используется библиотеку *beautifulsoup4* для парсинга HTML-кода страницы и извлечения нужной информации.
3. Далее применяются регулярные выражения из библиотеки *re* для поиска и извлечения номеров телефонов из текста.


## Лицензия

Этот проект распространяется под лицензией MIT. Подробности можно найти в файле LICENSE.