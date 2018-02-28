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
