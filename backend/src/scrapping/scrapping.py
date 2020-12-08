
"""
    WEB SCRAPPING MODULE
"""


import requests

def get_html_content(url):
    
    #* PRECONDITIONAL
    assert isinstance(url, str) == True
    
    content_page = ''
    mensaje = ''
    
    if url != '':
        
        try:
            
            if '.' in url:
                page = requests.get(url)
            
            else:
                raise requests.exceptions.InvalidURL

        except requests.exceptions.InvalidURL as req:
            mensaje = 'Invalid URL, try another'
            
        except requests.exceptions.MissingSchema as no_http:
            mensaje = f'There\'s no protocol HTTP/s in URL, Invalid URL \'{url}\': No schema supplied. Perhaps you mean: \'https://{url}\''
            
        except requests.exceptions.HTTPError as error_http:
            mensaje = f'There was a HTPP Error'
            
        except requests.exceptions.ConnectionError as con_error:
            mensaje = f'There was a Conection Error'
            
        except Exception as exc:
            mensaje = exc.args
        
        else:
            
            #* POSTCONDITIONAL
            assert page.status_code == 200
            
            content_page = page.text
            
            return content_page

    else:
        return None
    
    return mensaje

def get_all_labels(html_string, label):
    
    #* PRECONDITIONAL
    assert isinstance(html_string, str) == True
    assert isinstance(label, str) == True
    
    all_label = []
    
    label_first_position = html_string.find(f'<{label}')
    
    if label_first_position == -1:
        label_first_position = html_string.find(f'<{label}>')
    # print(html_string[label_first_position:label_first_position+10])
    label_second_position = html_string.find(f'</{label}>', label_first_position+1)
    
    if label_second_position == -1:
        label_second_position = html_string.find(f'>', label_first_position+1)
    
    # print(html_string[label_second_position:label_second_position+10])
    label_position = [label_first_position, label_second_position+len(label)+3]
    
    # cont = 1
    while label_first_position != -1 and label_second_position != -1:
        
        
        all_label.append(html_string[label_position[0]:label_position[1]])
        
        html_string = html_string[label_position[1]:]
        
        # print(html_string)
        
        # print(html_string[label_position[1]:80])
        
        label_first_position = html_string.find(f'<{label}')
        
        if label_first_position == -1:
            label_first_position = html_string.find(f'<{label}>')
        # print(html_string[label_first_position:label_first_position+10])
        # print(label_first_position)
        
        label_second_position = html_string.find(f'</{label}>', label_first_position+1)
        
        if label_second_position == -1:
            label_second_position = html_string.find(f'>', label_first_position+1)
        # print(html_string[label_first_position:label_second_position+1])
        
        label_position = [label_first_position, label_second_position+len(label)+3]
            
        # cont += 1
    
    if all_label == []:
        return 'Not Found any label'
    
    content_clean = []
    cont = 0
    for item_result in all_label:
        
        item_result_clean = item_result.split('\n')
        
        item_result_clean = ''.join(item_result_clean)
        
        item_result_clean = item_result_clean.split(' ')
        
        for elem in item_result_clean:
            # if elem.isalnum() == False:
            if elem == '':
                continue
            else:
                content_clean.append(elem)
                
        #* POSTCONDICIONAL
        assert isinstance(content_clean, list) == True 
        
        new_content_clean = ' '.join(content_clean)
        
        #* POSTCONDICIONAL
        assert isinstance(new_content_clean, str) == True 

        all_label[cont] = new_content_clean
        
        content_clean = []
        
        cont += 1
        
    #* POSTCONDICIONAL
    assert isinstance(all_label, list) == True 
    
    return all_label

def remove_label(content, name_label, class_label='', id_label=''):
    
    #* PRECONDITIONAL
    assert isinstance(class_label, str) == True
    assert isinstance(id_label, str) == True
    
    if class_label != '' or id_label != '':
        # if f'<{name_label} class=\"{class_label}\"' in content or f'<{name_label} id=\"{id_label}\"' in content:
        if f'class=\"{class_label}\"' in content or f'id=\"{id_label}\"' in content:
            content_first_position = content.find('>')
            content_last_position = content.find(f'</{name_label}>', content_first_position+1)
            
            if content_last_position == -1:
                
                return 'This label has not its close label, it\'s one label type'
            
            else:
                
                new_content = content[content_first_position+1:content_last_position]
            
        else:
            return 'There is no class or id with that value on this label'
        
    else:
        content_first_position = content.find('>')
        content_last_position = content.find(f'</{name_label}>', content_first_position+1)
        
        if content_last_position == -1:
            return 'This label has not its close label, it\'s one label type'
                
        new_content = content[content_first_position+1:content_last_position]
        
    #* POSTCONDITIONAL
    assert isinstance(new_content, str) == True
    
    return new_content
        
def get_content_attribute(attribute, label, class_label=None):
    
    #* PRECONDITIONAL
    assert isinstance(attribute, str) == True
    assert isinstance(label, str) == True
    
    if attribute != '':
            
        if attribute in label or (attribute in label and class_label in label):
            content_first_position = label.find(f'{attribute}="')
            #* +3 debido a: =" serían: +2 y el +1 para que busque a partir de el siguiente cáracter
            content_last_position = label.find('"', content_first_position+len(attribute)+2)
                
            content = label[content_first_position+len(attribute)+2:content_last_position]
            
        else:
            return 'There is no any type of attribute in label/s'

    else:
        return 'There is no any type of attribute in label/s'
            
    #* POSTCONDITIONAL
    assert isinstance(content, str) == True
    
    return content

def find_content(html_string, label, class_label='', id_label='', attribute=''):
    #* PRECONDITIONAL
    assert isinstance(html_string, str) == True
    assert isinstance(label, str) == True
    assert isinstance(class_label, str) == True
    assert isinstance(id_label, str) == True
    assert isinstance(attribute, str) == True
    
    result = []
    content_attribute = ''
    
    all_labels = get_all_labels(html_string, label)
    
    if all_labels != 'Not Found any label':
        
        
        for item in all_labels:
    
            new_content = remove_label(item, label, class_label=class_label, id_label=id_label)
    
            if new_content == 'There is no class or id with that value on this label' or new_content == 'This label has not its close label, it\'s one label type':
                
                content_attribute = get_content_attribute(attribute, item, class_label=class_label)
                
                if content_attribute == 'There is no any type of attribute in label/s':
                    
                    continue
                else:
                    #* POSTCONDITIONAL
                    assert isinstance(content_attribute, str) == True
                    
                    result.append(content_attribute)
            else:
                #* POSTCONDITIONAL
                assert isinstance(content_attribute, str) == True
                
                result.append(new_content)
    
    #* POSTCONDITIONAL
    assert isinstance(result, list) == True
    return result

def get_scrapping_content(html_string):
    
    #* PRECONDITIONAL
    assert isinstance(html_string, str) == True
    
    menu_content = {}
    titulo = ''
    description = ''
    stock = ''
    price = ''
    ingredients = ''
    category = ''
    if html_string != '':
        
        titulo = find_content(html_string, 'h3', class_label='titulo-menu')[0]
        
        description = find_content(html_string, 'p', class_label='descripcion-menu')[0]
        
        stock = int(find_content(html_string, 'input', id_label='stock-menu',attribute='value')[0])
        
        price = find_content(html_string, 'p', class_label='precio')
        price = price[0]
        first_position_price = price.find(' ')
        last_position_price = price.find('$', first_position_price+1)
        new_price = price[first_position_price+1:last_position_price]
        
        ingredients = find_content(html_string, 'p', class_label='ingredientes-menu')
        
        ingredients = ''.join(ingredients)
        ingredients_items = find_content(ingredients, 'li')
        
        category = find_content(html_string, 'p', class_label='tipo-menu')[0]
        
        # if titulo and description
        
        menu_content['titulo'] = titulo
        menu_content['descriptionMenu'] = description
        menu_content['stock'] = stock
        # menu_content['price'] = float(new_price)
        menu_content['price'] = new_price
        menu_content['ingredients'] = ingredients_items
        menu_content['category'] = category
        
        #* POSTCONDITIONALS
        assert isinstance(titulo, str) == True
        assert isinstance(description, str) == True
        assert isinstance(stock, int) == True
        # assert isinstance(new_price, float) == True
        assert isinstance(ingredients_items, list) == True
        assert isinstance(category, str) == True
    else:
        return None
    
    assert isinstance(menu_content, dict) == True
    
    return menu_content

# def get_scrapping_content(html_string):
    
#     menu_content = {}
#     titulo = ''
#     description = ''
#     stock = ''
#     price = ''
#     ingredients = ''
#     category = ''
#     if html_string != '':
        
#         titulo = find_content(html_string, '"titulo-menu">', second_content='</h3>')[0]
        
#         description = find_content(html_string, '"descripcion-menu">', second_content='</p>')[0]
        
#         stock = find_content(html_string, '<input type="hidden" id="stock-menu" value="30">', attribute='value')[0]
        
#         price = find_content(html_string, 'class="precio">', second_content='</p>')[0]
#         first_position_price = price.find(' ')
#         last_position_price = price.find('$', first_position_price+1)
#         new_price = price[first_position_price+1:last_position_price]
        
#         ingredients = find_content(html_string, 'class="ingredientes-menu">', second_content='</p>')[0]
#         ingredients_li = get_all_labels(ingredients, 'li')
#         ingredients_items = [find_content(item, '<li>', second_content='</li>')[0] for item in ingredients_li]
        
#         category = find_content(html_string, 'class="tipo-menu">', second_content='</p>')[0]
        
#         menu_content['titulo'] = titulo
#         menu_content['descriptionMenu'] = description
#         menu_content['stock'] = int(stock)
#         menu_content['price'] = new_price
#         menu_content['ingredients'] = ingredients_items
#         menu_content['category'] = category
    
#     else:
#         return None
    
#     return menu_content
        
# def find_content(html_string, first_content, second_content='', attribute=''):
    
#     result = []
    
#     if second_content == '':
        
#         result.append(get_content_attribute(attribute, first_content))
        
#     else:
    
#         first_position = html_string.find(first_content)
#         second_position = html_string.find(second_content, first_position+len(first_content))
    
#         result.append(html_string[first_position+len(first_content):second_position])
    
#     content_clean = []
#     cont = 0
#     for item_result in result:
        
#         item_result_clean = item_result.split('\n')
#         print(item_result_clean)
        
#         item_result_clean = ''.join(item_result_clean)
#         print(item_result_clean)
        
#         item_result_clean = item_result_clean.split(' ')
#         print(item_result_clean)
        
#         for elem in item_result_clean:
#             # if elem.isalnum() == False:
#             if elem == '':
#                 continue
#             else:
#                 content_clean.append(elem)
        
#         new_content_clean = ' '.join(content_clean)
        
#         #* POSTCONDICIONAL
#         assert isinstance(new_content_clean, str) == True 

#         result[cont] = new_content_clean
        
#         content_clean = []
        
#         cont += 1
    
#     return result

if __name__ == "__main__":
    # print(get_html_content('https://mateogarciag.github.io/Project-dual-website/'))
    pass
    html_contentt = get_html_content('https://mateogarciag.github.io/Project-dual-website/comida1.html')
    
    # # print(get_scrapping_content(html_contentt))
    
    # # new_labels = get_all_labels(html_contentt, 'section')
    
    # # # print(new_labels)
    
    # class_label = remove_label('<h3 class="titulo-menu"> MENÚ: </h3>', 'h3', class_label='cualquier-clase')
    
    # print(class_label)
    
    # # new_labels = get_all_labels(html_contentt, 'h3')
    
    # # print(new_labels)
    
    # class_label = get_content_attribute('src', '<img class="logotipo" src="resources/img/calidad/logo.png" alt="">')
    
    # print(class_label)
    
    # content = find_content(html_contentt, 'button', class_label='section-calidad-boton')
    
    # # # content = find_content(html_contentt, 'div', id_label='cancel')
    
    # print(content)
    
    
    # print('*'*50)
    
    menu = get_scrapping_content(html_contentt)
    
    print(menu)