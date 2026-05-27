from flask import Flask, request, render_template_string

app = Flask(__name__)

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

</body>
</html>
'''


@app.route('/')
def status():
    status_param = request.args.get('status', '').lower()

    if status_param == 'on':
        status_text = 'ON'
    elif status_param == 'off':
        status_text = 'OFF'
    else:
        status_text = 'OFF'

    return render_template_string(HTML_TEMPLATE, status_text=status_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)