from flask import Flask
from proxyParser import ProxyParser
app = Flash(__name__)
pp = ProxyParser()

@app.route("/json")
def yCombJson():
    return pp.getJson()
    
