from config import VIDEOS, REGISTER_LINK

def get_intro_message():
    return (
        "Merhaba! 🌿 Doğal yollarla enerji, stres yönetimi ve odaklanma konularına meraklı mısın?\n"
        "Bilim temelli, oldukça ilginç bir sistem keşfettim. İstersen kısa bir video göndereyim? 🎥"
    )

def get_followup_message(response_text):
    text = response_text.lower()
    if "evet" in text or "olur" in text:
        return f"Harika! Şuradaki videoyu izle 👉 {VIDEOS['intro']}"
    elif "ürün" in text:
        return f"Ürün tarafı ilgini çektiyse şu kısa tanıtıma bak 👉 {VIDEOS['product']}"
    elif "gelir" in text or "kazanç" in text:
        return f"Gelir modeliyle ilgili detaylı anlatım burada 👉 {VIDEOS['income']}"
    elif "kayıt" in text:
        return f"Katılmak istersen kayıt sayfası burada 👉 {REGISTER_LINK}"
    else:
        return "Ne konuda daha çok bilgi istersin? Ürün mü, gelir modeli mi?"
