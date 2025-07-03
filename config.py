import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN","7556347155:AAHzChS20YVstWivH_o8v-O9kcc-dcxl0eo")
    API_ID = int(os.environ.get("API_ID","26468828"))
    API_HASH = os.environ.get("API_HASH","4693513c08d1ac6af15f95b116c29478")
    AUTH_USER = os.environ.get('AUTH_USERS', '7517045929').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "[🅱🅴🅰🆂🆃 👑](https://t.me/chiru52)"
