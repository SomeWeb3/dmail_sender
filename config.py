from os import environ

from dotenv import load_dotenv

load_dotenv()

WALLETS_FILE = environ["WALLETS_FILE"]
SLEEP = eval(environ["SLEEP_BETWEEN_WALLETS"])
RPC = environ["RPC"]
RANDOM_WALLETS_ORDER = environ["RANDOM_WALLETS_ORDER"] == "True"

ZK_MAIL_ADDRESS = "0x981F198286E40F9979274E0876636E9144B8FB8E"
