import json
# se importa un diccionario

myRecord = {
    "name": "Jay",
    "Age": 99,
    "Occupation": "Unemployeed"
}

def convert_json(myRecord, filename):
    
    assert isinstance(myRecord, dict)
    assert isinstance(filename, str)
    mensaje = f"El diccionario ha sido convertido a json en este archivo: {filename}.json"
    try:
        j = json.dumps(myRecord)
        # para que pueda funcionar with open, la ruta empieza desde la raíz hasta la carpeta donde esta el archivo donde queremos guardar los datos
        with open(f"backend/json/{filename}.json", "w") as f: 
            f.write(j)
            # f.close()
    except json.JSONDecodeError as jsonerror:
        mensaje = "Decoding json ha fallado" 
    except FileNotFoundError as notfile:
        mensaje = "Archivo no encontrado"
    except Exception as exc:
        print("Ha ocurrido un error: ", exc.args)
    return mensaje
# de postcondición no se cual poner(pensar)
file_json = convert_json(myRecord)


