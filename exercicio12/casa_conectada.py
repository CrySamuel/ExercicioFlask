from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    dados = {'Quarto':'/quarto', 'Banheiro':'/banheiro'}
    return render_template("index.html", dados=dados)


@app.route('/quarto')
def quarto():
    quarto = {'Sensores':"/sensores_quarto", 'Atuadores':"/atuadores_quarto"}
    return render_template("quarto.html", room=quarto)

@app.route('/sensores_quarto')
def sensores_quarto():
    s = ['Sensor de Luminosidade', 'Sensor de Movimento']
    return render_template("sensores_quarto.html", sensores_quarto = s)

@app.route('/atuadores_quarto')
def atuadores_quarto():
    a = ['Interruptor', 'Lâmpadas']
    return render_template("atuadores_quarto.html", atuadores_quarto=a)

@app.route('/banheiro')
def banheiro():
    banheiro = {'Sensores':"/sensores_banheiro", 'Atuadores':"/atuadores_banheiro"}
    return render_template("banheiro.html", room=banheiro)

@app.route('/sensores_banheiro')
def sensores_banheiro():
    s = ['Sensor de Umidade', 'Sensor de Movimento']
    return render_template("sensores_banheiro.html", sensores_banheiro=s)

@app.route('/atuadores_banheiro')
def atuadores_banheiro():
    a = ['Lâmpada inteligente', 'Interruptor']
    return render_template("atuadores_banheiro.html", atuadores_banheiro=a)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)