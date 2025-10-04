#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import tempfile

# Path to ChromeDriver
chromedriver_path = "/usr/local/bin/chromedriver"

# Create Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless=new")        # Headless mode
chrome_options.add_argument("--no-sandbox")          # Linux server safety
chrome_options.add_argument("--disable-dev-shm-usage")  # Shared memory issues
chrome_options.add_argument("--disable-gpu")         # Disable GPU
chrome_options.add_argument("--disable-extensions")  # Disable extensions
chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")  # Unique temp profile
chrome_options.add_argument("--log-level=3")         # Reduce logging

# Read already retrieved links
with open('retrieved_links.txt', 'r+') as f:
    apartment_links = f.readlines()

def fill_and_send(link):
    service = Service(chromedriver_path)
    subDriver = webdriver.Chrome(service=service, options=chrome_options)
    subDriver.get(link)

    for field_id, field_value in form_data.items():
        if field_id.startswith('income'):
            element = Select(subDriver.find_element(By.ID, field_id))
            element.select_by_value(field_value)
        else:
            element = subDriver.find_element(By.ID, field_id)
            element.send_keys(field_value)

    submitbutton = subDriver.find_element(By.CLASS_NAME, 'form-expose_submit')
    print(submitbutton.get_attribute('name'))
    # submitbutton.click()  # Uncomment if you want to submit
    applied_files.write(link + '\n')
    subDriver.quit()


def fetchlinks():
    listofnewresults = []
    target_url = "https://www.deutsche-wohnen.com/en/property-offers#page=1&locale=en&commercializationType=rent&utilizationType=flat,retirement&location=Berlin&city=Berlin&area=50&radius=10"

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(target_url)
    print(driver.title)

    search_button = driver.find_element(By.ID, "search-objects-result")
    print(search_button.text)
    list_of_results = driver.find_elements(By.CLASS_NAME, "object-list__content-container")

    with open('retrieved_links.txt', 'r+') as retrieved_links_file:
        listOfLines = retrieved_links_file.readlines()
        title = search_button.text + ' - ' + datetime.now().isoformat()
        retrieved_links_file.write(title + "\n")
        for eachObject in list_of_results:
            href = eachObject.get_attribute('href')
            if href + '\n' not in listOfLines:
                retrieved_links_file.write(href + "\n")
                listofnewresults.append(href + '\n')

    driver.quit()
    print(listofnewresults)


def fetchlinks_heimstaden():
    listofnewresults = []
    target_url = "https://portal.immobilienscout24.de/ergebnisliste/92830022/1?sid=7nii6nlalhstgeisoi7s22or16"

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(target_url)

    list_of_results = driver.find_elements(By.XPATH, "//figure/a")
    with open('retrieved_links.txt', 'r+') as retrieved_links_file:
        listOfLines = retrieved_links_file.readlines()
        for eachObject in list_of_results:
            href = eachObject.get_attribute('href')
            if href + '\n' not in listOfLines:
                retrieved_links_file.write(href + "\n")
                listofnewresults.append(href + '\n')

    driver.quit()
    print(listofnewresults)


def fetchlinks_berlinhaus():
    listofnewresults = []
    target_url = "https://www.berlinhaus.com/suchergebnisse/?adv_search_nonce_field=0daa42b0d2&filter_search_action%5B%5D=wohnen&advanced_city=berlin&advanced_area=&kaltmiete-bis=1500&flaeche-ab=50&zimmeranzahl-ab=all&submit=SEARCH"

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(target_url)

    list_of_results = driver.find_elements(By.CLASS_NAME, "property_listing")
    with open('retrieved_links.txt', 'r+') as retrieved_links_file:
        listOfLines = retrieved_links_file.readlines()
        for eachObject in list_of_results:
            href = eachObject.get_attribute('data-link')
            if href + '\n' not in listOfLines:
                retrieved_links_file.write(href + "\n")
                listofnewresults.append(href + '\n')

    driver.quit()
    print(listofnewresults)


def fetchlinks_livingInBerlin():
    listofnewresults = []
    target_url = "https://www.livinginberlin.de/angebote/mieten"

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(target_url)

    list_of_results = driver.find_elements(By.CLASS_NAME, "uk-text-right")
    with open('retrieved_links.txt', 'r+') as retrieved_links_file:
        listOfLines = retrieved_links_file.readlines()
        for eachObject in list_of_results:
            tag = eachObject.find_element(By.TAG_NAME, 'a').get_attribute('href')
            if tag + '\n' not in listOfLines:
                retrieved_links_file.write(tag + "\n")
                listofnewresults.append(tag + '\n')

    driver.quit()
    print(listofnewresults)


def fetchlinks_inberlin():
    listofnewresults = []
    target_url = "https://inberlinwohnen.de/wohnungsfinder/"

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(target_url)

    list_of_results = driver.find_elements(By.CLASS_NAME, "org-but")
    with open('retrieved_links.txt', 'r+') as retrieved_links_file:
        listOfLines = retrieved_links_file.readlines()
        for eachObject in list_of_results:
            href = eachObject.get_attribute('href')
            if href + '\n' not in listOfLines:
                retrieved_links_file.write(href + "\n")
                listofnewresults.append(href + '\n')

    driver.quit()
    print(listofnewresults)


# Run fetchers
fetchlinks_heimstaden()
fetchlinks_livingInBerlin()
# fetchlinks()
# fetchlinks_berlinhaus()
# fetchlinks_inberlin()
