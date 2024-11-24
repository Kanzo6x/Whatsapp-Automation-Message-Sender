from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


with open('numbers.txt', 'r') as file:
    phone_numbers = [line.strip() for line in file]


message_body = """
Congratulations 🎉
تم قبولك لحضور  Event:
NXT (Next Generation Tech)

📍 جامعة الأهرام الكندية – مبنى ملحق صيدلة
🗓 الثلاثاء، 26 نوفمبر
⏰ من الساعة 11 صباحاً إلى الساعة 2 ظهراً

🗓 الأربعاء، 27 نوفمبر
⏰ من الساعة 11 صباحاً إلى الساعة 2 ظهراً

⚠ نحب نلفت انتباهك أن العدد محدود، لكن حامل هذه الرسالة ليه فرصة لدعوة شخص واحد لمشاركته الـEvent معنا.\n

منتظرينكم ✨
"""


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
    except:
        print(f"Failed to send message to {phone_number}")


for number in phone_numbers:
    send_message(number, message_body)
    time.sleep(5)  

print("All messages have been sent!")
driver.quit()
