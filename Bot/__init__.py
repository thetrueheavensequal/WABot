import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get("API_ID", "24833791")) #API ID
API_HASH = environ.get("API_HASH", "42488cb247a33d13d5f97d6839c8e52b") #API HASH
BOT_TOKEN = environ.get("BOT_TOKEN", "5898463551:AAESGh0DA-P0-K70Cy_4emMxhXWTAiz3rtU") #BOT TOKEN
ORMONGO_RS_URL = environ.get("ORMONGO_RS_URL", "mongodb://lon5-c15-1.mongo.objectrocket.com:43160,lon5-c15-2.mongo.objectrocket.com:43160,lon5-c15-0.mongo.objectrocket.com:43160/?replicaSet=cb70448b1adb4aec9a5965dfea16eb34&ssl=true") #MONGO DB
OWNER_ID = int(environ.get("OWNER_ID", "2064735436")) #OWNER ID
MAIN_CHANNEL = int(environ.get("MAIN_CHANNEL", "-1001886875139"))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get("ARCHIVE_CHANNEL", "-1001249680167"))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get("MESSAGE_ID", "9")) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
