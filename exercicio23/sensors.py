from flask import Blueprint, request, render_template

sensor_blueprint = Blueprint("sensor", __name__, template_folder="templates")

sensores = {
    'Umidade':22, 
    'Temperatura':23, 
    'Luminosidade':1034
    }

@sensor_blueprint.route('/list_sensors')
def list_sensors():
    global sensores
    return render_template("sensors.html", devices=sensores)

@sensor_blueprint.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@sensor_blueprint.route('/add_sensor', methods=['POST'])
def add_sensor():
    global sensores
    sensor = request.form.get('sensor')
    valor = request.form.get('valor')
    if sensor and valor:
        sensores[sensor] = valor
    return render_template("sensors.html", devices=sensores)

@sensor_blueprint.route('/remove_sensor')
def remove_sensor():
    return render_template("remove_sensor.html", devices=sensores)

@sensor_blueprint.route('/del_sensor', methods=['POST'])
def del_sensor():
    sensor = request.form.get('sensor')
    if sensor in sensores:
        del sensores[sensor]
    return render_template("sensors.html", devices=sensores)
