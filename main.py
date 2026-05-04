import time
import requests
from config import META_ACCESS_TOKEN
from message_flow import get_intro_message, get_followup_message

def send_meta_message(user_id, message):
    url = f"https://graph.facebook.com/v17.0/{user_id}/messages"
    data = {
        "recipient": {"id": user_id},
        "message": {"text": message},
        "access_token": META_ACCESS_TOKEN
    }
    requests.post(url, json=data)

def listen_and_respond():
    print("💬 Bot aktif... mesajları dinliyor.")
    while True:
        # Burada gerçek bir webhook veya API polling yapılır.
        # Gelen mesaj örnek datası:
        incoming = {"user_id": "123456", "text": "evet"}
        
        reply = get_followup_message(incoming['text'])
        send_meta_message(incoming['user_id'], reply)
        time.sleep(5)

if _name_ == "_main_":
    msg = get_intro_message()
    print("İlk mesaj:", msg)
    # Dinleme moduna geç
    listen_and_respond()
