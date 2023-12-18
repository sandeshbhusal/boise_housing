import telebot
import requests
import time

KEY = "6583339131:AAEH2sySsJxdgQCBBjRJdfwPAMvY9sq9-Sg"
time = 0

def send_message(text: str) -> None:
    try:
        bot = telebot.TeleBot(KEY)
        bot.send_message(chat_id="-4096042993", text = text)
    except Exception as e:
        print("no can send msg. :(") 
        print(e.with_traceback())
    

while True:
    resp = requests.get("https://www.boisestate.edu/housing-apartments/apartments-availability/")
    t = resp.text

    if "No Apartments Currently Available" in t:
        print(f"{time.time()} No apts")
    else:
        print(f"{time.time()} Apts!")
        send_message("Apartments listed!") 
         
    time += 10
    if time % 600 == 0 :
        send_message("Scanned for 10 mins, no updates.")
        
    time.sleep(10)