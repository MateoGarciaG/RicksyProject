
#* MODULES
#* DATABASE MODULE
from src.database.db_conection import connetion
from bson.json_util import dumps

#* REQUEST - CONTENT_PAGE MODULE
from src.content_page.content_html import get_html_content

#* CONVERT TO JSON MODULE


#* CRAWEL MODULE


#* WEB SCRAPPING MODULE
from src.scrapping.scrapping import get_scrapping_content


def execute_program():
    
    #* CONTENT_PAGE SECTION
    
    
    #* CRAWLER SECTION
    
    
    
    #* WEB SCRAPPING SECTION
    
    result_scrapping = []
    
    for link in links_web:
    
        html_string = get_html_content(link)
        
        dict_scrapping = get_scrapping_content(html_string)
        
        result_scrapping.append(dict_scrapping)
        
    
    #* CONVERT TO JSON SECTION
    
    
    #* MONGODB SECTION
    client = connetion()

    db_project = client['project_menus']
    menus_collection = db_project['menus']
    
    #* insert menus on database
    insert_menus = menus_collection.insert_many(result_scrapping)
    
    #* Get all documents of menus
    find_menus = menus_collection.find({}, {"_id":0})
    
    #*Imprimir resultado con documentos
    print(dumps(find_menus, indent=2))


if __name__ == "__main__":
    
    execute_program()