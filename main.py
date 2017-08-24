import appearances
import re
from flask import jsonify


from flask import Flask
app = Flask(__name__)

def remove_parentheses(str):
    return re.sub(r"[\(\[].*?[\)\]]", "", str)

@app.route("/")
def asdf():
    return "asdf"

@app.route("/<subject>")
def hello(subject):
    print subject
    subject = 'computer science'
    terms = ['GRASP', 'SOLID']

    terms = list(map(lambda x: remove_parentheses(x).lower().strip(), terms))
    y = appearances.build_appearances_dict(subject, terms)
    x = 4
    return jsonify(y)

app.run()






