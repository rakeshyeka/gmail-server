__author__ = 'rakesh'
import imaplib;
import Logger;
import email;

IMAP_LOG_FILE = "ImapLog.txt";
DEFAULT_INBOX = "RaspPi";
GMAIL_TRASH_FOLDER = "[Gmail]/Trash";


def fetchLatestEmail(credentials):
    logger = Logger.logger(IMAP_LOG_FILE);
    emailText = "";
    try:
        userName = credentials.userName;
        password = credentials.password;
        imapServer = getGmailIMAPServer(userName, password);
        imapServer.select(DEFAULT_INBOX);
        result, data = imapServer.uid('search', None, "ALL")
        latestUID = data[0].split()[-1];
        emailText = getEmail(imapServer, latestUID);

        logger.logSuccess("Mail fetched successfully");
        imapServer.logout();
    except BaseException as e:
        logger.logFailure("Failed to fetch mail, exception caught ::: " + str(e));
    return emailText;


def getFolderList(credentials):
    logger = Logger.logger(IMAP_LOG_FILE);
    list = [];
    try:
        userName = credentials.userName;
        password = credentials.password;
        imapServer = getGmailIMAPServer(userName, password);
        result, list = imapServer.list();

        logger.logSuccess("List of folders successfully");
        imapServer.logout();
    except BaseException as e:
        logger.logFailure("Failed to fetch list of folders, exception caught ::: " + str(e));
    return list;


def deleteAllExceptLatestEmail(credentials):
    logger = Logger.logger(IMAP_LOG_FILE);
    try:
        userName = credentials.userName;
        password = credentials.password;
        imapServer = getGmailIMAPServer(userName, password);
        imapServer.select(DEFAULT_INBOX);
        result, data = imapServer.uid('search', None, "ALL");
        UIDList = data[0].split();
        for UID in UIDList[:-1]:
            deleteEmail(imapServer, UID);

        logger.logSuccess("Mails deleted successfully")
        imapServer.logout();
    except BaseException as e:
        logger.logFailure("Failed to delete mails, exception caught ::: " + str(e));


# Private Functions

def getGmailIMAPServer(userName, password):
    imapServer = imaplib.IMAP4_SSL("imap.gmail.com", "993");
    imapServer.login(userName, password);
    return imapServer;


def getEmail(imapServer, UID):
    result, data = imapServer.uid('fetch', UID, '(RFC822)')
    emailMessage = email.message_from_bytes(data[0][1]);
    maintype = emailMessage.get_content_maintype()
    if maintype == 'multipart':
        for part in emailMessage.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return emailMessage.get_payload()


def deleteEmail(imapServer, UID):
    result = imapServer.uid('COPY', UID, GMAIL_TRASH_FOLDER);
    if(result == "ok"):
        result, data = imapServer.uid('STORE', UID, '+FLAGS', '(\Deleted)');
        imapServer.expunge();