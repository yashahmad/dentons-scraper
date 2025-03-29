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

# Initialize WebDriver
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
url = "https://www.dentons.com/en/our-professionals"
driver.get(url)

# Wait for page to load
time.sleep(3)  

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find all books
books = soup.find_all("div", class_="person-tab")
print("Books",books)

# Extract book titles and prices
for book in books:
    name = book.find("h4", class_="ng-binding").text
    print(f"{name}")

# Close the browser
driver.quit()
