__author__ = 'rakesh'
import json;
import inspect;


class config(object):
    port1 = False;
    port2 = False;
    port3 = False;
    port4 = False;

    def __init__(self, configDict=None):
        if(configDict != None):
            self.__dict__.update(configDict)
            for key, val in configDict.items():
                if isinstance(val, dict):
                    self.__dict__[key] = config(val);
                else:
                    self.__dict__[key] = val;

    def toString(self):
        pr = {}
        for name in dir(self):
            value = getattr(self, name)
            if not name.startswith('__') and not inspect.ismethod(value):
                pr[name] = value
        return json.dumps(pr);

    def getConfig(configString):
        configDict = json.loads(configString);
        return config(configDict);