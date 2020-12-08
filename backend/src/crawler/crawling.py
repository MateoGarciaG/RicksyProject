import requests

r = requests.get("https://mateogarciag.github.io/Project-dual-website")
the_html = r.text


def get_next_target(the_html):

    # assert isinstance(the_html, str)

    start_link = (the_html).find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = the_html.find('"', start_link)
    end_quote = the_html.find('"', start_quote + 1)
    url = the_html[start_quote + 1:end_quote]
    
    assert isinstance(url, str)
    assert isinstance(end_quote, int)

    return url, end_quote

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)
    
def get_all_links(the_html):
    links = []
    

    assert isinstance(links, list)
    
    while True:
        url, endpos = get_next_target(the_html)
        if url:
            links.append(url)
            the_html = the_html[endpos:]
        else:
            break
    
    assert isinstance(links, list)
    
    return links

def crawl_web(seed):
    tocrawl = seed
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl (get_all_links(the_html(page)))
            crawled.append(page)
    return crawled

links_index = get_all_links(the_html)
htmls = crawl_web(links_index)
print(htmls)
