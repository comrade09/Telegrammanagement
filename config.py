import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "13678305")
    API_HASH = getenv("API_HASH", "a5d9be6f810f31e5c56bad6eebbd7ba8")
    TOKEN = getenv("TOKEN", "5522488286:AAGt7lPKy31PL6WMLjspceESsNC99OD5ZQU")
    OWNER_ID = getenv("OWNER_ID","1442684727")
    STRING_SESSION = getenv("STRING_SESSION","BQC_6nmciUHubuyBYuHCplMfpZhWMsP40MiYlY1o-ULtvSZurnAk-DVmxhdE96EAJ9lplxWEtoIZ-OfAaN-x3oq_nj-wTsx_U_EbgwKqAhNXFal4CucPxIUSKDDTykiwK_1Ti2VLEfKt1fS4jJbvTvbMojXBUtDbW3UeHl8hZwdpzY0K2Yrdzgd9ajv3nFPq70shsrKdWZYBn2Xo_8CaCuYihNYmzFLlqLK0DXOlxZyAQPllWEuKGoG2qNclXJSQBRkVk2eBYZSXFjweVNrB_RsL7kkEYkS3-Hvos1sc2pzSi9fyhr4QM3Z9rE9_jBAEtoaeN06kxZL9eseGF7tflcNQPcjI6QA")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "Ath2023")
    DB_URI = getenv("DATABASE_URL" , "postgres://mozcfhlw:F9P_IepbofsGVuKMxWIRvyacXmdAICwe@lallah.db.elephantsql.com/mozcfhlw")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001509525202")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001509525202")
    SYS_ADMIN = getenv("SYS_ADMIN", "1669178360")
    DEV_USERS = getenv("DEV_USERS", "1669178360")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "1669178360").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))