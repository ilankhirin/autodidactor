import requests
import urls_scanner

URL_LIMIT = 5
def build_appearances_dict(subject, terms):
    appearances_dict = {}
    for term in terms:
        print term
        appearances_dict[term] = {}
        search_results = urls_scanner.get_urls(subject + " " + term, URL_LIMIT)
        safe_urls = []
        seen_urls = []

        for url in search_results:
            print url
            baseUrl = url.split("#")[0]
            if not(baseUrl in seen_urls):
                seen_urls.append(baseUrl)
                safe_urls.append(url)
                if len(safe_urls) > URL_LIMIT:
                    break

        print safe_urls
        for url in safe_urls:
            print url
            try:
                response = requests.get(url, verify=False)
            except BaseException as e:
                print e
                continue
            if response.status_code == 200:
                page_content = unicode(response.content, errors='ignore')
                for term2 in terms:
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
        return string.lower().count(substring)
    except BaseException as e:
        print e
        return -1


