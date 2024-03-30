import os

API_ID = API_ID = 25322308

API_HASH = os.environ.get("API_HASH", "4f720e70ce155df40213026c31ccd819")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6995167349:AAFSOgb2BiraX4YqlmGXV1fx1NIAygJdPvQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7184539514))

LOG = -1001907859284,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7184539514").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


