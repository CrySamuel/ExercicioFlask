from flask import Flask, render_template
app= Flask(__name__)
## __name__ is the application name
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sensors')
def sensors():
    return render_template("sensors.html")

@app.route('/actuators')
def actuators():
    return render_template("actuators.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)