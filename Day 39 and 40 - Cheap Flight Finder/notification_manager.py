import smtplib


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, private_data):
        self.email_sender = private_data["email_sender"]
        self.password = private_data["password"]
        self.email_reciver = private_data["email_reciver"]
        self.smtp = private_data["smtp"]

    def send_email(self, flight):
        msg = f"Subject:Low price alert!\n\nOnly £{flight.price} to fly from {flight.cityFrom}-{flight.airportFrom} to {flight.cityTo}-{flight.airportTo}, from {flight.outDate} to {flight.returnDate}.\n\nLink: {flight.link}"
        print("Sending Email...")
        with smtplib.SMTP(self.smtp, 587) as connection:
            connection.starttls()
            connection.login(user=self.email_sender, password=self.password)
            connection.sendmail(from_addr=self.email_sender,
                                to_addrs=self.email_reciver,
                                msg=msg.encode("utf8"))
            print("Email has been sent.")