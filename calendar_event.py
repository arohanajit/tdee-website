import google.auth
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime
import pytz
import json
from tdee_operation import tdee


def get_credentials():
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', ['https://www.googleapis.com/auth/calendar'])
    creds = None
    try:
        # Run the flow to obtain credentials
        creds = flow.run_local_server(port=0)
        # Save the credentials to a JSON file
        with open('token.json', 'w') as f:
            f.write(creds.to_json())
    except Exception as e:
        print(f"Failed to get credentials: {e}")
    return creds
    
def create_event(mycur):
    mycur.execute("SELECT userid, MAX(date) as latest_date FROM data GROUP BY userid")
    ids = mycur.fetchall()
    for i in ids:
        mycur.execute("SELECT credential from users WHERE userid=%s",i[0])
        result = mycur.fetchone()
        data = json.loads(result[0])
        with open('token.json','w') as f:
            f.truncate() # empty the file before writing to it
            json.dump(data, f) # write data to the file

        creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])
        # Set up the Google Calendar API client
        service = build('calendar', 'v3', credentials=creds)

        # expected_date_start = datetime.datetime.now(tzinfo=pytz.timezone('US/Eastern'))
        # expected_date_end = datetime.datetime.now(tzinfo=pytz.timezone('US/Eastern')) + datetime.timedelta(minutes=15,tzinfo=pytz.timezone('US/Eastern'))
        # Set up the reminder event
        tdee_vals= tdee(mycur,i[0])
        event = {
            'summary': 'Reminder: Your TDEE Goal for Today',
            'location': '',
            'description': f'Your TDEE Goal for today: {tdee_vals[0]}\nYour Average Weight: {tdee_vals[1]}\n Your Average Calories: {tdee_vals[2]}',
            'start': {
                'dateTime': (datetime.datetime.now(tz=pytz.timezone('US/Eastern')) + datetime.timedelta(hours=8,minutes=0)).isoformat(),
                'timeZone': 'US/Eastern',
            },
            'end': {
                'dateTime': (datetime.datetime.now(tz=pytz.timezone('US/Eastern')) + datetime.timedelta(hours=8,minutes=15)).isoformat(),
                'timeZone': 'US/Eastern',
            },
            'reminders': {
                'useDefault': True,
            },
            'colorId': '11', # Sets the event color to a light purple
        }

        # # Create the event in the calendar
        try:
            event = service.events().insert(calendarId='primary', body=event).execute()
            print('Event created: %s' % (event.get('htmlLink')))
        except HttpError as error:
            print('An error occurred: %s' % error)
