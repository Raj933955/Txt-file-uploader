import os

API_ID = API_ID = 27952989

API_HASH = os.environ.get("API_HASH", "74f04808a359e9a516e955ec243613ca")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7078244742:AAEyFtn60LTrHVOe8Wv4_9ItZsNh-hblgSI")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5128979564))

LOG = -1002047255106,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5128979564").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


