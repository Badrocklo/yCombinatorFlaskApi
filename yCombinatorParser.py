# from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urllib2
from BeautifulSoup import BeautifulSoup as bs
from pdb import set_trace as dbg
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


# class HackerNewsRest(BaseHTTPRequestHandler):
#     def do_GET(self):
#         pass

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
            self.__data = bs(urllib2.urlopen(self.__url).read())('tr')
        except:
            logger.warning("Failed to retrieve data from url.")

    def parse(self):
        self.__datajson["items"] = []
        for i in xrange(4,len(self.__data)-5, 3):
            url = self.__data[i]('td')[2]
            item = copy.deepcopy(self.__data_item)
            item["title"] = url.a.text
            item["url"] = url.a.attrs[0][1]
            td = self.__data[i+1]
            td = td('td')
            td = td[1]
            if not td.span is None:
                tdf = self.__d.match(td.span.text)
                item["points"] = td.span.text[tdf.start():tdf.end()]
                item["postedBy"] = td('a')[0].text
                tdf = self.__d.match(td('a')[1].text)
                item["commentCount"] = td('a')[0].text[tdf.start():tdf.end()]
            self.__datajson["items"].append(item)


    def getData(self):
        return self.__datajson
