from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID", "20478395"))
    API_HASH = getenv("API_HASH", "276134bae90f79bbf534206036163a41")
    BOT_TOKEN = getenv("BOT_TOKEN", "7106861798:AAE6NatuBhHB48BI1B1ZF_79L50trtPARc0")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "BQE4ebsAB5mvxmWN9ZD0dqBnKEvMH4le-4Mw-8iZdqd6eFnV8r7TjztkpYcS3XbpYBRIsoJv4a0_E1ZYtesfpniDf_ax-oOdCjGRys8hvInhZ2TexUW8R-fjHp5IiL1NhDNowsBfATftuPVgSfGQTEhLAuK9IFLtdvBMi6P9NDnlY8ADYfTE32LGo-rX3MB8ei-F4ewyf3j2P3hcpREtkujsqyWIymF5y_13TMQCkFdIStBzAkLYO6GG5EqBBK3QuvHu8PLm_y4OsTU_tU04yjejGXxzC_aSfqImlBrkoj0in-W4RxdJp1dv1Au9zqLheTyVYjRQRHuenDLFYrM2ENvh1ifoigAAAAHc0RHzAA")
    BASE_URL = getenv("BASE_URL", "https://web-app-dff20.onrender.com/").rstrip('https://web-app-dff20.onrender.com/')
    DATABASE_URL = getenv("DATABASE_URL", " mongodb+srv://dff_db_user:EMHtoA6Dyrf53Vnj@cluster0.ydf8yoj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") 
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL", "-1001903104162").split(",")]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "admin")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "sample")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "sample")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
    HIDE_CHANNEL = bool(getenv('HIDE_CHANNEL', 'False'))
