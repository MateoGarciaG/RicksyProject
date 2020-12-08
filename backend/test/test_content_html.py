
from src.content_page.content_html import get_html_content

def test_get_content_html():
    
    assert get_html_content('') == None
    assert get_html_content('http://xkcd') == 'Invalid URL, try another'
    assert get_html_content('xkcd') == 'Invalid URL, try another'
    assert get_html_content('xkcd.com/353') == 'There\'s no protocol HTTP/s in URL, Invalid URL \'xkcd.com/353\': No schema supplied. Perhaps you mean: \'http://xkcd.com/353\''