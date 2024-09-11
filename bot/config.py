from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID", "26780899"))
    API_HASH = getenv("API_HASH", "88c1b5a2a369695990bfce2ecd4fe601")
    BOT_TOKEN = getenv("BOT_TOKEN", "6737943130:AAENzY3vZdDVo6jsfvvip019IRzbp38h01U")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "BQGYpOMAR8CnerlWSNx_h66UEswxIZDoY_-SZ6BpOOgfAMshAypvLsIPFtLhCqNNyxane7ErDJ6xsAm6ELzwZ2pJ41v4QBesjVBJxkAGTIvLdqMg8f6IfZEUZi_1gftJWBjBCCy4ep-71hYX_BUIcV6YL0ZQ6arz4LjhdFsY6GNgpEAPmT1C1fgxIeUSGFdfCJV-ZdwOFvNN1JvLz_wgv3mTjjhzhziwm5RsyWUJlLYcj35_kSLIdOfJWb9Y8UeJGSAGkMU499Zk9LcL89XtvLvvsd5voesSFYrczvaJmtOLkmbBWouWaYbGmzPIJxpl2QVrzKtCbWJbOSyrg6452PpIgcIUowAAAAGpf-0jAA")
    BASE_URL = getenv("BASE_URL", "https://interim-sheelagh-rrrrr-88421628.koyeb.app/").rstrip('/')
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://tabolo8539:0evqZDV4fC5fD17c@cluster0.cw8zxus.mongodb.net/?retryWrites=true&w=majority")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL", "-1002248276059").split(",")]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "admin")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "surfTG")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "surfTG")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
    HIDE_CHANNEL = bool(getenv('HIDE_CHANNEL', 'False'))
