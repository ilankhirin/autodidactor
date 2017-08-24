import appearances
import re
from flask import jsonify
import terms_provider
# encoding=utf8
import sys

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
    terms = terms_provider.get_final_terms(subject, 0)
    print 'terms count: ' + str(len(terms))
    terms = list(map(lambda x: remove_parentheses(x).lower().strip(), terms))
    y = appearances.build_appearances_dict(subject, terms)
    x = 4
    return jsonify(y)

app.run()






