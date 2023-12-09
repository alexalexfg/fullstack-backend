from persistencia import  guardar_pedido



with open("pedidos.txt", "w", encoding="utf-8") as file:
    file.write("")
    file.close()


pedidos = [{"nombre: ": "Pedro", "apellidos: ": "Gil de Diego"},
           {"nombre: ": "Michael", "apellidos: ": "Jordan"}]       


for elem in pedidos:      
    for k,v in elem.items():       
        guardar_pedido(k, v)    


