
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    titulo = "Inicio"
    mensaje = "Bienvenido Al Portal de Servicios "
    return render_template("index.html", titulo=titulo, mensaje=mensaje)


@app.route("/Compra")
def compra():
    titulo = "Compra"
    mensaje = "Consulta tu compra."
    return render_template("compra.html", titulo=titulo, mensaje=mensaje)


@app.route("/Salario")
def salario():
    titulo = "Salario"
    mensaje = "Consulta de Salario."
    return render_template("salario.html", titulo=titulo, mensaje=mensaje)


@app.route("/Temperatura")
def temperatura():
    titulo = "Temperatura"
    mensaje = "Consulta la temperatura."
    return render_template("temperatura.html", titulo=titulo, mensaje=mensaje)

@app.route("/Empresa")
def empresa():
    titulo = "Empresa"
    mensaje = "Consulta información sobre la empresa."
    return render_template("empresa.html", titulo=titulo, mensaje=mensaje)

@app.route("/Servicios")
def servicios():
    titulo = "Servicios"
    mensaje = "Consulta los servicios."
    return render_template("servicios.html", titulo=titulo, mensaje=mensaje)

@app.route("/Contacto")
def contacto():
    titulo = "Contacto"
    mensaje = "Aquí puedes encontrar nuestros medios de contacto."
    return render_template("contacto.html", titulo=titulo, mensaje=mensaje)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)