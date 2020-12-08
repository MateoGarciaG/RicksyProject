from src.crawler.crawling import get_next_target, get_all_links, the_html

def test_html_string():
    (url, end_quote,) = get_next_target(the_html)
    assert isinstance(url, str) == True
    assert isinstance(end_quote, int) == True
    # assert isinstance(start_quote, int) == True
    # assert isinstance(start_link, int) == True

def test_list_links():
    (links) = get_all_links(the_html)
    assert isinstance(links, list) == True

def test_list_number():
    (links) = get_all_links(the_html)
    assert len(links) == (4) ##número de links que hay que sacar

def test_wewant_exact():
    (links) = get_all_links(the_html)
    assert (links) == ['index.html', 'menu.html', 'calidad.html', 'contactos.html']

# def test_list_crawled():
    # (crawled) = crawl_web(the_html)
    # assert isinstance(crawled, list) == True

# def test_crawled_number():
    # (crawled) = crawl_web(the_html)
    # assert (crawled) == [0]



##PARA LA FUNCIÓN GET_ALL_LINKS
##1er, en caso de que la lista con links esté vacia.
##2ndo, colocar todos los links directamente en un caso test
##3er, preimer elemento de la lista de los links no esté vacío o sea el que esperemos