# Fuck yea 👍
import logging
from logging.handlers import RotatingFileHandler
import os
import time
from pyrogram import Client


# TODO: is there a better way?




from bot.config import Config




AUTH_USERS = [1820242622,-1001711333852,1690217497,1737176378,1979928067]

SESSION_NAME = "Workflow2"
TG_BOT_TOKEN = "1900584203:AAFlXwmYZC5XuB64bRQqMwyWT3WjhvSlQbY"
APP_ID = 2970864
API_HASH = "4e04aef1a856dc32cb7e98bce4440509"

LOG_CHANNEL = "hdhdhidjs"  # make sure to us this 
DOWNLOAD_LOCATION = "/app/downloads"
FREE_USER_MAX_FILE_SIZE = 2097152000
MAX_MESSAGE_LENGTH = 4096
FINISHED_PROGRESS_STR = "▓"
UN_FINISHED_PROGRESS_STR = "░"
BOT_START_TIME = time.time()
LOG_FILE_ZZGEVC = "Log.txt"
BOT_USERNAME = "mayank25Bot"
CHAT_ID = -1001749028548
UPDATES_CHANNEL = "anime_channelz"
data = []
crf = []
watermark = []
resolution = []
codec = []
preset = []
audio_b = []

pid_list = []
app = Client(
        SESSION_NAME,
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        workers=2
    )
if os.path.exists(LOG_FILE_ZZGEVC):
    with open(LOG_FILE_ZZGEVC, "r+") as f_d:
        f_d.truncate(0)

# the logging things
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=FREE_USER_MAX_FILE_SIZE,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)
