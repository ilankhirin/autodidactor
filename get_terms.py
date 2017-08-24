from bs4 import BeautifulSoup
import requests

url_base = "https://en.wikipedia.org"
category_base_url = "/wiki/Category:"

def create_url(site_url, category_extension, category):
    return site_url + category_extension + category

def get_final_terms(category, depth):
    final_terms = []

    root_category_url = create_url(url_base, category_base_url, category.replace(" ", "_"))
    root_terms, root_fetched_urls = scan_url(root_category_url)
    last_lvl_urls = root_fetched_urls

    for term in root_terms:
        final_terms.append(term)

    current_lvl_urls = []
    for i in range(depth):
        for url in last_lvl_urls:
            lvl_terms, lvl_fetched_urls = scan_url(url)
            for term in lvl_terms:
                final_terms.append(term)
            for lvl_url in lvl_fetched_urls:
                current_lvl_urls.append(lvl_url)
        last_lvl_urls = current_lvl_urls



    return set(final_terms)

def scan_url(url):
    terms = []
    categories_url = []
    log("fetching " + url)
    data = requests.get(url).text
    log("fetch " + url + " completed")
    soup = BeautifulSoup(data)
    for term in get_terms_from_soup(soup):
        terms.append(term)
    for category_url in get_categories_url(soup):
        categories_url.append(url_base + category_url)

    return terms, categories_url

def get_terms_from_soup(soup):
    possible_selectors = [".mw-category a"]
    terms = []
    for possible_selector in possible_selectors:
        terms_items = soup.select(possible_selector);
        for term in terms_items:
            if term is not None:
                terms.append(term.text)

    return terms

def get_categories_url(soup):
    possible_selectors = ["#mw-subcategories a.CategoryTreeLabel"]
    categories_url = []
    for possible_selector in possible_selectors:
        for category in soup.select(possible_selector):
            categories_url.append(category.attrs["href"])

    return categories_url;

def log(msg):
    print msg

#print get_final_terms("web development", 1)