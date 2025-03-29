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
url = "https://books.toscrape.com/"
driver.get(url)

# Wait for page to load
time.sleep(2)  

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find all books
books = soup.find_all("article", class_="product_pod")

# Extract book titles and prices
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    print(f"{title} - {price}")

# Close the browser
driver.quit()
