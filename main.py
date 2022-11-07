from __future__ import print_function
import requests
import json
import os
import sib_api_v3_sdk
import time
from flask import escape
from flask_cors import CORS, cross_origin
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

@cross_origin()
def receive_request(request):
    request_form = request.form

    if request_form and 'inputName' and 'inputLastname' and 'inputEmail' in request_form:
        firstname = request_form['inputName']
        lastname = request_form['inputLastname']
        email = request_form['inputEmail']

        result = moodle_user_create(email, firstname, lastname)

        if result == 'success':
            return 'Request received successfully.'
        else:
            print('RR:ERROR:USER_CREATION_FAILED')
            return 'Error, contact your system administrator!'
    else:
        print('RR:ERROR:PARAMETER_NOT_FOUND')
        return 'Error, contact your system administrator!'

def moodle_user_test():
    token = os.environ.get('MOODLE_TOKEN')
    server = os.environ.get('MOODLE_SERVER')
    sender_name = os.environ.get("SENDER_NAME")
    sender_email = os.environ.get("FROM_EMAIL_ADDRESS")
    smtp_key = os.environ.get("SMTP_KEY")

    print (" token %s", token)
    print(" server "  + server)
    print(" sender_name %s", sender_name)
    print(" sender_email %s", sender_email)
    print(" smtp " + smtp_key)

def moodle_user_create(email, firstname, lastname):
    token = os.environ.get('MOODLE_TOKEN')
    server = os.environ.get('MOODLE_SERVER')
    sender_name = os.environ.get("SENDER_NAME")
    sender_email = os.environ.get("FROM_EMAIL_ADDRESS")


    function = 'core_user_create_users'
    url = 'http://{0}/webservice/rest/server.php?wstoken={1}&wsfunction={2}&moodlewsrestformat=json'.format(server,
                                                                                                            token,
                                                                                                            function)

    email = email
    username = email.split("@")[0]

    users = {'users[0][username]': username,
             'users[0][email]': email,
             'users[0][lastname]': lastname,
             'users[0][firstname]': firstname,
             'users[0][password]': 'P@40ssword123'}

    try:
        response = requests.post(url, data=users)
        if 'exception' in json.loads(response.text):
            print('Result: ' + response.text)
            return 'error'
        else:
            print('Result: ' + response.text)
            print(" Now sending email ")
            smtp_step = sendemail(sender_name, sender_email, firstname + " " + lastname, email)

            if 'exception' in smtp_step:
                return ' error while sending email'
            else:
                return 'success'

    except Exception as e:
        print(e)
        return 'error'


def sendemail(sender_name, sender_email, to_name, to_email):
    # Configure API key authorization: api-key
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = os.environ.get("SMTP_KEY")
    print (" sender name %s ", sender_name)
    print(" sender email %s ", sender_email)
    print(" to name %s ", to_name)
    print(" to email %s ", to_email)

    # Uncomment below lines to configure API key authorization using: partner-key
    # configuration = sib_api_v3_sdk.Configuration()
    # configuration.api_key['partner-key'] = 'YOUR_API_KEY'

    # create an instance of the API class
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    subject = "Welcome"
    html_content = "<html><body><h1>Welcome Aboard</h1>"
    html_content = html_content + " Please complete <a href='http://34.138.157.211/course/view.php?id=2#section-0'>Onboarding training </a> courses </body></html>"
    sender = {"name": sender_name, "email": sender_email}
    to = [{"email": to_email, "name": to_name}]
    reply_to = {"email": sender_email, "name": sender_name}
    headers = {"Some-Custom-Name": "unique-id-1234"}
    params = {"parameter": "My param value", "subject": "New Subject"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, reply_to=reply_to, headers=headers,
                                                   html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
        return 'success'
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
        return "Exception when calling SMTPApi->send_transac_email: %s\n" % e


if __name__ == '__main__':
    moodle_user_create('suhassankolli@gmail.com', 'shilpa', 'sankolli')
    #moodle_user_test()
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
