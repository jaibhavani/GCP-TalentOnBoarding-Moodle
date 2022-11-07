# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import smtplib
from email.message import EmailMessage
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def sendmail(email_from, email_to, subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.login('sdscloudlearning@gmail.com', 'Blaze04)$')