import google.auth
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
import datetime
import pytz
import json
import os
from tdee_operation import tdee

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return creds

def create_event(connection, mycur):
    mycur.execute("SELECT userid, MAX(date) as latest_date FROM data GROUP BY userid")
    ids = mycur.fetchall()
    for i in ids:
        mycur.execute("SELECT credential FROM users WHERE userid=%s", (i[0],))
        result = mycur.fetchone()
        if result:
            data = json.loads(result[0])
            
            # Update token.json with the stored credentials
            with open('token.json', 'w') as f:
                json.dump(data, f)
            
            creds = get_credentials()  # This will refresh the token if necessary
            
            # Update the stored credentials in the database if they've changed
            new_creds_json = creds.to_json()
            if new_creds_json != result[0]:
                mycur.execute("UPDATE users SET credential = %s WHERE userid = %s", (new_creds_json, i[0]))
                mycur.connection.commit()
            
            # Set up the Google Calendar API client
            service = build('calendar', 'v3', credentials=creds)

            tdee_vals = tdee(connection, mycur, i[0])
            event = {
                'summary': 'Reminder: Your TDEE Goal for Today',
                'location': '',
                'description': f'Your TDEE Goal for today: {tdee_vals[0]}\nYour Average Weight: {tdee_vals[1]}\nYour Average Calories: {tdee_vals[2]}',
                'start': {
                    'dateTime': (datetime.datetime.now(tz=pytz.timezone('US/Eastern')) + datetime.timedelta(hours=8, minutes=0)).isoformat(),
                    'timeZone': 'US/Eastern',
                },
                'end': {
                    'dateTime': (datetime.datetime.now(tz=pytz.timezone('US/Eastern')) + datetime.timedelta(hours=8, minutes=15)).isoformat(),
                    'timeZone': 'US/Eastern',
                },
                'reminders': {
                    'useDefault': True,
                },
                'colorId': '11',  # Sets the event color to a light purple
            }

            # Create the event in the calendar
            try:
                event = service.events().insert(calendarId='primary', body=event).execute()
                print(f'Event created for user {i[0]}: {event.get("htmlLink")}')
            except HttpError as error:
                print(f'An error occurred for user {i[0]}: {error}')
        else:
            print(f"No credentials found for user {i[0]}")