import time, threading
from flask import Flask
from flask.views import MethodView
from proxyParser import ProxyParser
import API

app = Flask(__name__)

def taskParser():
    pp = ProxyParser()
    while True:
        pp.runParser()
        time.sleep(20)
    

# @app.route("/json")
# def yCombJson():
#     return pp.getJson()
API.addJsonAPI(app)
API.addXmlAPI(app)


if __name__ == "__main__":
    th = threading.Thread(target=taskParser)
    th.setDaemon(True)
    th.start()
    app.run(use_reloader=False)
    
