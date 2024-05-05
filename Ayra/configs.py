# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default=6, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", default=None)
    MONGO_URI = sys.argv[4] if len(sys.argv) > 4 else config("MONGO_URI", default=None)

    BOT_TOKEN = config("BOT_TOKEN", default=None)
    DB_NAME = config("DB_NAME", default="NayaDB")
    LOG_CHANNEL = config("LOG_CHANNEL", default=123, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    SUDO = config("SUDO", default=True, cast=bool)
    VC_SESSION = config("VC_SESSION", default=SESSION)
    ADDONS = config("ADDONS", default=False, cast=bool)
    INLINE_PIC = config("INLINE_PIC", default=False, cast=bool)
    VCBOT = config("VCBOT", default=True, cast=bool)
    DISABLE_PMDEL = config("DISABLE_PMDEL", default=True, cast=bool)
