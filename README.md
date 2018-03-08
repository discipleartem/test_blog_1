# First Blog by tutorital

## Blog from Tutorital by https://pythonworld.ru/web/cgi-1.html

Работаем на Windows

Запуск встроенного веб сервера Python 3 на Linux:
    python3 -m http.server --cgi

    http://localhost:8000

Для сидящих на Windows чуть проще будет запуск Python файла

    from http.server import HTTPServer, CGIHTTPRequestHandler
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()

командная строка windows у меня выеживалась и мне пришлось использовать программу "git-bash.exe"
чтобы перейти в каталог и запустить скрипт на запуск сервера

Открываем localhost:8000 и видим содержимое папки проекта.При создании новых файлов мне не пришлось перегружать веб сервер

У кого проблемы с кодировкой вставляем вверху:

    # установка кодировки UTF-8
    import sys
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


Часть 4: Публикация в сети Интернет
https://pythonworld.ru/web/cgi-4.html

Я использовал heroku хостинг.
Для успешного деплоя нужно создать 2 файла:
https://devcenter.heroku.com/articles/python-support

runtime.txt
    python-3.6.4

Pipfile
    [requires]
    python_full_version = "python-3.6.4"

Procfile
    web: gunicorn app:app

и Гайд по деплою https://devcenter.heroku.com/articles/getting-started-with-python#introduction

доп. настройки для gunicorn
https://devcenter.heroku.com/articles/python-gunicorn

в консоле heroku
    pip install pipenv
    pip install gunicorn

у себя в bash консоле от git-bash.exe
   pip freeze --local  #просмотр зависимостей
   pip freeze > requirements.txt #запись в файл

в файл requirements.txt добавить строку

gunicorn==19.7.1  #версию мы узнали при установке
