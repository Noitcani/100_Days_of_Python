import datetime as dt
from random import choice
import smtplib
import pandas

## CHANGE THESE SETTINGS

EMAIL = "your_email@domain.com"
PASSWORD = "your password"
EMAIL_SMTP = "your email provider smtp"

LETTER_LIST = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
today = (now.month, now.day)
print(today)

# 2. Check if today matches a birthday in the birthdays.csv
for (index, row) in data.iterrows():
    birthday = (row["month"], row["day"])

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
    # actual name from birthdays.csv
    if birthday == today:

        with open(choice(LETTER_LIST), "r") as f:
            email_body = f.read().replace("[NAME]", row["name"])
            message = f"Subject: Happy Birthday {row['name']}!\n\n{email_body}"

        # 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP(EMAIL_SMTP) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL, to_addrs=row["email"], msg=message)