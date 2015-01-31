from yCombinatorParser import yCombinatorParser
import os
import time
import logging

#Init logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
sh.setFormatter(logging.Formatter("%(asctime)s - %(name)s | %(message)s"))
logger.addHandler(sh)
    

try:
    import cPickle as pickle
except:
    import pickle

fcjson = "cjson.dump"
    
def dumpHelper(name, data):
    with open(name, "wb") as f:
        cPickle.dump(data, f)

def loadHelper(name):
    with open(name, "rb") as f:
        return cPickle.load(f)

class ProxyParser(object):
    __lasttime = {
        "json":0,
        "xml":0
        }
    __fclist = {
        "json":"cached/cjson.dump",
        "xml":"cached/cxml.dump"
        }
    __cb = yCombinatorParser()
    
    def getJson():
        cjson = ""
        if (os.path.getctime(fcjson) - self.__lasttime["json"])<60:
            logger.debug("Update json.")
            try:
                self.__cb.refresh()
                self.__cb.parse()
                cjson = self.__cb.getJson()
                dumpHelper(self.__fclist["json"], cjson)
            except:
                logger.debug("Failed to retrieve data.")
        else:
            logger.debug("Retrieve json from cache.")
            cjson = loadHelper(self.__fclist["json"])
        return cjson
    
