import appearances
import re
from flask import jsonify
import terms_provider
# encoding=utf8
import sys
from multiprocessing.dummy import Pool as ThreadPool
import grequests
import urls_scanner

reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask
app = Flask(__name__)

def remove_parentheses(str):
    return re.sub(r"[\(\[].*?[\)\]]", "", str)

@app.route("/")
def asdf():
    return "asdf"

@app.route("/<subject>")
def hello(subject):
    terms = map(lambda x:remove_parentheses(x).lower().strip(), list(terms_provider.get_final_terms(subject, 0)))
    print 'terms count: ' + str(len(terms))

    # urls = get_urls(subject, terms)
    urls = get_urls(subject, terms)
    rs = (grequests.get(u, timeout=3) for u in map(lambda x: x, urls.keys()))
    responses = grequests.map(rs)
    results = []
    for response in responses:
        if response is None:
            continue
        response_url = response.url
        if response_url not in urls:
            response_url = response_url.replace("https", "http")
            if response_url not in urls:
                continue
        term = urls[response_url]
        result = appearances.build_appearances_dict(response, term, terms)
        results.append(result)

    newResults = {}
    for result in results:
        key = result.keys()[0]
        newResults[key] = result[key]

    return jsonify(newResults)


def get_urls(subject, terms):
    urls = {}
    URL_LIMIT = 3
    for term in terms:
        search_results = urls_scanner.get_urls(subject + " " + term, URL_LIMIT)
        for search_result in search_results:
            if search_result in urls:
                continue
            urls[search_result] = term
    return urls


app.run()