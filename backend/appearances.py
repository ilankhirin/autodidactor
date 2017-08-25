import requests
import urls_scanner
from bs4 import BeautifulSoup


URL_LIMIT = 3
def build_appearances_dict(args):
    term, all_terms, subject = args
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

    for url in safe_urls:
        try:
            print "scanning url " + url
            response = requests.get(url, verify=False)
        except BaseException as e:
            print e
            continue
        if response.status_code == 200:
            print "finished scanning " + url
            data = response.text
            page_content = str(BeautifulSoup(data).text)
            for term2 in all_terms:
                if term2 != term:
                    appearances_count = count_substring_in_string(page_content, term2)
                    if appearances_count >= 0:
                        if term2 in appearances_dict[term]:
                            appearances_dict[term][term2] += appearances_count
                        else:
                            appearances_dict[term][term2] = appearances_count


    return appearances_dict


def count_substring_in_string(string, substring):
    try:
        return string.lower().count(substring.lower())
    except BaseException as e:
        print e
        return -1


