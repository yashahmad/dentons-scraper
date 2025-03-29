from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")  # Helps avoid permission issues
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevents crashes in Docker/Linux
chrome_options.add_argument("--user-data-dir=/tmp/chrome-profile")  # Use a different profile directory

service = Service()
driver = webdriver.Chrome(service=service ,options=chrome_options)

driver.get("https://www.scrapingcourse.com/ecommerce/")
print(driver.page_source)

driver.quit()
