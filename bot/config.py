from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID", "23171051"))
    API_HASH = getenv("API_HASH", "10331d5d712364f57ffdd23417f4513c")
    BOT_TOKEN = getenv("BOT_TOKEN", "7512610380:AAGWZ2CRw7i8c-XOkAZDXQcNL_mw37eI-Ws")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "BQGYpOMAnw9pcg7_YrDqatTXCOg57YbwIublqwDRIFKWvmwW_uSDZoLPNhfRU5niIQAtnJv_26vfp0k64dQ85ZlKYhap5EaqPRZJPELjuIHnmangBmNA3PC0AcoabOFMPg5qca9D4G0YIXLrWag0YyzFl1aL_4nvEQNJTIOBEg2fJM2I5VP_VKFPdkq9Mo6qJK_bSmzpjeVGryQqCmbVcXgtgPPhKVn3vv4l25wli-kEXXi9ZCY-Y6UjsyQqR3wfYxG44PRYdjxC6AXpnVdhP4i1jLqa01oLQcPgoXDsbJnAcMv09la5ktowi5hZDRYkGlgsB3OubML2haa_FqD7sh9nf_HdxwAAAAGpf-0jAA")
    BASE_URL = getenv("BASE_URL", "https://web-app-7wj0.onrender.com/").rstrip('https://web-app-7wj0.onrender.com/')
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://tabolo8539:0evqZDV4fC5fD17c@cluster0.cw8zxus.mongodb.net/?retryWrites=true&w=majority")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL", "-1002248276059").split(",")]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "admin")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "Vishalku")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "Vishalku")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
    HIDE_CHANNEL = bool(getenv('HIDE_CHANNEL', 'False'))
