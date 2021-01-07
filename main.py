import gspread
import pandas as pd
import datetime
from oauth2client.service_account import ServiceAccountCredentials

from collect import parse
from process import *
from gspread_formatting import *
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

sheet = client.open('Test1')

sheet_instance = sheet.get_worksheet(0)

items = ["twisted-bow","sanguinesti-staff-uncharged","dragon-hunter-lance","super-restore-4","blood-rune","ancestral-robe-top"]






#item_prices = parse(items)
#update(sheet_instance, item_prices)
#combine(sheet_instance)
