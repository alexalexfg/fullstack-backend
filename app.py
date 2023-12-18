"""Aplicación para rellenar los nombres y apellidos"""
from flask import Flask,request,redirect





app = Flask(__name__)

@app.route("/pizza",methods=['POST'])

def pizza():
     """Funcion que recupera nombres y apellidos"""
     nombre = request.form.get('nombreDelCliente')
     apellido =  request.form.get('apellidoDelCliente')

     with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre + " " + apellido+"."+" " + "Su pedido se ha realizado correctamente!!" + "\n")
        file.close()

     print(nombre, apellido,". Su pedido se ha realizado correctamente!!")
     return redirect("http://localhost/ejerciciosMaster/modulo1/111-A1/solicita_pedido.html", code=302)
