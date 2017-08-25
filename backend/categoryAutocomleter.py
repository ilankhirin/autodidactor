import requests

AUTOCOMPLETE_URL = "https://en.wikipedia.org/w/api.php"
AUTOCOMPLETE_PARAMS = {
    "action": "opensearch",
    "format": "json",
    "formatversion": 2,
    "search": "",
    "namespace": 0,
    "limit": 10,
    "suggest": "true"
}
CATEGORY_PREFIX = "Category:"

def getOptions(text):
    requestParams = AUTOCOMPLETE_PARAMS
    requestParams["search"] = CATEGORY_PREFIX + text
    response = requests.get(AUTOCOMPLETE_URL, params=requestParams)
    resCont = response.content
    resContList = eval(resCont)
    resOpts = resContList[1]
    options = map(removeCategoryPrefix, resOpts)
    return options

def removeCategoryPrefix(text):
    textWithoutPrefix = text.replace(CATEGORY_PREFIX, "")
    return textWithoutPrefix