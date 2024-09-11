from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID", "26780899"))
    API_HASH = getenv("API_HASH", "88c1b5a2a369695990bfce2ecd4fe601")
    BOT_TOKEN = getenv("BOT_TOKEN", "7512610380:AAGWZ2CRw7i8c-XOkAZDXQcNL_mw37eI-Ws")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "BQGYpOMALrcLUfmTbYyEAc6t1-9SecXWMiiXcbWiQjUpOaFG6e7oYf7x0V4SExlTL-peEdrgZBzaqxWo6F36nNZY76JWy5-ll1U9NArODVT_SREX2jNMAf61IppmnCJ7HPPeDAFLMZzo1ergQ4lIzluZ1Ti208xMBJ7ycALAfv47dGI6AaTh1FrYbkrSUTqJ4LUy9b8IVnH529in5yxYgyCKNPLYd4MDTF7zq0qw3XYZ7K6jXPFsY9ArpiyCabnfAtmTE_KVyzwlEmGgXQpDBunXHBSYacxQVWB5FKT1BB3ZIvA-i1tXB_xB39CQvnJ6kuv_p0oEutKwyYDDifXEORsHUvut2QAAAAGpf-0jAA")
    BASE_URL = getenv("BASE_URL", "https://interim-sheelagh-rrrrr-88421628.koyeb.app/").rstrip('https://interim-sheelagh-rrrrr-88421628.koyeb.app/')
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
