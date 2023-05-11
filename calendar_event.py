import google.auth
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime
import pytz
import json


def get_credentials(uname):
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', ['https://www.googleapis.com/auth/calendar'])
    creds = Credentials.from_authorized_user_info(info=flow.run_local_server(port=0))
    with open('token.json', 'w') as f:
        f.write(creds.to_json())
    
def create_event(mycur,uname):

    mycur.execute("SELECT credential from users WHERE userid=%s",uname)
    result = mycur.fetchone()
    data = json.loads(result[0])
    with open('token.json','w') as f:
        json.dump(data,f)

    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])
    # Set up the Google Calendar API client
    service = build('calendar', 'v3', credentials=creds)

    # Set up the reminder event
    event = {
        'summary': 'Reminder: Your Appointment',
        'location': '123 Main St, Anytown USA',
        'description': 'This is a reminder for your appointment with Dr. Smith.',
        'start': {
            'dateTime': datetime.datetime(2023, 5, 12, 10, 0, tzinfo=pytz.timezone('US/Eastern')).isoformat(),
            'timeZone': 'US/Eastern',
        },
        'end': {
            'dateTime': datetime.datetime(2023, 5, 12, 11, 0, tzinfo=pytz.timezone('US/Eastern')).isoformat(),
            'timeZone': 'US/Eastern',
        },
        'reminders': {
            'useDefault': True,
        },
        'colorId': '11', # Sets the event color to a light purple
    }

    # Create the event in the calendar
    try:
        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))
    except HttpError as error:
        print('An error occurred: %s' % error)
