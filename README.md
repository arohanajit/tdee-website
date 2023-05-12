# tdee-website
This is a personal project which aims to make tracking calories/weights more convenient using google calendar and multiple input methods via web/google forms.

## Table of Contents
- [tdee-website](#tdee-website)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [Language and Libraries](#language-and-libraries)
    - [API and Credentials](#api-and-credentials)
  - [Contribution](#contribution)
  - [License](#license)
  - [Future Scope and Personal Notes](#future-scope-and-personal-notes)

## Features
- The project takes input via web/google forms thus enabling users to input data via pc/smartphone as per their convenience. Use this [form](https://docs.google.com/forms/d/e/1FAIpQLScvfee38jOdAMEsOvmX2SUSCPIjlm8tPCwJGcbW86RVlvvv8A/viewform)
- It calculates tdee and sets reminder via google calendar event, thus eliminating the need of browsing to a certain app to see your daily calorie needs. This particularly can come in handy if someone uses a smart home device which can give them their daily tdee goal as they wake up
- The generic formula for calculating tdee is used which updated itself as more data is input. It is highly recommeded to input atleast **2 weeks** of data to get consistent results.

## Installation

### Language and Libraries
You'll need Python 3.7 or above to run the code. As of now it's a terminal based program, however developing it into a web app using flask is something I'm planning to do in the future. I developed this program in a conda environment and it's something I recommend as there are some project specific libraries not employed often in general use case.
List of libraries:
- google.auth, google.oauth2, google_auth_oauthlib, googleapiclient
- pymysql
- bcrypt
- getpass
- gspread, gspread_dataframe
- oauth2client
- traceback
  
### API and Credentials

- You'll need to create a project in the Google Cloud Console and enable the Google Calendar API for that project. You can follow the steps outlined in this [guide](https://developers.google.com/calendar/quickstart/python) to do this.

- Once you have enabled the API, you'll need to create OAuth 2.0 credentials for your project. You can follow the steps outlined in this [guide](https://developers.google.com/calendar/auth) to create the credentials.

- You will also need credential file for google sheets. Follow this [link](https://developers.google.com/sheets/api/guides/authorizing) to create one.

## Contribution

I, Arohan Ajit am the sole contributor. You can contact me on arohanajit232@gmail.com for anything related. Alternatively you can post some on github which I check rather sporadically.

## License

The project is covered under MIT Open Source

## Future Scope and Personal Notes
There are a couple of things I plan to do

- Better comments
- The project uses a free online database, so you probably won't be able to use it for extensive tests. This also introduces a possibility to that it might be down at sometime in future (whenever you're seeing this). Please create your own instance of db and replace the credentials.
- Clean up the code. In case it is not immediately evident, I am an amateur programmer and having lot of extra code commented out which were used for test/previous versions. I am planning to clean up the code.
- Develop into a flask web app. As of now the web input is terminal based.
- Something else that comes in mind in future, time permiting.