from flask.views import MethodView
from proxyParser import ProxyParser
import json
from lxml import etree

class BasicAPI(MethodView):
    pass


class JsonAPI(BasicAPI):
    """
    Json class api to send json content from GET request
    """
    __pp = ProxyParser()

    
    def get(self, **kwargs):
        try:
            return json.dumps(self.__pp.getData())
        except Exception, e:
            print(e)
        return d

    
    def post(self):
        return "Unknown command."

class XmlAPI(BasicAPI):
    """
    Xml class api to send xml content from GET request
    """
    __pp = ProxyParser()

    
    def get(self, **kwargs):
        d = self.__pp.getData()
        root = etree.Element("root")
        try:
            for key,val in d.iteritems():
                ch = etree.SubElement(root, key)
                if isinstance(val, list):
                    for v in val:
                        it = etree.SubElement(ch, "item")
                        for k in v.iterkeys():
                            subit = etree.SubElement(it, k)
                            subit.text = v[k]
                else:
                    ch.text=str(val)
        except Exception, e:
            print(e)
            
        return etree.tostring(root, pretty_print=True)
    

    def post(self):
        return "Unknown command."


"""
Helper functions to register json and xml to the Flask app
"""    
def addJsonAPI(app):
    app.add_url_rule('/json/', view_func=JsonAPI.as_view('json'))

    
def addXmlAPI(app):
    app.add_url_rule('/xml/', view_func=XmlAPI.as_view('xml'))
