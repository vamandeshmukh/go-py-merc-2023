import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print('start')
sender_email = 'vamandeshmukh@yahoo.com'
recipient_email = 'vamandeshmukh@gmail.com'
subject = 'Asdf'
body = ';lkj'
smtp_server = 'smtp.mail.yahoo.com'
smtp_port = 587
username = 'vamandeshmukh@yahoo.com'
password = ''
with open('C://Users//DELL//Documents//pass-word.txt', 'r') as file:
    password = file.read()

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)
server.sendmail(sender_email, recipient_email, message.as_string())
server.quit()

print('end')


