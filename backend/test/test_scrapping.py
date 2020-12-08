
from src.content_page.content_html import get_html_content
#* FUNTIONS WEB SCRAPPING MODULE IMPORT
from src.scrapping.scrapping import  get_scrapping_content, find_content, get_all_labels, get_content_attribute

#* HTML_STRING: Contiene el string del html de comida1.html para realizar los casos test correctamente
html_string = get_html_content('https://mateogarciag.github.io/Project-dual-website/comida1.html')

def test_get_scrapping_content():
    
    assert get_scrapping_content('') == None
    assert get_scrapping_content(get_html_content('https://mateogarciag.github.io/Project-dual-website/comida1.html')) == {'titulo': 'ANDROMEDA', 'descriptionMenu': 'Andromeda és el mejor menú de este lado del universo.', 'stock': 30, 'price': '9.99', 'ingredients': ['Carne de Marte', 'Lechuga de Jupiter', 'Tomate de Pluton'], 'category': 'Comida Chatarra'}
    
    assert get_scrapping_content(get_html_content('https://mateogarciag.github.io/Project-dual-website/comida2.html')) =={'titulo': 'MILKYWAY', 'descriptionMenu': 'Sabores exóticos desde lugares desconocidos.', 'stock': 30, 'price': '8.99', 'ingredients': ['Patata de Andromeda', 'Lechuga de Jupiter', 'Sustancia 0'], 'category': 'Comida Chatarra'}
    
    assert get_scrapping_content(get_html_content('https://mateogarciag.github.io/Project-dual-website/comida3.html')) == {'titulo': 'MAKO', 'descriptionMenu': 'Este menú te dara la energía necesaria para destruir un planeta.', 'stock': 30, 'price': '4.99', 'ingredients': ['Pipas de la tierra', 'Gelatina de lenteja', 'Tomate de Pluton'], 'category': 'Comida Chatarra'}
    
    assert get_scrapping_content(get_html_content('https://mateogarciag.github.io/Project-dual-website/comida4.html')) == {'titulo': 'FUNKI', 'descriptionMenu': 'Baila al ritmo de los espamos que provoca este menú.', 'stock': 30, 'price': '5.99', 'ingredients': ['Tofu de Vega', 'Lechuga de Jupiter', 'Quarzo deshidratado'], 'category': 'Comida Chatarra'}
    


def test_find_content():
    
    assert find_content(html_string, '<input type="hidden" id="stock-menu" value="30">', attribute='value') == ['30']
    assert find_content(html_string, '"titulo-menu">', second_content='</h3>') == ['ANDROMEDA']
    assert find_content(html_string, 'class="precio">', second_content='</p>') == ['PRECIO: 9.99$']
    assert find_content(html_string, 'class="tipo-menu">', second_content='</p>') == ['Comida Chatarra']
    assert find_content(html_string, 'id="cancel">', second_content='</div>') == ['<img src="resources/svg/simbolo_eliminar_44.svg" alt="">']
    assert find_content(html_string, 'class="section-calidad-boton">', second_content='</button>') == ['<a href="https://mateogarciag.github.io/Project-dual-website/compra.html">PEDIR</a>']


def test_get_all_labels():
    
    assert get_all_labels(html_string, 'h3') == ['<h3 class="titulo-menu"> ANDROMEDA </h3>', '<h3>Lorem Ipsum</h3>']
    assert get_all_labels(html_string, 'img') == ['<img class="logotipo" src="resources/img/calidad/logo.png" alt="">', '<img src="resources/svg/simbolo_eliminar_44.svg" alt="">', '<img src="../resources/svg/escritoriomenu_icono2.ico" alt="">', 
    '<img src="resources/img/menu/comida1.png" alt="">', '<img class="iconos" src="resources/img/social_media/fb.png" alt="">', '<img class="iconos" src="resources/img/social_media/twitter2.png">', '<img class="iconos" src="resources/img/social_media/instagramm.png" alt="">', '<img src="resources/img/calidad/logo_rickMorty.JPG">']
    
    assert get_all_labels(html_string, 'p') == ['<p class="descripcion-menu"> Andromeda és el mejor menú de este lado del universo. </p>', '<p class="precio"> PRECIO: 9.99$ </p>', '<p class="ingredientes-menu"> Ingredientes: <ul> <li>Carne de Marte</li> <li>Lechuga de Jupiter</li> <li>Tomate de Pluton</li> </ul> </p>', '<p class="tipo-menu"> Comida Chatarra </p>']
    
    assert get_all_labels(html_string, 'a') == ['<a href="https://mateogarciag.github.io/Project-dual-website/index.html" class="titulo"> <img class="logotipo" src="resources/img/calidad/logo.png" alt=""> <h1> JummyFood </h1> </a>', '<a href="https://mateogarciag.github.io/Project-dual-website/menu.html">Menús</a>', '<a href="https://mateogarciag.github.io/Project-dual-website/calidad.html">Calidad</a>', '<a href="https://mateogarciag.github.io/Project-dual-website/contactos.html">Contacto</a>', '<a href="https://mateogarciag.github.io/Project-dual-website/compra.html">PEDIR</a>', '<a href=""> <img class="iconos" src="resources/img/social_media/fb.png" alt=""> </a>', '<a href=""> <img class="iconos" src="resources/img/social_media/twitter2.png"> </a>', '<a href=""> <img class="iconos" src="resources/img/social_media/instagramm.png" alt=""> </a>', '<a href="#" alt="">Políticas de Empresa </a>', '<a href="#" alt="">Derechos de autor </a>', '<a href="#" alt="">Licencia inventada del año 2013 </a>', '<a href="#" alt="">Lorem Lorem Ipsum Ipsum </a>', '<a href="#" alt="">Ipsum ipsum lorem lorem </a>', '<a href="#" alt="">Lorem Ipsum Ipsum Lorem </a>', '<a href="#"> <img src="resources/img/calidad/logo_rickMorty.JPG"> </a>']
    
    
def test_get_content_attribute():
    
    assert get_content_attribute('src', '<img class="logotipo" src="resources/img/calidad/logo.png" alt="">') == 'resources/img/calidad/logo.png'
    assert get_content_attribute('value', '<input type="hidden" name="stock-menu" value="30">') == '30'
    assert get_content_attribute('href', '<a href="#" alt="">') == '#'
    assert get_content_attribute('href', '<img class="logotipo" src="resources/img/calidad/logo.png" alt="">') == 'There is no any type of attribute in label/s'
    assert get_content_attribute('', '<img class="logotipo" src="resources/img/calidad/logo.png" alt="">') == 'There is no any type of attribute in label/s'
    