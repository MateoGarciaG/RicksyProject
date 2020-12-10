from src.convert_json.convert_json import convert_json
from src.scrapping.scrapping import get_scrapping_content
from src.content_page.content_html import get_html_content
import pytest


"""
CASES TEST JSON
"""

@pytest.mark.convert_json
def test_convert_json():
    
    links = ['https://mateogarciag.github.io/Project-dual-website/comida1.html', 'https://mateogarciag.github.io/Project-dual-website/comida2.html', 'https://mateogarciag.github.io/Project-dual-website/comida3.html']
    
    dict_menus = []
    for link in links:
        html_string = get_html_content(link)
        dict_menus.append(get_scrapping_content(html_string))
    
    assert convert_json(dict_menus[0], "datos") == "El diccionario ha sido convertido a json en este archivo: datos.json"
    assert convert_json(dict_menus[1], "datos") == "El diccionario ha sido convertido a json en este archivo: datos.json"
    assert convert_json(dict_menus[2], "datos") == "El diccionario ha sido convertido a json en este archivo: datos.json"






# def test_how_many():
    # convert_json 
    # assert len(convert_json) == (3)

# También se puede poner en concreto que puede salir