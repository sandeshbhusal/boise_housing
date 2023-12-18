import telebot
import requests
import time

KEY = "6583339131:AAEH2sySsJxdgQCBBjRJdfwPAMvY9sq9-Sg"

while True:
    resp = requests.get("https://www.boisestate.edu/housing-apartments/apartments-availability/")
    t = resp.text

    if "No Apartments Currently Available" in t:
        print(f"{time.time()} No apts")
    else:
        print(f"{time.time()} Apts!")
    try:
        bot = telebot.TeleBot(KEY)
        bot.send_message(chat_id="@boise_housing_monitor", text = "Helo")
    except Exception as e:
        print("no can send msg. :(") 
        print(e.with_traceback())
    time.sleep(10)