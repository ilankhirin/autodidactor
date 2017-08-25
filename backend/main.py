<<<<<<< HEAD
import sys
import re
from flask import jsonify, Flask
from flask_cors import CORS
from multiprocessing.dummy import Pool as ThreadPool
import appearances
import terms_provider
import categoryAutocomleter

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
CORS(app)

def remove_parentheses(str):
    return re.sub(r"[\(\[].*?[\)\]]", "", str)

@app.route("/")
def asdf():
    return "asdf"

@app.route("/getGraph/<subject>")
def getGraph(subject):
    terms = map(lambda x:remove_parentheses(x).lower().strip(), list(terms_provider.get_final_terms(subject, 0)))
    print 'terms count: ' + str(len(terms))
    terms_passed = list(map(lambda x: (x, terms, subject), terms))
    print terms_passed
    pool = ThreadPool(100)
    results = pool.map(appearances.build_appearances_dict, terms_passed)
    newResults = {}
    for result in results:
        key = result.keys()[0]
        newResults[key] = result[key]

    return jsonify(newResults)

@app.route("/getAutocomplete/<input>")
def getAutocomplete(input):
    options = categoryAutocomleter.getOptions(input)
    optionsDict = { "options" : options }
    return jsonify(optionsDict)

=======
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
    terms = map(lambda x:remove_parentheses(x).lower().strip(), list(terms_provider.get_final_terms(subject, 0)))
    print 'terms count: ' + str(len(terms))
    terms_passed = list(map(lambda x: (x, terms, subject), terms))
    print terms_passed
    pool = ThreadPool(100)
    results = pool.map(appearances.build_appearances_dict, terms_passed)
    newResults = {}
    for result in results:
        key = result.keys()[0]
        newResults[key] = result[key]

    return jsonify(newResults)

>>>>>>> 519f26368fc48d0aa96f82b275a9573bfb926a00
app.run()