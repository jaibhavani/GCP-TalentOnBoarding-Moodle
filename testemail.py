from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
# Instantiate the client\

def sendemail():

    # Configure API key authorization: api-key
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'

    # Uncomment below lines to configure API key authorization using: partner-key
    # configuration = sib_api_v3_sdk.Configuration()
    # configuration.api_key['partner-key'] = 'YOUR_API_KEY'

    # create an instance of the API class
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    subject = "My Subject"
    html_content = "<html><body><h1>This is my first transactional email </h1></body></html>"
    sender = {"name": "John Doe", "email": "sdscloudlearning@gmail.com"}
    to = [{"email": "sdscloudlearning@gmail.com", "name": "Jane Doe"}]
    reply_to = {"email": "sdscloudlearning@gmail.com", "name": "John Doe"}
    headers = {"Some-Custom-Name": "unique-id-1234"}
    params = {"parameter": "My param value", "subject": "New Subject"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, reply_to=reply_to, headers=headers,
                                                   html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sendemail()