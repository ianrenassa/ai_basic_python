# https://realpython.com/python-send-email/

import smtplib, ssl
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = input("Masukkan email pengirim: ")
password = getpass.getpass("Masukkan password: ")

message = MIMEMultipart("alternative")
message["Subject"] = input("Masukkan Judul email: ")
message["From"] = sender_email

text = "Test Email"
html = input("Masukkan isi email: ")

with open("send_email/list_email.txt", "r") as filex:
    receiver_email = filex.read().replace('\n',',')
#receiver_email = "ian.renassa@fingram.id"
message["To"] = receiver_email

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
print("Email terkirim!")