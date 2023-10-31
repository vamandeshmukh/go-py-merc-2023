import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print('start')
sender_email = 'vamandeshmukh@yahoo.com'
recipient_email = 'vamandeshmukh@gmail.com'
subject = 'Subject of the email'
body = 'This is the email body'
smtp_server = 'smtp.mail.yahoo.com'
smtp_port = 587
username = 'vamandeshmukh@yahoo.com'
password = ''
with open('C://Users//DELL//Documents//pass-word.txt', 'r') as file:
    password = file.read()

# Create the email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Establish a connection to the Yahoo Mail SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# Login to the email account
server.login(username, password)

# Send the email
server.sendmail(sender_email, recipient_email, message.as_string())

# Close the connection
server.quit()
print('end')


# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# print('start')
# # Email configuration
# sender_email = 'vamanpundit@gmail.com'
# recipient_email = 'vamandeshmukh@example.com'
# subject = 'Subject of the email'
# body = 'This is the email body'
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# username = 'vamanpundit@gmail.com'
# password = ''
# with open('C://Users//DELL//Documents//pass-word.txt', 'r') as file:
#     password = file.read()

# # Create the email message
# message = MIMEMultipart()
# message['From'] = sender_email
# message['To'] = recipient_email
# message['Subject'] = subject
# message.attach(MIMEText(body, 'plain'))

# # Establish a connection to the SMTP server
# server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()

# # Login to the email account
# server.login(username, password)

# # Send the email
# server.sendmail(sender_email, recipient_email, message.as_string())

# # Close the connection
# server.quit()
