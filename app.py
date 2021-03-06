
import os
from twilio.rest import Client
from flask import Flask, jsonify
app = Flask (__name__)

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

#---------------------------------------------------------------------

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
