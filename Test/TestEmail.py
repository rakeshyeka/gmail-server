__author__ = 'rakesh'
from Config import config;
from Credentials import credentials;
from InterfaceHandler import NetworkHandler;

def testFunction():
    myCredentials = credentials("test@gmail.com", "testPassword");
    myConfig = config({'port1':True});
    NetworkHandler.updateNetworkConfig(myCredentials,myConfig);
    responseConfig = NetworkHandler.fetchNetworkConfig(myCredentials);
    print(responseConfig.toString());
testFunction();