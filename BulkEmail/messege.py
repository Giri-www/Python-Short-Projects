""" Email sent code  by using your gmail """

""" Code 1st wayout => only one mail"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email server configuration
smtp_server = 'smtp.gmail.com' 
smtp_port = 587 
sender_email = 'nordkai8977@gmail.com'  
password = 'abcdfrr' 
# Email content
subject = 'The Vibe'
message_body = 'The vibe is very good !!'

# List of recipient email addresses
recipient_emails = ['rg786483@gmail.com']

# Create a multipart message
message = MIMEMultipart()
message['From'] = sender_email
message['Subject'] = subject
message.attach(MIMEText(message_body, 'plain'))

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

try:
    # Login to the SMTP server with App Password
    server.login(sender_email, password)

    # Send emails in bulk
    for recipient_email in recipient_emails:
        message['To'] = recipient_email
        text = message.as_string()
        for i in range(1):
            server.sendmail(sender_email, recipient_email, text)

            print("Emails sent successfully!")

except smtplib.SMTPAuthenticationError as e:
    print("SMTP Authentication Error:", e)

# Close the connection to the SMTP server
server.quit()

""" Code 2nd  way out => Multiple mail"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# smtp server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'nordkai89877@gmail.com'  
password = 'abcccc' 

# Email contents: subject and message body pair
subjects = ['Pampu', 'Sorav']
message_bodies = ['atoz', 'ztoa']

# List of recipient email addresses
recipient_emails = ['abc@gmail.com', 'def@gmail.com']

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

try:
    # Login to the SMTP server with the app password
    server.login(sender_email, password)

    # Send emails in bulk
    for recipient_email, subject, message_body in zip(recipient_emails, subjects, message_bodies):
        # Create a fresh email message object for each recipient
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(message_body, 'plain'))
        for i in range(5):
#             server.sendmail(sender_email, recipient_email, text)

            # Send the email
            server.sendmail(sender_email, recipient_email, message.as_string())
            print(f"Email sent successfully to {recipient_email}")

except smtplib.SMTPAuthenticationError as e:
    print("SMTP Authentication Error:", e)

# Close the connection to the SMTP server
server.quit()
