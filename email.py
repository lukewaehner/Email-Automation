import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv("./logins.env")


print("Email:", os.getenv("EMAIL_ADDRESS"))
print("Password:", os.getenv("EMAIL_PASSWORD"))


def send_email(subject, body, recipient_email):
    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
    print("Sent")
    # try:
    #     server = smtplib.SMTP('smtp.gmail.com', 465)
    #     server.starttls()
    #     server.login(sender_email, sender_password)
    #     server.sendmail(sender_email, recipient_email, msg.as_string())
    #     server.quit()
    #     print("Sent")
    # except Exception as e:
    #     print(f"Failed at: {e}")

    # format: Subject, Body, Recipient Email
send_email("Boom", "Test",
           "test@test.com")
