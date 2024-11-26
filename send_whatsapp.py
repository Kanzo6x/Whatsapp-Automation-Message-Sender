from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.parse  


with open('numbers.txt', 'r') as file:
    phone_numbers = [line.strip() for line in file]


message_body = """
Congratulations 🎉
تم قبولك لحضور  Event:
NXT (Next Generation Tech)

📍 جامعة الأهرام الكندية - Hall 8 
من الساعة 11 للساعة 1

⚠ نحب نلفت انتباهك أن العدد محدود، لكن حامل هذه الرسالة له فرصة لدعوة شخص واحد لمشاركته الـEvent معنا.

منتظرينكم ✨
"""


encoded_message = urllib.parse.quote(message_body)

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')


print("Please scan the QR code in the opened browser window to log in.")
input("Press Enter after logging in...")


def send_message(phone_number, message):
    
    driver.get(f"https://web.whatsapp.com/send?phone={phone_number}&text={message}")
    time.sleep(25)  

    try:
        send_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Send']")
        send_button.click()
        print(f"Message sent to {phone_number}")
    except Exception:
        print(f"Failed to send message to {phone_number}.")

for number in phone_numbers:
    send_message(number, encoded_message)
    time.sleep(5)  

print("All messages have been sent!")
driver.quit()
