from flask import Flask
from proxyParser import ProxyParser
app = Flask(__name__)
pp = ProxyParser()

@app.route("/json")
def yCombJson():
    print("Request")
    return pp.getJson()


if __name__ == "__main__":
    app.run()
    
