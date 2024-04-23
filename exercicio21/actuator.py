from flask import Blueprint, request, render_template

actuator_blueprint = Blueprint("actuator", __name__, template_folder="templates")

atuadores = {
    'Servo':122, 
    'Lâmpada':1
}


@actuator_blueprint.route('/list_actuator')
def list_actuator():
    global atuadores
    return render_template("actuators.html", devices=atuadores)

@actuator_blueprint.route('/register_actuator')
def register_actuator():
    return render_template("register_actuator.html")

@actuator_blueprint.route('/add_actuator', methods=['POST'])
def add_actuator():
    global atuadores
    atuador = request.form.get('atuador')
    valor = request.form.get('valor')
    if atuador and valor:
        atuadores[atuador] = valor
    return render_template("actuators.html", devices=atuadores)

@actuator_blueprint.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html", devices=atuadores)

@actuator_blueprint.route('/del_actuator', methods=['POST'])
def del_actuator():
    atuador = request.form.get('atuador')
    if atuador in atuadores:
        del atuadores[atuador]
    return render_template("actuators.html", devices=atuadores)
