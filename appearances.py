from google import search
import requests
import itertools


def build_appearances_dict(subject, terms):
    appearances_dict = {}
    for term in terms:
        print term
        appearances_dict[term] = {}
        search_results = search(subject + " " + term, stop=5)
        search_results = itertools.islice(search_results, 5)
        for url in search_results:
            print url
            try:
                response = requests.get(url)
            except:
                pass
            if response.status_code == 200:
                page_content = response.content
                for term2 in terms:
                    if term2 != term:
                        appearances_count = page_content.lower().count(term2)
                        if term2 in appearances_dict[term]:
                            appearances_dict[term][term2] += appearances_count
                        else:
                            appearances_dict[term][term2] = appearances_count
    return appearances_dict





