'''
import os
from subprocess import call
from twilio.rest import Client
from flask import Flask, jsonify
app = Flask (__name__)

from twilio.twiml.voice_response import Client, Dial, VoiceResponse
from twilio.twiml.voice_response import Client, Dial, Identity, Parameter, VoiceResponse
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant

# required for all twilio access tokens
account_sid = os.environ['ACa04a1cf087c83f08afc6577b475144f6']
api_key = os.environ['TWILIO_API_KEY']
api_secret = os.environ['Uddd3lCSxyPERyh2DbpspZXvgdl9bOtx']

# required for Voice grant
outgoing_application_sid = 'AP1b8379ac105401d26803be32ec4466dd'
identity = 'user_enisco'

# Create access token with credentials
token = AccessToken(account_sid, api_key, api_secret, identity=identity)

# Create a Voice grant and add to token
voice_grant = VoiceGrant(
    outgoing_application_sid=outgoing_application_sid,
    incoming_allow=True, # Optional: add to allow incoming calls
)
token.add_grant(voice_grant)

# Return token info as JSON
print(token.to_jwt())


@app.route("/")
def home():
    return "Welcome to my Flask App for Twilio Voice and Messaging SDKs."

@app.route('/call')
def twilioMakeCall():
    account_sid = "ACa04a1cf087c83f08afc6577b475144f6"
    auth_token  = "40b8213df917bb608bd7c86da5362162"
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml='<Response><Say>Hello, Engineer Paul. This is Sodiq. I am calling from my app using the Twilio call API. Thank you.!</Say></Response>',
        to='+2349032242379',
        from_='+18573715906'
        )

    print(call.sid)
    return call.sid


@app.route('/sms')
def twilioSendSMS():
    account_sid = "ACa04a1cf087c83f08afc6577b475144f6"
    auth_token  = "40b8213df917bb608bd7c86da5362162"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+2348051039931", 
        from_="+18573715906",
        body="Hello Cospis. I am sending you this message from my Flutter Mobie App using Python Twilio hosted on a Flask API!"
        )

    print(message.sid)
    return message.sid

#--------------------------------------------------------------------- env cmd 11111111

@app.route('/callp/<myquery>')
def twilioCallWithDetails(myquery):
    print(myquery) 
    data = myquery.split ("~", 1)
    print(myquery)

    account_sid = "ACa04a1cf087c83f08afc6577b475144f6"
    auth_token  = "40b8213df917bb608bd7c86da5362162"
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml='<Response><Say>' + data[1] + '</Say></Response>',
        to=data[0], 
        from_='+18573715906'
        )

    print(call.sid)
    return call.sid


@app.route('/smsp/<myquery>')
def twilioSendSMSWithDetails(myquery):
    print(myquery) 
    data = myquery.split ("~", 1)
    print(myquery) 

    account_sid = "ACa04a1cf087c83f08afc6577b475144f6"
    auth_token  = "40b8213df917bb608bd7c86da5362162"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=data[0], 
        from_="+18573715906",
        body=data[1]
        )

    print(message.sid)
    return message.sid

#---------------------------------------------------------------------

if __name__ == '__main__':
    app.run()

'''


import sys
import os
import time
from random import randint
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agora_token_builder import RtcTokenBuilder
from flask import Flask, jsonify
app = Flask(__name__)

Role_Attendee = 0 # depreated, same as publisher
Role_Publisher = 1 # for live broadcaster
Role_Subscriber = 2 # default, for live audience

appId = "ae5fd2a5833c4da5937bbd3a5d01b646"
appCertificate = "b6e2d56a64f7436d829db594fc0d51ce"
expireTimeInSeconds = 86400
currentTimestamp = int(time.time())
privilegeExpiredTs = currentTimestamp + expireTimeInSeconds


@app.route("/")
def home():
    return "Welcome to my Flask App for Agora Token Client."

#---------------------------------------------------------------------

@app.route('/get-token/<myquery>')
def getNewAgoraToken(myquery):
    print(myquery)
    data = myquery.split ("~", 1)
    print(data[0])
    print(data[1])
    channelName = data[0]
    uid = data[1]
    
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, 1, privilegeExpiredTs)
    print(token)
    return token

#---------------------------------------------------------------------

if __name__ == '__main__':
    app.run()