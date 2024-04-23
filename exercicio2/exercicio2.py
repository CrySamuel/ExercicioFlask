from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
<html>
    <head>
        <title>Casa conectada</title>
    </head>
    <body>
        <h1>CASA CONECTADA</h1>
        <a href="/quarto"><h1>Quarto</h1></a>
        <a href="/banheiro"><h1>Banheiro</h1></a>
    </body>
</html>
"""

@app.route('/quarto')
def quarto():
    return """
<html>
    <head>
        <title>Quarto</title>
    </head>
    <body>
        <h1>QUARTO</h1>
        <ul>
            <a href="/sensores_quarto"><li>Sensores</li></a>
            <a href="/atuadores_quarto"><li>Atuadores</li></a>
        </ul>
        <p>Voltar para <a href="/">página inicial</a>!</p>
    </body>
</html>
    """

@app.route('/atuadores_quarto')
def atuadores_quarto():
    return """
<html>
    <head>
        <title>Atuadores do Quarto</title>
    </head>
    <body>
        <h1>Atuadores</h1>
        <ul>
            <li>Interruptor</li>
        </ul>
        <p>Voltar para o <a href="/quarto">quarto</a>!</p>
    </body>
</html>
"""

@app.route('/sensores_quarto')
def sensores_quarto():
    return """
<html>
    <head>
        <title>Sensores do Banheiro</title>
    </head>
    <body>
        <h1>Sensores</h1>
        <ul>
            <li>Sensor de Umidade</li>
        </ul>
        <p>Voltar para o <a href="/banheiro">banheiro</a>!</p>
    </body>
</html>
"""

@app.route('/banheiro')
def banheiro():
    return """
<html>
    <head>
        <title>Banheiro</title>
    </head>
    <body>
        <h1>BANHEIRO</h1>
        <ul>
            <a href="/sensores_banheiro"><li>Sensores</li></a>
            <a href="/atuadores_banheiro"><li>Atuadores</li></a>
        </ul>
        <p>Voltar para <a href="/">página inicial</a>!</p>
    </body>
</html>
    """

@app.route('/atuadores_banheiro')
def atuadores_banheiro():
    return """
<html>
    <head>
        <title>Atuadores do Banheiro</title>
    </head>
    <body>
        <h1>Atuadores</h1>
        <ul>
            <li>Lâmpada inteligente</li>
        </ul>
        <p>Voltar para o <a href="/banheiro">banheiro</a>!</p>
    </body>
</html>
"""

@app.route('/sensores_banheiro')
def sensores_banheiro():
    return """
<html>
    <head>
        <title>Sensores do Banheiro</title>
    </head>
    <body>
        <h1>Sensores</h1>
        <ul>
            <li>Sensor de Umidade</li>
        </ul>
        <p>Voltar para o <a href="/banheiro">banheiro</a>!</p>
    </body>
</html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)