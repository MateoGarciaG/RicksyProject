


from src.content_page.content_html import get_html_content

def test_get_html_content():
    assert get_html_content('') == None
    assert get_html_content('github') == 'Invalid URL, try another'
    assert get_html_content('mateogarciag.github.io/Project-dual-website/') == 'There\'s no protocol HTTP/s in URL, Invalid URL \'mateogarciag.github.io/Project-dual-website/\': No schema supplied. Perhaps you mean: \'https://mateogarciag.github.io/Project-dual-website/\''