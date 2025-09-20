import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "Jayanthb000@gmail.com"
app_password = "qmxxuqemcaeaqbdy"
receiver_email = "jayanth1962@outlook.com"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Test Email from Python (Gmail)"

body = "Hello, this is a test email sent using Gmail SMTP from Python."
msg.attach(MIMEText(body, 'plain'))

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(msg)

print("Email sent successfully!")
