import smtplib
from email.message import EmailMessage

from config import getConfig, checkSMTPConfig
from common import output, outputFileName


def send():
    data = getConfig('smtp_server')
    if data == None:
        text = "Could not sucessfully get smtp server configuration! - data=[{}]".format(data)
        print(text)
        return False

    if not checkSMTPConfig(data):
        print("Error while validating SMTP configuration!")
        return False

    server = data['server']
    port = data['port']
    SSL = data['SSL']
    sender = data['sender']
    recipient = data['recipient']
    subject = data['subject']
    username = data['username']
    password = data['password']

    # Create message. 
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg['Subject'] = subject
    msg.set_content(
        "Automatic message sent by checkmarx cloc tool. Please check the results attached.")
    msg.add_attachment(open(output, "r").read(), filename=outputFileName)

    if SSL.upper() == "YES" or SSL.upper() == "TRUE":
        srv = smtplib.SMTP_SSL(server, port)
    else:
        srv = smtplib.SMTP(server, port)

        # Optional login for the receiving mail_server.
    srv.login(username, password)

    try:
        srv.send_message(msg)
        print("Checkmarx CLOC E-Mail successfully sent.")
    finally:
        srv.quit()

    return True
