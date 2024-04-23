from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

users = {
    'user1': '1234',
    'leonadro': 'min'
}
sensores = {'Umidade':22, 'Temperatura':23, 'Luminosidade':1034}
atuadores = {'Servo':122, 'Lâmpada':1}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            return render_template('home.html')
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login.html')

@app.route('/demonstration', methods=['GET'])
def demonstration():
    return jsonify(sensores)

@app.route('/sensors')
def sensors():
    return render_template('sensors.html', devices=sensores)

@app.route('/actuators')
def actuators():
    return render_template('actuators.html', devices=atuadores)

@app.route('/register_user')
def register_user():
    return render_template("register_user.html")

@app.route('/add_user', methods=['GET','POST'])
def add_users():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
    users[user] = password
    return render_template("users.html", devices=users)

@app.route('/list_users')
def list_users():
    global users
    return render_template("users.html", devices=users)

@app.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@app.route('/add_sensor', methods=['GET','POST'])
def add_sensor():
    global users
    if request.method == 'POST':
        sensor = request.form['sensor']
        valor = request.form['valor']
    else:
        sensor = request.args.get('sensor', None)
        valor = request.args.get('valor', None)
    sensores[sensor] = valor
    return render_template("sensors.html", devices=sensores)

@app.route('/register_actuator')
def register_actuator():
    return render_template("register_actuator.html")

@app.route('/add_actuator', methods=['GET','POST'])
def add_actuator():
    global users
    if request.method == 'POST':
        atuador = request.form['atuador']
        valor = request.form['valora']
    else:
        atuador = request.args.get('atuador', None)
        valor = request.args.get('valora', None)
    atuadores[atuador] = valor
    return render_template("actuators.html", devices=atuadores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)