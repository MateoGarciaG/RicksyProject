

"""WEB SCRAPPING MODULE: This module consist of a serie of functions that handle HTML's content
"""

def get_scrapping_content(html_string):
    """get_scrapping_content: This function does scrapping over a html content related to Menus website to get information about a menu page.

    Args:
        html_string (str): It's the HTML's content that function will take its information about menu

    Returns:
        dict: Returns a dictionary with menu's information from result of scrapping of Menus Website's page
    """
    
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
        
        titulo = find_content(html_string, '"titulo-menu">', second_content='</h3>')[0]
        
        description = find_content(html_string, '"descripcion-menu">', second_content='</p>')[0]
        
        stock = int(find_content(html_string, '<input type="hidden" id="stock-menu" value="30">', attribute='value')[0])
        
        price = find_content(html_string, 'class="precio">', second_content='</p>')[0]
        first_position_price = price.find(' ')
        last_position_price = price.find('$', first_position_price+1)
        new_price = float(price[first_position_price+1:last_position_price])
        
        ingredients = find_content(html_string, 'class="ingredientes-menu">', second_content='</p>')[0]
        ingredients_li = get_all_labels(ingredients, 'li')
        ingredients_items = [find_content(item, '<li>', second_content='</li>')[0] for item in ingredients_li]
        
        category = find_content(html_string, 'class="tipo-menu">', second_content='</p>')[0]
        
        #* POSTCONDITIONALS
        assert isinstance(titulo, str) == True
        assert isinstance(description, str) == True
        assert isinstance(stock, int) == True
        # assert isinstance(new_price, float) == True
        assert isinstance(ingredients_items, list) == True
        assert isinstance(category, str) == True
        
        menu_content['titulo'] = titulo
        menu_content['descriptionMenu'] = description
        menu_content['stock'] = stock
        menu_content['price'] = new_price
        menu_content['ingredients'] = ingredients_items
        menu_content['category'] = category
        
    else:
        return None
    
    #* POSTCONDITIONAL
    assert isinstance(menu_content, dict) == True
    assert menu_content is not {}
    
    return menu_content
        
def find_content(html_string, first_content, second_content='', attribute=''):
    """find_content: This function find and scrapping the content that we want to get from a HTML's page. 

    Args:
        html_string (str): It's the HTML content where we want to get the information
        first_content (str): It's the first point of content where the function will begin to search content that we want to get
        second_content (str, optional): It's the last point of content where the function will search content that we want to get. Defaults to ''. Because in the case that we want to get content of a value's attribute from unique label, there's not will be obviusly a close label for example
        attribute (str, optional): It's the type of attribute that we want to select to get value's content from a attribute of a unique label. Defaults to ''. Because it's depend on if we want to get content from a unique label

    Returns:
        list: Returns a list with results of scrapping HTML's content that we specified in Args.
    """
    
    #* PRECONDITIONALS
    assert isinstance(html_string, str) == True
    assert isinstance(first_content, str) == True
    assert isinstance(second_content, str) == True
    assert isinstance(attribute, str) == True
    
    result = []
    
    if second_content == '':
        
        result.append(get_content_attribute(attribute, first_content))
        
    else:
    
        first_position = html_string.find(first_content)
        second_position = html_string.find(second_content, first_position+len(first_content))
    
        result.append(html_string[first_position+len(first_content):second_position])
    
    content_clean = []
    cont = 0
    for item_result in result:
        
        item_result_clean = item_result.split('\n')

        
        item_result_clean = ''.join(item_result_clean)

        
        item_result_clean = item_result_clean.split(' ')

        
        for elem in item_result_clean:

            if elem == '':
                continue
            else:
                content_clean.append(elem)
        
        new_content_clean = ' '.join(content_clean)
        
        #* POSTCONDICIONAL
        assert isinstance(new_content_clean, str) == True 

        result[cont] = new_content_clean
        
        content_clean = []
        
        cont += 1
        
    #* POSTCONDITIONALS
    assert isinstance(result, list) == True
    
    return result


def get_all_labels(html_string, label):
    """get_all_labels: This function get all label with their content from a HTML's content

    Args:
        html_string (str): It's the HTML content where we want to get all labels
        label (str): It's the type of label that we specified to get all labels from html's content

    Returns:
        list: Returns a list with all labels get from HTML's content where every element contains the label and its content
    """
    
    
    #* PRECONDITIONAL
    assert isinstance(html_string, str) == True
    assert isinstance(label, str) == True
    
    all_label = []
    
    label_first_position = html_string.find(f'<{label}')
    
    if label_first_position == -1:
        label_first_position = html_string.find(f'<{label}>')

    label_second_position = html_string.find(f'</{label}>', label_first_position+1)
    
    if label_second_position == -1:
        label_second_position = html_string.find(f'>', label_first_position+1)
    
    label_position = [label_first_position, label_second_position+len(label)+3]

    while label_first_position != -1 and label_second_position != -1:
        
        
        all_label.append(html_string[label_position[0]:label_position[1]])
        
        html_string = html_string[label_position[1]:]
        
        
        label_first_position = html_string.find(f'<{label}')
        
        if label_first_position == -1:
            label_first_position = html_string.find(f'<{label}>')

        
        label_second_position = html_string.find(f'</{label}>', label_first_position+1)
        
        if label_second_position == -1:
            label_second_position = html_string.find(f'>', label_first_position+1)

        
        label_position = [label_first_position, label_second_position+len(label)+3]

    
    if all_label == []:
        return 'Not Found any label'
    
    content_clean = []
    cont = 0
    for item_result in all_label:
        
        item_result_clean = item_result.split('\n')
        
        item_result_clean = ''.join(item_result_clean)
        
        item_result_clean = item_result_clean.split(' ')
        
        for elem in item_result_clean:

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

        
def get_content_attribute(attribute, label, class_label=None):
    """get_content_attribute: This function get content's attribute from a label

    Args:
        attribute (str): It's the type of attribute that we want to select to get value's content from a attribute of a label.
        label (str): It's the type of label that function needs and after get content's attribute
        class_label (str, optional): It's the class with their value. Defaults to None. It's optional because not all cases have a class.

    Returns:
        str: Returns a string with value's content of attribute from a label
    """
    
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


if __name__ == "__main__":
    
    print(get_scrapping_content.__doc__)
    print(find_content.__doc__)
    print(get_all_labels.__doc__)
    print(get_content_attribute.__doc__)