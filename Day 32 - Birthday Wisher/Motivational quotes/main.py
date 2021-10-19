import random
import datetime as dt
import smtplib

with open("Day 32 - Birthday Wisher\Motivational quotes\quotes.txt") as file:
    all_quotes = file.readlines()
    quote = "Subject:Motivational Quote.\n\n" + random.choice(all_quotes)

#SAMPLE
email_sender = "example@example.com"
password = "3x3mple"
smtp = "smtp.exemple.com"
email_reciver = "exemple@example.com"
#To use subject = "Subject:Hello\n\nThis is my email body.", to separe subject to the email body use "\n\n"
#if you want to send a random inspirational quote just write "quote"(without quotes)
msg = quote
#Starts with monday, monday = 0, tuesday = 1, etc...
sender_day = 0

if dt.datetime.now().weekday() == sender_day:
    print("Sending email...")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=password)
        connection.sendmail(from_addr=email_sender,
                            to_addrs=email_reciver,
                            msg=msg)
        print("\nEmail has been sent.")
else:
    print("Today isn't monday.")