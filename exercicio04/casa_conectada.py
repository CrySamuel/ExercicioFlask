from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/quarto')
def quarto():
    return render_template("quarto.html")

@app.route('/sensores_quarto')
def sensores_quarto():
    return render_template("sensores_quarto.html")

@app.route('/atuadores_quarto')
def atuadores_quarto():
    return render_template("atuadores_quarto.html")

@app.route('/banheiro')
def banheiro():
    return render_template("banheiro.html")

@app.route('/sensores_banheiro')
def sensores_banheiro():
    return render_template("sensores_banheiro.html")

@app.route('/atuadores_banheiro')
def atuadores_banheiro():
    return render_template("atuadores_banheiro.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)