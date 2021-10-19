from bs4 import BeautifulSoup
import requests
import json
import smtplib

with open("Day 47 - Amazon Price Tracker\\private_data.json") as file:
    private_data = json.load(file)

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52",
    "Accept-Language":
        "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
}

TARGET_PRICE = 308
URL = "https://www.amazon.com.br/Externo-Port%C3%A1til-Expansion-STEA1000400-Seagate/dp/B07N6994DT?ref_=Oct_d_otopr_d_16364750011&pd_rd_w=6qjxR&pf_rd_p=32b1ddde-8c67-4d85-bbf2-2754a91fdba5&pf_rd_r=T40540XH59JNGD2VS8FW&pd_rd_r=c348f14d-fa73-4b58-b930-2d802f8d695b&pd_rd_wg=ZDipY&pd_rd_i=B07N6994DT"

data = requests.get(
    url=URL,
    headers=headers,
).text

soup = BeautifulSoup(data, "html.parser")

title = soup.find("span", id="productTitle")
price = soup.find("span", id="priceblock_ourprice")

price_float = float(price.text.split("R$")[1].replace(",", "."))
title = title.text.replace("\n", "")

print(title)
print(price.text)

if price_float <= TARGET_PRICE:
    email_sender = private_data["email_sender"]
    password = private_data["password"]
    email_reciver = private_data["email_reciver"]
    smtp = private_data["smtp"]

    msga = f"Subject:Amazon Price Tracker\n\n{title} is now for {price.text}, and your target price was R${'{:.2f}'.format(TARGET_PRICE)}\n\n Link: {URL}"

    print("Sending Email...")
    with smtplib.SMTP(smtp, 587) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=password)
        connection.sendmail(
            from_addr=email_sender,
            to_addrs=email_reciver,
            msg=msga.encode("utf-8"))
        print("\nEmail has been sent.\n")