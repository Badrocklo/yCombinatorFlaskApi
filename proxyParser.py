from yCombinatorParser import yCombinatorParser
import os
import time
import logging

#Init logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
sh = logging.StreamHandler()
sh.setLevel(logging.WARNING)
sh.setFormatter(logging.Formatter("%(asctime)s - %(name)s | %(message)s"))
logger.addHandler(sh)
    

try:
    import cPickle as pickle
except:
    import pickle

    
def dumpHelper(name, data):
    with open(name, "wb") as f:
        pickle.dump(data, f)

def loadHelper(name):
    with open(name, "rb") as f:
        return pickle.load(f)

class ProxyParser(object):
    """
    ProxyParser class use to both retrieve data from cPickle cache and 
    Save the data to the cache file
    """
    __fclist = {
        "parse":"cached/parse.dump"
        }
    __cb = yCombinatorParser()

    
    def __init__(self):
        if not os.path.exists("cached"):
            os.makedirs("cached")
        for f in self.__fclist.values():
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
            cjson = self.__cb.getData()
            logger.debug("Getjson json.")
            dumpHelper(self.__fclist["parse"], cjson)
            logger.debug("dump json.")
        except Exception as e:
            logger.warning("Failed to retrieve data.")
            logger.warning(e)
              
    
    def getData(self):
        logger.debug("Retrieve json from cache.")
        cjson = loadHelper(self.__fclist["parse"])
        return cjson
    
