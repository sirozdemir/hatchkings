import pyautogui
import time
import datetime

CONFIDENCE = 0.85  # Görsel eşleşme güven seviyesi
WAIT_TIME = 1.5    # Tıklama sonrası bekleme süresi (saniye)

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}")

def locate_and_click(image, name):
    pos = pyautogui.locateCenterOnScreen(image, confidence=CONFIDENCE)
    if pos:
        log(f"{name} bulundu: {pos}, tıklanıyor.")
        pyautogui.click(pos)
        time.sleep(WAIT_TIME)
        return True
    return False

def run_bot():
    log("Bot başlatıldı! CTRL+C ile çıkabilirsiniz.")
    while True:
        try:
            found = False

            # Sıralı kontrol: önce 'open', sonra 'continue', sonra 'gotit'
            if locate_and_click("open_button.png", "Open Butonu"):
                found = True
            elif locate_and_click("continue_button.png", "Continue Butonu"):
                found = True
            elif locate_and_click("gotit_button.png", "Got It Butonu"):
                found = True

            if not found:
                log("Buton bulunamadı, tekrar deneniyor...")
                time.sleep(1)

        except KeyboardInterrupt:
            log("Bot kapatıldı.")
            break

run_bot()
