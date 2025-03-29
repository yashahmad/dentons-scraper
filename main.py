from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import json

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

professionals = soup.find_all("div", class_="person-tab")

data = []

for prof in professionals:
    name = prof.find("h4", class_="ng-binding").text.strip()
    info = prof.find_all("p", class_="ng-binding")
    if len(info) >= 2:
        designation = info[0].text.strip()
        places = info[1].text.strip()
        data.append({
            "name": name,
            "designation": designation,
            "places": places
        })

# Write the data to a JSON file
with open("professionals.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

# Close the browser
driver.quit()
