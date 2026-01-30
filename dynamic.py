from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
url = "https://quotes.toscrape.com/js/"
driver.get(url)
wait = WebDriverWait(driver, 10)

quotes = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
)
for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text
    print(f"{text} — {author}")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
next_button = driver.find_element(By.LINK_TEXT, "Next →")
next_button.click()
time.sleep(3)
import csv

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])

    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text
        writer.writerow([text, author])
driver.quit()
