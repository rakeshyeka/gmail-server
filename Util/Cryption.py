__author__ = 'rakesh'
from Crypto.Cipher import AES;
import base64;
import os;

BLOCK_SIZE = 16;
PADDING_CONSTANT = '{';


def encryption(text):
    secret = os.urandom(BLOCK_SIZE);
    cipher = AES.new(secret);
    encodedText = base64.b64encode(cipher.encrypt(padText(text)));
    return encodedText;


def decryption(secret, encryptedText):
    cipher = AES.new(secret);
    decodedText = removePadding(cipher.decrypt(base64.b64decode(encryptedText)));
    return decodedText;


# Private functions

def addPadding(text):
    paddedText = text + (BLOCK_SIZE - len(text) % BLOCK_SIZE) * PADDING_CONSTANT;
    return paddedText;


def removePadding(text):
    return text.rstrip(PADDING_CONSTANT);