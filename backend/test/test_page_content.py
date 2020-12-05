
from src.content_page.content_html import get_html_content

def test_get_html_content():
    
    assert get_html_content('') == None
    assert isinstance(get_html_content(''), str) == True
    assert get_html_content('') == 'There\'s no protocol HTTP/s in URL'
    