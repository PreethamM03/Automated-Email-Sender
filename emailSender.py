import smtplib, ssl
import getpass

port = 465

server = 'smtp.gmail.com'
sender = input("what is your email? ")
receiver = input("What email would you like to send to? ")
subject = input("What is the subject of your email? ")
text = input("What is the message of your email? ")
password = getpass.getpass('What is your email password: ', stream=None)

message = """\
Subject:{sub}

{tex}

""".format(sub=subject, tex=text)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
