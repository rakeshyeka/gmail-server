__author__ = 'rakesh'
import Logger;
from Network import SMTPMail;
from Network import IMAPMail;
from Config import config;

DEFAULT_SUBJECT = "RPI status";
NETWORK_LOG_FILE = "EventLog.txt";


def updateNetworkConfig(credentials, configEntity):
    logger = Logger.logger(NETWORK_LOG_FILE);

    configString = configEntity.toString();
    SMTPMail.sendEmail(credentials, credentials.userName, DEFAULT_SUBJECT, configString);
    IMAPMail.deleteAllExceptLatestEmail(credentials);

    logger.logEvent("Configuration updated to network");


def fetchNetworkConfig(credentials):
    logger = Logger.logger(NETWORK_LOG_FILE);

    configString = IMAPMail.fetchLatestEmail(credentials);
    configEntity = config.getConfig(configString);

    logger.logEvent("Configuration fetched from network");
    return configEntity;