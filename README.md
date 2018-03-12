# First Blog by tutorital

## Blog from Tutorital by https://pythonworld.ru/web/cgi-1.html

Работаем на Windows

Запуск встроенного веб сервера Python 3 на Linux:
    python3 -m http.server --cgi

    http://localhost:8000

Для сидящих на Windows проще будет запустить Python файл (мною немного поправленный)

    import os, sys

    from http.server import HTTPServer, CGIHTTPRequestHandler
    # Путь до корня, где лежит cgi-bin
    webdir = r'D:\путь_к_папке_проекта'
    port = 8000
    # Переходим в корневую директорию
    os.chdir(webdir)
    #localhost у нас по адресу 127.0.0.1
    srvaddr = ('127.0.0.1', port)
    srvrobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
    srvrobj.serve_forever()


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

requirements.txt
    pew==1.1.2
    pipenv==11.1.4
    psutil==5.4.3
    virtualenv==15.1.0
    virtualenv-clone==0.3.0
    gunicorn==19.7.1

Procfile
    # web: gunicorn cgi-bin:app
    # web: python index.html runserver 0.0.0.0:$PORT

    # web: gunicorn --pythonpath <directory_containing_package> <package>.<module>

    # web: gunicorn --pythonpath test_blog_1

    # 176.37.205.48 runserver 0.0.0.0:5180

    # web: gunicorn hello:app

    # gunicorn = gunicorn -w 3 test:app

    # web: gunicorn
    # gunicorn = gunicorn -w 3 app:app
----------------------------------------------------
    # web: gunicorn <main-routing-python>:app

    # web: python main.py --port=$PORT

    # web: gunicorn gettingstarted.wsgi --log-file -

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

чтобы повторить heroku ps:scale web=1 нужно дописать --app имя_приложения_в_хероку
heroku ps:scale web=1 --app aqueous-bayou-99527

чтобы открыть
 heroku open --app aqueous-bayou-99527

смотрим логи
 heroku logs --tail --app aqueous-bayou-99527

Деплой:

1) клонируем git
    $ git clone https://github.com/heroku/python-getting-started.git
    $ cd python-getting-started

2) создаем новое имя для приложения
    $ heroku create

3) самая главная команда
    $ git push heroku master

4) проверяем инстанс
    $ heroku ps:scale web=1

5) смотрим логи
    $ heroku logs --app aqueous-bayou-99527

для обновления репозитория на heroku
$ git pull git@github.com:discipleartem/test_blog_1.git

    сначала нужно перейти в папку с клонированым проэктом
    cd test_blog_1


Define a Procfile ?
https://devcenter.heroku.com/articles/getting-started-with-python#define-a-procfile

https://dashboard.heroku.com/apps

Вопрос о деплое на https://ru.stackoverflow.com
https://ru.stackoverflow.com/questions/795328/%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-gunicorn-%D0%BD%D0%B0-heroku-%D1%85%D0%BE%D1%81%D1%82%D0%B8%D0%BD%D0%B3%D0%B5-at-error-code-h14-desc-no-web-processes-r
