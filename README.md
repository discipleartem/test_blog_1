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

Часть 3: Пример приложения
https://pythonworld.ru/web/cgi-3.html
