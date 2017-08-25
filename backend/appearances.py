import requests
import urls_scanner
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool


URL_LIMIT = 5
def build_appearances_dict(args):
    term, all_terms, subject = args

    # term = "html"
    # all_terms = ["html", "javascript", "css"]


    appearances_dict = {}
    appearances_dict[term] = {}
    search_results = urls_scanner.get_urls(subject + " " + term, URL_LIMIT)
    safe_urls = []
    seen_urls = []

    for url in search_results:
        baseUrl = url.split("#")[0]
        if not(baseUrl in seen_urls):
            seen_urls.append(baseUrl)
            safe_urls.append(url)
            if len(safe_urls) >= URL_LIMIT:
                break

    safe_urls = list(map(lambda url: (url, term, all_terms), safe_urls))
    pool = ThreadPool(URL_LIMIT)
    results = pool.map(process_url, safe_urls)

    pool.close()
    pool.join()

    for result in results:
        if result is None:
            continue
        for searched_term in result:
            if searched_term in appearances_dict[term]:
                appearances_dict[term][searched_term] += result[searched_term]
            else:
                appearances_dict[term][searched_term] = result[searched_term]

    return appearances_dict

def process_url(args):
    url, term, all_terms = args

    try:
        print "scanning url " + url
        response = requests.get(url, verify=False)
        print "finished scanning " + url
    except BaseException as e:
        print e
        return None

    if response.status_code != 200:
        return None

    print "Starting processsing results for " + url

    data = response.text
    page_content = str(BeautifulSoup(data).text)
    # page_content = "html5 javascript css"
    appearances = {}

    for term2 in all_terms:
        if term2 == term:
            continue
        appearances_count = count_substring_in_string(page_content, term2)
        if appearances_count >= 0:
            if term2 in appearances:
                appearances[term2] += appearances_count
            else:
                appearances[term2] = appearances_count

    print "Finished processsing results for " + url

    return appearances

def count_substring_in_string(string, substring):
    try:
        return string.lower().count(substring.lower())
    except BaseException as e:
        print e
        return -1


