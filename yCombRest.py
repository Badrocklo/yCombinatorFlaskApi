from flask import Flask
from parserRunner import ParserRunner
import API

app = Flask(__name__)


if __name__ == "__main__":
    ParserRunner.runParserTask()
    API.updateApp(app)
    app.run(use_reloader=False)
    
