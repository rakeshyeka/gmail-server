__author__ = 'rakesh'
import smtplib;
import Logger;
import email;

SMTP_LOG_FILE = "SMTPLog.txt";


def sendEmail(credentials, address, subject, message):
    logger = Logger.logger(SMTP_LOG_FILE);
    result = False;
    try:
        userName = credentials.userName;
        password = credentials.password;
        smtpServer = getGmailSMTPServer(userName, password);
        formattedMessage = formatMessage(address, userName, subject, message);
        smtpServer.sendmail(userName, address, formattedMessage);

        logger.logSuccess("Mail sent successfully");
        smtpServer.close();
        result = True;
    except BaseException as e:
        logger.logFailure("Failed to send mail, exception caught ::: " + str(e));
    return result;


# Private Functions

def getGmailSMTPServer(userName, password):
    smtpServer = smtplib.SMTP("smtp.gmail.com", 587);
    smtpServer.ehlo();
    smtpServer.starttls();
    smtpServer.ehlo;
    smtpServer.login(userName, password);
    return smtpServer;


def formatMessage(toAddres, fromAddress, subject, message):
    message = "To: %s\n" \
              "From: %s\n" \
              "Subject: %s\n" \
              "\n%s\n\n" % (toAddres, fromAddress, subject, message);
    return message;