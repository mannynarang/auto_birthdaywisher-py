import random
import smtplib
import datetime as dt
import pandas as df


def sendemail(motivational_quote, email):
    my_email = "<email>"
    my_password = "<password>"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f"Subject:Happy Birthday\n\n{motivational_quote}")
        connection.close()


def get_random_letter(name):
    number = random.randint(1, 3)
    with open(f"letter_templates/letter_{number}.txt") as file_data:
        file = file_data.read()
        file = file.replace('[NAME]', name)
        return file


now = dt.datetime.now()
birthday_data = df.read_csv("birthdays.csv")
dic = birthday_data.to_dict(orient="index")

birthday_dict = {(dic[key]['month'], dic[key]['day']): {'name': dic[key]['name'], 'email': dic[key]['email']} for key, value in
                 dic.items()}
today = (dt.datetime.now().month, dt.datetime.now().day)


for key, value in birthday_dict.items():
    print(today)
    print(key)
    if today == key:
        sendemail(get_random_letter(birthday_dict[key]['name']), birthday_dict[key]['email'])
