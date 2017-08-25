import appearances
import re
from flask import jsonify
import terms_provider
# encoding=utf8
import sys
from multiprocessing.dummy import Pool as ThreadPool

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
    terms = list(terms_provider.get_final_terms(subject, 0))
    print 'terms count: ' + str(len(terms))
    terms_passed = list(map(lambda x: (remove_parentheses(x).lower().strip(), terms, subject), terms[:50]))
    print terms_passed
    pool = ThreadPool(100)
    results = pool.map(appearances.build_appearances_dict, terms_passed)
    pool.close()
    pool.join()

    return jsonify(results)

app.run()