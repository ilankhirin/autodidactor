from bs4 import BeautifulSoup
import requests

def build_url_from_term(term):
    formatted_term = term.replace(" ", "+")
    return "http://www.bing.com/search?q=" + formatted_term

def get_urls(term, limit):
    url = build_url_from_term(term)
    log("fetching " + url)
    data = requests.get(url).text
    log("fetch " + url + " completed")
    soup = BeautifulSoup(data)
    links = get_links_from_results(soup, limit)
    return links

def get_links_from_results(soup, limit):
    possible_selectors = ["#b_results .b_algo h2 a"]
    links = []
    for possible_selector in possible_selectors:
        for link_item in soup.select(possible_selector):
            if link_item is not None:
                links.append(link_item.attrs["href"])
            if len(links) > limit:
                return links

    return links

def log(msg):
    print msg