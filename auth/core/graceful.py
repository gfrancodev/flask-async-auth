from os import environ
from sys import exit 

def gracelful_shutdown(signum, callback):
    func = environ.get('werkzeug.server.shutdown')
    if func:
        func()
    exit(0)