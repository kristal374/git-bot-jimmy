import discord
import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
import time

client = discord.Client()
a = 0
try:
    CREDENTIALS_FILE = 'Grim-Soul-PlachValki-reids-fac49cc847d2.json'
    spreadsheet_id = '1LMdiA-YvYyOjFus56XWc-sUN5moBRCds9g7M-cdEtA0'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
    a = "complit"
except:
    a = "error"
@client.event
async def on_ready():
    channel = client.get_channel(int(733230754817114166))
    await channel.send(f'Reconecting {a}!')

tok = "NzMzMjM3NDQ1MTcyMzk2MDQ0"
en = ".XxAOlQ.A6_McAUlhRfFvJuDE7IloQe98tc"
client.run(str(tok+en))
