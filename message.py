from twilio.rest import TwilioRestClient

def sendSMS(messageToSend):
    account_sid = "ACa326d844b6f8edd861dc1488531d9efe"
    auth_token = "dbd22909483217c1f1c23a2aa6a7e4a5"

    # We instantiate a REST Client and pass it our accout ID and token as arguments
    client = TwilioRestClient(account_sid, auth_token)

    """ We use the 'TwilioRestClient' object, access it's messages object, and then
     then it's 'create method' """
    client.messages.create(to="+13477920858",
                           from_="+19145945181",
                           body=messageToSend)
    print messageToSend + " was sent thorugh twilio"

sendSMS("Are you a robot?")
# sendSMS("You Punk!")
