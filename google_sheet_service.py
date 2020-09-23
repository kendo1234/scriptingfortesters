import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

client = gspread.authorize(creds)

sheet = client.open('Script Testing').sheet1

# Update
# sheet.update_cell(1, 1, "Test")

# Read
# print(sheet.row_values(1))
# print(sheet.get_all_values())

my_data = [[1, 2, 3], [4, 5, 6]]

# enumerate will provide indexed list of values provided
for row_index,row in enumerate(my_data):
    for col_index,value in enumerate(row):
        sheet.update_cell(row_index+1, col_index+1, value)
