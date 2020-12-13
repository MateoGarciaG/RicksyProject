
import requests
from src.content_page.content_html import get_html_content

"""CRAWLING MODULE: This module consists of a serie of functions that take HTML's content and search for every URL inside that HTML and after get into that URL and get all URL from that new HTML's content, this process repeats.
"""

#* 
def get_next_target(the_html):
    """get_next_target: This function takes a HTML's content and get the next URL inside that HTML's content

    Args:
        the_html (str): It's the HTML's content that function needs for searching the next URL

    Returns:
        (str, int): Returns two variables. First with the URL get. Second with the last position where it found the URL
    """

    # assert isinstance(the_html, str)

    start_link = (the_html).find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = the_html.find('"', start_link)
    end_quote = the_html.find('"', start_quote + 1)
    url = the_html[start_quote + 1:end_quote]
    
    #* POSTCONDITIONAL
    assert isinstance(url, str)
    assert isinstance(end_quote, int)

    return url, end_quote
    
def get_all_links(the_html):
    """get_all_links: This function get all links from a HTML's content

    Args:
        the_html (str): It's the HTML's content that function needs for searching all links

    Returns:
        list: Returns a list with all Links from HTML's content
    """
    links = []
    #* PRECONDITIONAL
    assert isinstance(links, list)
    
    while True:
        url, endpos = get_next_target(the_html)
        if url:
            links.append(url)
            the_html = the_html[endpos:]
        else:
            break
    
    #* POSTCONDITIONAL
    assert links is not []
    
    return links

def union(p, q):
    """union: This function takes a link from a list A and in the case that this link is not inside of the list B, this function put this link into list B

    Args:
        p (list): It's the first list that will receive the link from other list
        q (list): It's the second list with the link that will get into the other list
    """
    for e in q:
        if e not in p:
            p.append(e)

#* seed: lINK
def crawl_web(seed):
    """crawel_web: This function will take all link for every HTML's content of a website, into this function have a list with a serie of link that we don't want to get their links

    Args:
        seed (str): It's the index link from the website.

    Returns:
        list: Returns a list with all links related to menus pages.
    """
    tocrawl = [seed]            
    crawled = []
    no_menus = ['#','https://mateogarciag.github.io/Project-dual-website/contactos.html', 'https://mateogarciag.github.io/Project-dual-website/compra.html', 'https://mateogarciag.github.io/Project-dual-website/index.html', 'https://mateogarciag.github.io/Project-dual-website', 'https://mateogarciag.github.io/Project-dual-website/calidad.html', 'https://mateogarciag.github.io/Project-dual-website/menu.html']
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_html_content(page)))
            crawled.append(page)
            
    new_crawled = []
    for link in crawled:
        if link in no_menus:
            continue
        else:
            new_crawled.append(link)
            
    return new_crawled

if __name__ == "__main__":
    print(get_next_target.__doc__)
    print(get_all_links.__doc__)
    print(union.__doc__)
    print(crawl_web.__doc__)