from asyncio import run
from signal import SIGINT, SIGTERM, signal
from dotenv import load_dotenv
from flask import Flask
from asgiref.wsgi import WsgiToAsgi
from core.handle import handle
from core.setup import setup
from core.graceful import gracelful_shutdown
from core.doc import documentation
from infra.events.http_auth import auth
from infra.events.http_user import user

load_dotenv()

server = Flask(__name__)
setup(server)

documentation(server)
server.register_blueprint(auth)
server.register_blueprint(user)

app = WsgiToAsgi(server)

if __name__ == "__main__":
    run(handle())
    
signal(SIGINT, gracelful_shutdown)
signal(SIGTERM, gracelful_shutdown)