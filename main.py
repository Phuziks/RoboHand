from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

STATUS_FILE = 'status.txt'

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Статус</title>
</head>
<body>
    <h1>Статус: {{ status_text }}</h1>

    <p>
        <a href="/?status=on">Включить (ON)</a> |
        <a href="/?status=off">Выключить (OFF)</a>
    </p>
    
    <p>Текущий статус сохранен в файле: {{ status_file }}</p>
</body>
</html>
'''


def read_status():
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, 'r') as f:
            return f.read().strip()
    return 'OFF'


def write_status(status):
    with open(STATUS_FILE, 'w') as f:
        f.write(status)


@app.route('/')
def status():
    status_param = request.args.get('status', '').lower()

    if status_param == 'on':
        status_text = 'ON'
        write_status(status_text)
    elif status_param == 'off':
        status_text = 'OFF'
        write_status(status_text)
    else:
        status_text = read_status()

    return render_template_string(HTML_TEMPLATE, 
                                 status_text=status_text,
                                 status_file=STATUS_FILE)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
