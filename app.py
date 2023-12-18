"""Aplicación para rellenar los nombres y apellidos"""
from flask import Flask,request,redirect,Response





app = Flask(__name__)

@app.route("/pizza",methods=['POST'])

def pizza():
    """Funcion que recupera nombres y apellidos"""
    nombre = request.form.get('nombreDelCliente')
    apellido =  request.form.get('apellidoDelCliente')

    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre + " " + apellido+"."+" " +
                    "Su pedido se ha realizado correctamente!!" + "\n")
        file.close()

    print(nombre, apellido,". Su pedido se ha realizado correctamente!!")
    return redirect("http://localhost/ejerciciosMaster/modulo1/111-A1/solicita_pedido.html",
                     code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """Comprueba disponibilidad de un tamaño de pizza."""
    size =  request.args.get('value')
    if size != 'S':
        return Response("Disponible", 200, {'Access-Control-Allow-Origin': '*'})
    else:
        return Response("No Disponible", 200, {'Access-Control-Allow-Origin': '*'})
           