from app.core.logging import logger
from app.core.config import Config

from ldap3 import Server, Connection, NTLM, ALL

def ad_connection():
    server = Server(Config.SERVER_NAME, port=636, use_ssl=True, get_info=ALL)
    return Connection(
        server,
        user = Config.USER,
        password = Config.PASSWORD,
        authentication = NTLM,
        auto_bind = True
    )

