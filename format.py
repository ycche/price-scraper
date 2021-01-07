import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_formatting import *

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

sheet = client.open('Test1')

ss = sheet.get_worksheet(0)

col_n = ss.find("Change").col


rule = ConditionalFormatRule(
    ranges= [GridRange(0,0,100,col_n-1,col_n)],
    booleanRule = BooleanRule(
        condition = BooleanCondition('NUMBER_GREATER',['1']),
        format = CellFormat(textFormat = textFormat(bold=True),backgroundColor = Color(0,3,0))
    )
)

rules = get_conditional_format_rules(ss)
rules.clear()
rules.append(rule)
rules.save()

rule = ConditionalFormatRule(
    ranges= [GridRange(0,0,100,col_n-1,col_n)],
    booleanRule = BooleanRule(
        condition = BooleanCondition('NUMBER_LESS',['1']),
        format = CellFormat(textFormat = textFormat(bold=True) , backgroundColor = Color(2,0,0))
    )
)

rules = get_conditional_format_rules(ss)
rules.append(rule)
rules.save()

# Bolding Col Names/Items

ss.format("A",{"textFormat":{"bold" : True}})
ss.format("1", {"textFormat":{"bold" : True}})

def remove_dash(ss):
    cell_list = ss.range('A1:A100')

    for cell in cell_list:
        cell.value = cell.value.replace("-", " ")

    ss.update_cells(cell_list)

remove_dash(ss)
