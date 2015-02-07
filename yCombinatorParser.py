import sys
if sys.version[0] == '2':
    from urllib2 import urlopen as urlopen
elif sys.version[0] == '3':
    from urllib.request import urlopen as urlopen
    
from bs4 import BeautifulSoup as bs
#from pdb import set_trace as dbg
import re
import copy

import logging

#Init logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
sh = logging.StreamHandler()
sh.setLevel(logging.WARNING)
sh.setFormatter(logging.Formatter("%(asctime)s - %(name)s | %(message)s"))
logger.addHandler(sh)


class yCombinatorParser(object):
    """
    Class which parse the html data of new.ycombinator.com website
    it organize them in a dict which follow the api.ihackernews.com
    json.
    """
    __url = "https://news.ycombinator.com/"
    __datajson = {
        "nextId":2,
        "items":
        [],
        "version":"0.1a"
    }
    __data_item = {
        "title":"",
        "url":"",
        "id":"",
        "commentCount":"",
        "points":"",
        "postedAgo":"",
        "postedBy":""
    }

    __d = re.compile("\d*")

    def __init__(self):
        self.refresh()

    def refresh(self):
        try:
            self.__data = bs(urlopen(self.__url).read())('tr')
        except:
            logger.warning("Failed to retrieve data from url.")

    def parse(self):
        """
        HTML parser the loop begin to 4 because the first 'tr'
        are used for the table title, and done to len-5 because
        the last 5 'tr' are use for More, Guidelines, blabla.
        Each items use 3 'tr'.
        """
        self.__datajson["items"] = []
        for i in range(4,len(self.__data)-5, 3):
            logger.debug("Begin loop")
            url = self.__data[i]('td')[2]
            item = copy.deepcopy(self.__data_item)
            logger.debug("Deepcopy")
            item["title"] = url.a.text
            logger.debug("Title: %s" % url.a.text)
            logger.debug("url a attrs: %s" % url.a.attrs)
            if isinstance(url.a.attrs, list):
                item["url"] = url.a.attrs[0][1]
            elif isinstance(url.a.attrs, dict):
                item["url"] = url.a.attrs['href']
            logger.debug("url: %s" % item["url"])
            td = self.__data[i+1]
            logger.debug("td1: %s" % td)
            td = td('td')
            logger.debug("td2: %s" % td)
            td = td[1]
            logger.debug("td3: %s" % td)
            if not td.span is None:
                logger.debug("span text: %s" % td.span.text)
                tdf = self.__d.match(td.span.text)
                item["points"] = td.span.text[tdf.start():tdf.end()]
                item["postedBy"] = td('a')[0].text
                tdf = self.__d.match(td('a')[1].text)
                item["commentCount"] = td('a')[0].text[tdf.start():tdf.end()]
            self.__datajson["items"].append(item)


    def getData(self):
        return self.__datajson
