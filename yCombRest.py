import time, threading
from flask import Flask
from proxyParser import ProxyParser

app = Flask(__name__)
pp = ProxyParser()

def taskParser():
    while True:
        pp.runParser()
        time.sleep(5)
    

@app.route("/json")
def yCombJson():
    return pp.getJson()


if __name__ == "__main__":
    th = threading.Thread(target=taskParser)
    th.setDaemon(True)
    th.start()
    app.run(use_reloader=False)
    
