#! /usr/bin/python3
import smtplib, ssl, sys, dotenv, os
from email import message
from datetime import datetime

# collect clock in or clock out argument
args = sys.argv

if len(args) > 1 and args[1] == 'in':
    subject = "Signing In"
elif len(args) > 1 and args[1] == 'out':
    subject = "Signing Out"
else:
    print("Failed to supply clockin argument, should be either 'in' or 'out'")
    sys.exit(1)

dotenv.load_dotenv(dotenv.find_dotenv())

port = os.environ.get("port_number")
password = os.environ.get("email_password")
receiver_email = os.environ.get("receiver_email")
cc_email = os.environ.get("cc_email")
sender_email = os.environ.get("sender_email")
mail_server = os.environ.get("mail_server")

context = ssl.create_default_context()

email_message = message.Message()
email_message.add_header('from', sender_email)
email_message.add_header('to', receiver_email)
email_message.add_header('cc', cc_email)
email_message.add_header('subject', subject)
email_message.set_payload(f'{subject}\n')

to_addrs = [receiver_email, cc_email]


with smtplib.SMTP_SSL(mail_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, to_addrs, email_message.as_string())
