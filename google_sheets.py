import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe
from tdee_operation import weight_cal_insert



def update_from_sheet(connection,mycur):
    # define the scope of access
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)

    # get the instance of the spreadsheet
    sheet = client.open('TDEE_Responses')

    # get the first sheet of the spreadsheet
    sheet_instance = sheet.get_worksheet(0)

    # get all the records of the data
    records_data = sheet_instance.get_all_records()

    # convert the json to dataframe
    records_df = pd.DataFrame.from_dict(records_data)

    rows = int(records_df.shape[0])

    # delete empty rows
    delete_empty_rows = records_df['Username']==""
    records_df = records_df.drop(records_df[delete_empty_rows].index)

    # delete duplicates
    records_df = records_df.drop_duplicates(subset="Username",keep='last')


    # delete invalid users
    db_users = mycur.execute("SELECT userid FROM users")
    db_users = mycur.fetchall()
    user = []
    for i in db_users:
        user.append(i[0])
    records_df = records_df[records_df['Username'].isin(user)]
    
    # insert data into db
    for index,vals in records_df.iterrows():
        weight_cal_insert(connection,mycur,vals['Username'],vals['Weight'],vals['Calorie'])

    # empty dataframe 
    for i in range(2,rows+3):
        sheet_instance.delete_rows(2)
