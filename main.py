from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up Chrome options
chrome_options = Options()
# Comment this out to see the browser
chrome_options.add_argument("--headless=new")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initializing WebDriver
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
url = "https://www.dentons.com/en/our-professionals"
driver.get(url)

# Wait for page to load
time.sleep(3)  

# BeautifulSoup to parse the page source
soup = BeautifulSoup(driver.page_source, "html.parser")

books = soup.find_all("div", class_="person-tab")

for book in books:
    name = book.find("h4", class_="ng-binding").text
    info = book.find_all("p", class_="ng-binding")
    designation = info[0].text
    places = info[1].text
    print(f"{name} {designation} {places}")

# Close the browser
driver.quit()
