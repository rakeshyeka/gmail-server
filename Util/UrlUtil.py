__author__ = 'rakesh'


def join(arg1, arg2):
    arg1 = arg1.rstrip("/");
    arg2 = arg2.lstrip("/");
    return arg1 + "/" + arg2;