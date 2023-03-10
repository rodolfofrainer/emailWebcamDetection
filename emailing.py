import os
import env
import smtplib

import imghdr
from email.message import EmailMessage


def send_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = 'New customer showed up!'
    email_message.set_content('Hey, we just saw a new customer!')

    with open(image_path, 'rb') as file:
        content = file.read()

    email_message.add_attachment(
        content, maintype='image', subtype=imghdr.what(None, content))

    app_email_user = os.getenv('APP_EMAIL_USER')
    app_email_password = os.getenv('APP_EMAIL_PASSWORD')
    RECEIVER = app_email_user

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(app_email_user, app_email_password)
    gmail.sendmail(app_email_user, RECEIVER, email_message.as_string())
    gmail.quit()


if __name__ == '__main__':
    send_email('images\8.png')
