
from decimal import Decimal, InvalidOperation

from flask import Flask, render_template, request

app = Flask(__name__)


def leer_decimal(campo, etiqueta):
    valor = request.form.get(campo, "").strip()
    if not valor:
        raise ValueError(f"{etiqueta} es obligatorio.")

    try:
        numero = Decimal(valor)
    except InvalidOperation as error:
        raise ValueError(f"{etiqueta} debe ser un número válido.") from error

    if not numero.is_finite():
        raise ValueError(f"{etiqueta} debe ser un número válido.")
    return numero


@app.route("/")
def inicio():
    titulo = "Inicio"
    mensaje = "Bienvenido Al Portal de Servicios "
    return render_template("index.html", titulo=titulo, mensaje=mensaje)


@app.route("/Compra", methods=["GET", "POST"])
def compra():
    resultado = None
    error = None
    if request.method == "POST":
        try:
            cantidad_decimal = leer_decimal("cantidad", "La cantidad")
            if cantidad_decimal != cantidad_decimal.to_integral_value():
                raise ValueError("La cantidad debe ser un número entero.")
            if cantidad_decimal < 1:
                raise ValueError("La cantidad debe ser al menos 1.")

            precio = leer_decimal("precio", "El precio")
            if precio <= 0:
                raise ValueError("El precio debe ser mayor que cero.")

            cantidad = int(cantidad_decimal)
            subtotal = cantidad_decimal * precio
            descuento = subtotal * Decimal("0.10") if subtotal > 1000 else Decimal("0")
            resultado = {
                "cantidad": cantidad,
                "precio": precio,
                "subtotal": subtotal,
                "descuento": descuento,
                "total": subtotal - descuento,
            }
        except ValueError as exc:
            error = str(exc)

    return render_template("compra.html", resultado=resultado, error=error, valores=request.form)


@app.route("/Salario", methods=["GET", "POST"])
def salario():
    resultado = None
    error = None
    if request.method == "POST":
        try:
            horas = leer_decimal("horas", "Las horas trabajadas")
            pago_hora = leer_decimal("pago_hora", "El pago por hora")
            if horas < 0:
                raise ValueError("Las horas no pueden ser negativas.")
            if pago_hora < 0:
                raise ValueError("El pago por hora no puede ser negativo.")

            horas_normales = min(horas, Decimal("40"))
            horas_extra = max(horas - Decimal("40"), Decimal("0"))
            pago_normal = horas_normales * pago_hora
            pago_extra = horas_extra * pago_hora * Decimal("2")
            resultado = {
                "horas": horas,
                "pago_hora": pago_hora,
                "horas_normales": horas_normales,
                "horas_extra": horas_extra,
                "pago_normal": pago_normal,
                "pago_extra": pago_extra,
                "total": pago_normal + pago_extra,
            }
        except ValueError as exc:
            error = str(exc)

    return render_template("salario.html", resultado=resultado, error=error, valores=request.form)


@app.route("/Temperatura", methods=["GET", "POST"])
def temperatura():
    resultado = None
    error = None
    if request.method == "POST":
        try:
            celsius = leer_decimal("celsius", "La temperatura")
            if celsius < Decimal("-273.15"):
                raise ValueError("La temperatura no puede ser inferior al cero absoluto (-273.15 °C).")

            resultado = {
                "celsius": celsius,
                "fahrenheit": celsius * Decimal("9") / Decimal("5") + Decimal("32"),
                "kelvin": celsius + Decimal("273.15"),
            }
        except ValueError as exc:
            error = str(exc)

    return render_template("temperatura.html", resultado=resultado, error=error, valores=request.form)

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