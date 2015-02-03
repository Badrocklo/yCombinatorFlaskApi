import time, threading
from proxyParser import ProxyParser

class ParserRunner(object):
    time = 20

    def run(self):
        self.pp = ProxyParser()
        while True:
            self.pp.runParser()
            time.sleep(self.time)

    @classmethod
    def runParserTask(self):
        pr = ParserRunner()
        th = threading.Thread(target=pr.run)
        th.setDaemon(True)
        th.start()
        
