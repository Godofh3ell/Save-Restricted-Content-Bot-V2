# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "1741221"))
API_HASH = getenv("API_HASH", "a9d0852e8a6545c2f47593fb560b937a")
BOT_TOKEN = getenv("BOT_TOKEN", "2068629541:AAF1s0ksWiVKLTqCKMaq-lzlVbTQ-khB-38")
OWNER_ID = list(map(int, getenv("OWNER_ID", "810796147").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://tsnm:tsnm@cluster0.ck68u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1001499573135")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001344957091"))
