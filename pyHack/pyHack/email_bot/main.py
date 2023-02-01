import smtplib
import pandas as pd
import time

#
# https://docs.google.com/spreadsheets/d/18NVEGyZXntZfpqLFfdsNVKQ6c1LASwijAag9XgnwDv4/edit?usp=sharing

sheet_id = "18NVEGyZXntZfpqLFfdsNVKQ6c1LASwijAag9XgnwDv4"

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

MY_EMAIL = "devjuneja197@gmail.com"
PASSWORD = "bcprtxjibmucipoh"


with open("content.txt") as content_file:
    CONTENT = content_file.read()

content_path = "content.txt"
while True:
    for i in range(0,len(df["Name"])):

        name = df["Name"][i]
        email = df["Email address"][i]


        with smtplib.SMTP("smtp.gmail.com") as connection:
            contents = CONTENT.replace("[NAME]",name)

            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                 to_addrs=email,
                                 msg= f"Subject: Feedback form\n\n{contents}")

    time.sleep(60)

    sheet_id = "18NVEGyZXntZfpqLFfdsNVKQ6c1LASwijAag9XgnwDv4"

    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")




    connection.close()