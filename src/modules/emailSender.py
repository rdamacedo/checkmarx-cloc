import smtplib
from email.message import EmailMessage

from src.modules.config import getConfig, checkEMailConfig
from src.modules.libUtils import clocOutput, clocOutputFileName


def send():
    data_dict = getConfig('email_config')
    if data_dict == None:
        msgtext = "Could not sucessfully get E-Mail Config! - data_dict=[{}]".format(data_dict)
        print(msgtext)
        return False

    if not checkEMailConfig(data_dict):
        print("Error while validating E-Mail Config!")
        return False

    smtpServer = data_dict['SMTPServer']
    smtpPort = data_dict['SMTPPort']
    useSSL = data_dict['useSSL']
    sender = data_dict['sender']
    receiver = data_dict['receiver']
    subject = data_dict['subject']
    senderName = data_dict['senderName']
    receiverName = data_dict['receiverName']
    username = data_dict['username']
    password = data_dict['password']

    # Create our message. 
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg['Subject'] = subject
    msg.set_content(
        "Automatic message sent by the PyCLOC automation tool. The attached file contains the statistic results generated by the tool.")
    msg.add_attachment(open(clocOutput, "r").read(), filename=clocOutputFileName)

    # --- send the email ---

    # SMTP() is used with normal, unencrypted (non-SSL) email.
    # To send email via an SSL connection, use SMTP_SSL().
    if useSSL == "YES":
        server = smtplib.SMTP_SSL(smtpServer, smtpPort)
    else:
        server = smtplib.SMTP(smtpServer, smtpPort)

        # Optional login for the receiving mail_server.
    server.login(sender, password)

    try:
        server.send_message(msg)
        print("E-Mail successfully sent.")
    finally:
        server.quit()

    return True