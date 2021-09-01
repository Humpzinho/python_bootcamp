import pandas as pd
import datetime as dt
import smtplib
import random

new_data = {
    'name': [],
    'email': [],
    'year': [],
    'month': [],
    'day': [],
}

new_record = 'yes'
while new_record == 'yes':
    new_record = input("Do you want to enter a new birthday record? Type yes or no: ")
    if new_record == 'yes':
        data = pd.read_csv("Day 32 - Birthday Wisher\Birthday Wisher\Birthday.csv")
        for key in new_data:
            new_data[key] = data[key].to_list()
        print(new_data)
        for key in new_data:
            new_value = input(f"Enter the {key}: ")
            new_data[key].append(new_value)
        print(new_data)
        n_data = pd.DataFrame(new_data)
        n_data.to_csv("Day 32 - Birthday Wisher\Birthday Wisher\Birthday.csv", index=False)
        print("The new data has been saved in birthdays.csv")
        
data_dict = pd.read_csv(
    "Day 32 - Birthday Wisher\Birthday Wisher\Birthday.csv")
data_dict = data_dict.to_dict(orient="records")

for data in data_dict:
    print("#", "*" * 50, "#")

    with open(
            f"Day 32 - Birthday Wisher\Birthday Wisher\letter_templates\letter_{random.randint(1, 3)}.txt"
    ) as file:
        letter = file.read()
        letter = "Subject:Happy Birthday!\n\n" + letter.replace(
            "[NAME]", data["name"])

    email_sender = "example@example.com"
    password = "3x3mple"
    smtp = "smtp.exemple.com"
    email_reciver = data["email"]
    msg = letter

    if dt.datetime.now().month == data["month"] and dt.datetime.now(
    ).day == data["day"]:
        print(f"\n              Sending email to {data['name']}...")
        with smtplib.SMTP(smtp, 587) as connection:
            connection.starttls()
            connection.login(user=email_sender, password=password)
            connection.sendmail(from_addr=email_sender,
                                to_addrs=email_reciver,
                                msg=msg)
            print("\n                Email has been sent.\n")
    else:
        print(f"\n              Today isn't birthday of {data['name']}.\n")

print("#", "*" * 50, "#")
print("Exiting...")
