import os
from os import getenv
from dotenv import load_dotenv
import os.path

from typing import List, Optional

load_dotenv()
que = {}
admins = {}


API_ID = int(getenv("API_ID", "14688437"))
API_HASH = getenv("API_HASH", "5310285db722d1dceb128b88772d53a6")
BOT_TOKEN = getenv("BOT_TOKEN","6399781777:AAEXmjdpieZ3qiJLkxqng6b09tNj_q87KkQ")
