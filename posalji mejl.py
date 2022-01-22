import smtplib
import ssl
from email.message import EmailMessage

sender_email = input("Unesite vas email: ")
receiver_email = input("Unesite email na koji saljete: ")
password = input("Unesite sifru: ")
subject =  input("Unesite subject email-a: ")
body = input("Unesite body email-a: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

brojac = 0

print("Sending email!")
while(brojac<10):
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,message.as_string())
    brojac += 1
print("Success")