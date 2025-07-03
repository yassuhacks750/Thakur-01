import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN","7556347155:AAHzChS20YVstWivH_o8v-O9kcc-dcxl0eo")
    API_ID = int(os.environ.get("API_ID","22849789"))
    API_HASH = os.environ.get("API_HASH","0fc127c6055acd59f00ec6c229e1e3c4")
    AUTH_USER = os.environ.get('AUTH_USERS', '7296271316').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "[🅱🅴🅰🆂🆃 👑](https://t.me/chiru52)"
