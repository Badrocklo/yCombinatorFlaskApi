from flask.views import MethodView
from proxyParser import ProxyParser
import json
from lxml import etree
#from pdb import set_trace as dbg

def updateApp(app):
    for sub in BasicAPI.__subclasses__():
        sub.addAPI(app)

class BasicAPI(MethodView):
    @classmethod
    def addAPI(self, app):
        raise Exception("Not implemented yet.")


class JsonAPI(BasicAPI):
    """
    Json class api to send json content from GET request
    """
    __pp = ProxyParser()

    
    def get(self, **kwargs):
        try:
            return json.dumps(self.__pp.getData())
        except Exception as e:
            print(e)
        return d

    
    def post(self):
        return "Unknown command."
    

    @classmethod
    def addAPI(self, app):
        app.add_url_rule('/json/', view_func=JsonAPI.as_view('json'))

        

class XmlAPI(BasicAPI):
    """
    Xml class api to send xml content from GET request
    """
    __pp = ProxyParser()

    
    def get(self, **kwargs):
        d = self.__pp.getData()
        root = etree.Element("root")
        try:
            for key,val in d.items():
                ch = etree.SubElement(root, key)
                if isinstance(val, list):
                    for v in val:
                        it = etree.SubElement(ch, "item")
                        for k in v.keys():
                            subit = etree.SubElement(it, k)
                            subit.text = v[k]
                else:
                    ch.text=str(val)
        except Exception as e:
            print(e)
            
        return etree.tostring(root, pretty_print=True)
    

    def post(self):
        return "Unknown command."
    

    @classmethod
    def addAPI(self, app):
        app.add_url_rule('/xml/', view_func=XmlAPI.as_view('xml'))    

