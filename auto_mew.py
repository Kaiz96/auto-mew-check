import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Lấy danh sách từ BIP-39 từ GitHub
BIP39_URL = "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt"
wordlist = requests.get(BIP39_URL).text.splitlines()

# Chọn 12 từ ngẫu nhiên
mnemonic = " ".join(random.sample(wordlist, 12))
print(f"🔑 Seed Phrase: {mnemonic}")

# Cấu hình Selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Chạy chế độ không hiển thị trình duyệt
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Khởi động trình duyệt
driver = webdriver.Chrome(options=options)

# Truy cập MyEtherWallet
driver.get("https://www.myetherwallet.com/wallet/access/software?type=mnemonic")
time.sleep(3)  # Đợi trang tải

# Nhập Seed Phrase
mnemonic_input = driver.find_element(By.XPATH, "//textarea")
mnemonic_input.send_keys(mnemonic)
time.sleep(1)

# Nhấn "Next"
next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
next_button.click()

print("✅ Đã nhập Seed Phrase và nhấn NEXT!")
time.sleep(5)  # Đợi trang tải tiếp theo

driver.quit()
