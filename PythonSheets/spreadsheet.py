import gspread
import pprint
from enum import IntEnum
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
json_file = 'PythonSheets/client_secret.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
client = gspread.authorize(creds)
pp = pprint.PrettyPrinter()

sheet = client.open('PythonSheets').sheet1

data = sheet.get_all_records()
pp.pprint(type(data))
# pp.pprint(dir(sheet.find('kolumna 2')))
pp.pprint(data[0])


