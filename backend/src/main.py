
#* MODULES
#* DATABASE MODULE
from database.db_conection import connetion
from bson.json_util import dumps

#* REQUEST - CONTENT_PAGE MODULE
from content_page.content_html import get_html_content

#* CONVERT TO JSON MODULE
from convert_json.convert_json import convert_json

#* CRAWEL MODULE
from crawler.crawling import crawl_web

#* WEB SCRAPPING MODULE
from scrapping.scrapping import get_scrapping_content
from bson.json_util import dumps


#*************************************************************


def execute_program():
    
    
    #* CRAWLER SECTION
    
    links_menus_web = crawl_web('https://mateogarciag.github.io/Project-dual-website')
    
    #* WEB SCRAPPING SECTION
    
    result_scrapping = []
    
    for link in links_menus_web:
        
        #* CONTENT_PAGE SECTION REQUEST
        html_string = get_html_content(link)
        
        dict_scrapping = get_scrapping_content(html_string)
        
        #* CONVERT TO JSON SECTION
        convert_to_json = convert_json(dict_scrapping, 'datos')
        
        result_scrapping.append(dict_scrapping)
    
    
    #* MONGODB SECTION
    client = connetion()              

    try:
        db_project = client['project_menus']
        menus_collection = db_project['menus']
    
        #* insert menus on database
        insert_menus = menus_collection.insert_many(result_scrapping)
    
        # #* Get all documents of menus
        # find_menus = menus_collection.find({}, {"_id":0})
    
        # #*Imprimir resultado con documentos
        # print(dumps(find_menus, indent=2))
    except Exception as err:
        print('ERROR: ', err.args)
    
    
    return result_scrapping


#*******************************************************


if __name__ == "__main__":
    
    #* Ejecuta el programa
    dicctionaries_menus = execute_program()
    
    for menus in dicctionaries_menus:
        
        print(menus)
        
        print('*'*50)