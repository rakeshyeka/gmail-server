__author__ = 'rakesh'
from _datetime import datetime;
from Util import UrlUtil;
import inspect;

def getCurrentTime():
    return str(datetime.now());

class logger:
    logFilePointer = "";
    LOG_LOCATION = "/home/rakesh/.raspPi/";

    def __init__(self, file):
        logFile = UrlUtil.join(self.LOG_LOCATION, file);
        self.logFilePointer = open(logFile,"a");

    def logFailure(self, reason):
        logMessage = self.formatLogMessage("FAILURE", inspect.stack()[1][3], reason);
        self.logFilePointer.write(logMessage);

    def logSuccess(self, message):
        logMessage = self.formatLogMessage("SUCCESS", inspect.stack()[1][3], message);
        self.logFilePointer.write(logMessage);

    def logEvent(self, message):
        logMessage = self.formatLogMessage("EVENT", inspect.stack()[1][3], message);
        self.logFilePointer.write(logMessage);

    def formatLogMessage(self, type, scenario, message):
        message = "%s :: %s, At %s ; %s\n" % (getCurrentTime(), type, scenario, message);
        return message;

    def __del__(self):
        self.logFilePointer.close();