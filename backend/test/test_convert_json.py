from src.convert_json.convert_json import convert_json, myRecord

def test_convert_json():
    # assert convert_json(myRecord) == "Decoding json ha fallado"
    # assert convert_json(myRecord) == "Archivo no encontrado"
    assert convert_json(myRecord, "datos") == "El diccionario ha sido convertido a json en este archivo: datos.json"
    assert convert_json(myRecord2, "datos") == "El diccionario ha sido convertido a json en este archivo: datos.json"
    assert convert_json(myRecord3, "datos") == "El diccionario ha sido convertido a json en este archivo: datos.json"






# def test_how_many():
    # convert_json 
    # assert len(convert_json) == (3)

# También se puede poner en concreto que puede salir