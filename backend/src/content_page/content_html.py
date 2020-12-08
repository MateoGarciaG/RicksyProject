
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
            mensaje = f'There\'s no protocol HTTP/s in URL, Invalid URL \'{url}\': No schema supplied. Perhaps you mean: \'http://{url}\''
            
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



if __name__ == "__main__":
    pass