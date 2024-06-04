from flask_cors import CORS
from flask_compress import Compress
from flask_talisman import Talisman 
from flask_limiter import Limiter, util 

def setup(server):
    CORS(server, origins=['*'])
    Compress(server)
    Talisman(server, content_security_policy=None, force_https=False)
    Limiter(
        util.get_remote_address,
        app=server, 
        default_limits=["60 per hour"],
        storage_uri="memory://"
    ) 