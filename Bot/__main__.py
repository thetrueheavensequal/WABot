import os, sys
import asyncio 
import requests 
from Bot import LOG, soheru
from Bot.database.client import startup


x = requests.get('http://soheru.in', allow_redirects=True).status_code
if x != 200:
    sys.exit()  

for x in os.listdir("."):
    if "mp4" in x:
        os.remove(x)
    elif 'png' in x:
        os.remove(x)        
LOG.info('Cleaned Terminal')
    
soheru.start()
print('''
AUTOPAHE BY SOHERU''')
print('''
BOT STARTED''')

startup()
print('''
CHECKED ALL SETTINGS''')

loop = asyncio.get_event_loop()
loop.run_forever()
