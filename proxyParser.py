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
        pickle.dump(data, f)

def loadHelper(name):
    with open(name, "rb") as f:
        return pickle.load(f)

class ProxyParser(object):
    __fclist = {
        "json":"cached/cjson.dump",
        "xml":"cached/cxml.dump"
        }
    __cb = yCombinatorParser()

    
    def __init__(self):
        if not os.path.exists("cached"):
            os.makedirs("cached")
        for f in self.__fclist.itervalues():
            if not os.path.exists(f):
                with open(f, "w") as ft:
                    logger.debug("File %s created." % f)

    def runParser(self):
        logger.debug("Update json.")
        try:
            self.__cb.refresh()
            logger.debug("Refresh json.")
            self.__cb.parse()
            logger.debug("Parse json.")
            cjson = self.__cb.getJson()
            logger.debug("Getjson json.")
            dumpHelper(self.__fclist["json"], cjson)
            logger.debug("dump json.")
        except Exception ,e:
            logger.debug("Failed to retrieve data.")
            logger.debug(e)
    
                              
    
    def getJson(self):
        logger.debug("Retrieve json from cache.")
        cjson = loadHelper(self.__fclist["json"])
        return cjson
    
