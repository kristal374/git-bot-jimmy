import discord

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
import time
import random, asyncio
import threading
client = discord.Client()
order = ["Орден"]
l_author, l_nick, l_mention, l_author_m, lst_reid, reid, last_reid, last_index_reid, wins, sum_reid, indexl, teen, sostaw, zapas = [], [], [], [], [], [], [], [], [], [], [], [], [], []
composit = ['', '', '', '', '', '', '', '', '', '']
ltime = ["сегодня"]
messag, zapisano, dezap, ykaz, autir = 0, 0, 0, 0, 0

CREDENTIALS_FILE = 'Grim-Soul-PlachValki-reids-fac49cc847d2.json'
spreadsheet_id = '1LMdiA-YvYyOjFus56XWc-sUN5moBRCds9g7M-cdEtA0'

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
try:
    values = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range='O2', majorDimension='COLUMNS').execute()
    valy = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=f'A2:B{int(((values["values"])[0])[0])}', majorDimension='COLUMNS').execute()
    val = valy["values"]
    lst_reid, reid = val[0], val[1]
except:
    pass
try:
    valy = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range='C2:D11', majorDimension='COLUMNS').execute()
    val = valy["values"]
    teen, sostaw = val[0], val[1]
except:
    try:
        val.append([])
        teen, sostaw = val[0], val[1]
    except:
        pass
try:
    values = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range='N2', majorDimension='COLUMNS').execute()
    valy = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=f'E2:L{int(((values["values"])[0])[0])}', majorDimension='COLUMNS').execute()
    val = valy["values"]
    l_nick, l_mention, l_author_m, last_reid, last_index_reid, wins, sum_reid, l_author = val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7]
except:
    pass
try:
    values = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range='P2', majorDimension='COLUMNS').execute()
    valy = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=f'M{int(((values["values"])[0])[0])}', majorDimension='COLUMNS').execute()
    val = valy["values"]
    zapas = val[0]
except:
    pass
try:
    valy = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range='Q2', majorDimension='COLUMNS').execute()
    val = valy["values"]
    order = val[0]
except:
    pass


@client.event
async def on_ready():
    channel = client.get_channel(int(733230754817114166))
    await channel.send(l_author, l_nick, l_mention, l_author_m, lst_reid, reid, last_reid, last_index_reid, wins, sum_reid, indexl, teen, sostaw, zapas)
    await channel.send('Reconecting Complite!')

tok = "NzMzMjM3NDQ1MTcyMzk2MDQ0"
en = ".XxAOlQ.A6_McAUlhRfFvJuDE7IloQe98tc"
client.run(str(tok+en))
