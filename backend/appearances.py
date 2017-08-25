import requests
import urls_scanner
from bs4 import BeautifulSoup


URL_LIMIT = 3
def build_appearances_dict(response, term, all_terms):
    appearances_dict = {}
    appearances_dict[term] = {}

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


