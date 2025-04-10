#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
from mac_notifications import client


# Set the path to the ChromeDriver executable
chromedriver_path = "/usr/local/bin/chromedriver"  # Adjust the path if needed

# Create Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Add this line if you are running on a headless server


# Using readlines()
apartment_links_file = open('/Users/sunil.vaggannavar/project-appartment/retrieved_links.txt', 'r+')
apartment_links = apartment_links_file.readlines()



def fill_and_send(link):
    subDriver = webdriver.Chrome( options=chrome_options)
    subDriver.get(link)

    for field_id,field_value in form_data.items():
        if field_id.startswith('income'):
            element =  Select(subDriver.find_element(By.ID, field_id))
            element.select_by_value(field_value)
        else:
            element = subDriver.find_element(By.ID, field_id)
            element.send_keys(field_value)
    submitbutton = subDriver.find_element(By.CLASS_NAME,'form-expose_submit')
    print(submitbutton.get_attribute('name'))
    for i in range(0,10000000):
        print(i)
    #submitbutton.click()
    applied_files.write(link+'\n')
    for i in range(0,10000):
        print(i)
    subDriver.close()

def fetchlinks():
    listofnewresults=[]
    target_url = "https://www.deutsche-wohnen.com/en/property-offers#page=1&locale=en&commercializationType=rent&utilizationType=flat,retirement&location=Berlin&city=Berlin&area=50&radius=10"
    # Specify the path to the ChromeDriver executable and Chrome options
    driver = webdriver.Chrome( options=chrome_options)
    driver.get(target_url)
    print(driver.title)
    search_button = driver.find_element(By.ID, "search-objects-result")
    print(search_button.text)
    list_of_results = driver.find_elements(By.CLASS_NAME, "object-list__content-container")
    retrieved_links_file = open('/Users/sunil.vaggannavar/project-appartment/retrieved_links.txt', 'r+')
    listOfLines = retrieved_links_file.readlines()
    title = search_button.text+' - '+ datetime.now().isoformat()
    retrieved_links_file.write(title)
    retrieved_links_file.write("\n")
    for eachObject in list_of_results:
        if eachObject.get_attribute('href')+'\n' not in listOfLines:
            retrieved_links_file.write(eachObject.get_attribute('href'))
            retrieved_links_file.write("\n")
            listofnewresults.append(eachObject.get_attribute('href')+'\n')
    retrieved_links_file.close()
    driver.close()
    if len(listofnewresults) > 0 : 
        print(listofnewresults)
        client.create_notification(
            title="New listing is found",
            subtitle=''.join(listofnewresults)
        )

def fetchlinks_heimstaden():
    listofnewresults=[]
    target_url = "https://portal.immobilienscout24.de/ergebnisliste/92830022/1?sid=7nii6nlalhstgeisoi7s22or16"
    # Specify the path to the ChromeDriver executable and Chrome options
    driver = webdriver.Chrome( options=chrome_options)
    driver.get(target_url)
    list_of_results = driver.find_elements(By.XPATH, "//figure/a")
    retrieved_links_file = open('/Users/sunil.vaggannavar/project-appartment/retrieved_links.txt', 'r+')
    listOfLines = retrieved_links_file.readlines()
    
    for eachObject in list_of_results:
        if eachObject.get_attribute('href')+'\n' not in listOfLines:
            retrieved_links_file.write(eachObject.get_attribute('href'))
            retrieved_links_file.write("\n")
            listofnewresults.append(eachObject.get_attribute('href')+'\n')
    retrieved_links_file.close()
    driver.close()
    if len(listofnewresults) > 0 : 
        client.create_notification(
            title="New listing is found",
            subtitle=''.join(listofnewresults)
        )

def fetchlinks_berlinhaus():
    listofnewresults=[]
    target_url = "https://www.berlinhaus.com/suchergebnisse/?adv_search_nonce_field=0daa42b0d2&filter_search_action%5B%5D=wohnen&advanced_city=berlin&advanced_area=&kaltmiete-bis=1500&flaeche-ab=50&zimmeranzahl-ab=all&submit=SEARCH"
    # Specify the path to the ChromeDriver executable and Chrome options
    driver = webdriver.Chrome( options=chrome_options)
    driver.get(target_url)
    list_of_results = driver.find_elements(By.CLASS_NAME, "property_listing")
    retrieved_links_file = open('/Users/sunil.vaggannavar/project-appartment/retrieved_links.txt', 'r+')
    listOfLines = retrieved_links_file.readlines()
    header = driver.find_element(By.CLASS_NAME,'title_prop')
    for eachObject in list_of_results:
        if eachObject.get_attribute('data-link')+'\n' not in listOfLines:
            retrieved_links_file.write(eachObject.get_attribute('data-link'))
            retrieved_links_file.write("\n")
            listofnewresults.append(eachObject.get_attribute('data-link')+'\n')
    retrieved_links_file.close()
    driver.close()
    if len(listofnewresults) > 0 : 
        client.create_notification(
            title="New listing is found",
            subtitle=''.join(listofnewresults)
        )

def fetchlinks_livingInBerlin():
    listofnewresults=[]
    target_url = "https://www.livinginberlin.de/angebote/mieten"
    # Specify the path to the ChromeDriver executable and Chrome options
    driver = webdriver.Chrome( options=chrome_options)
    driver.get(target_url)
    list_of_results = driver.find_elements(By.CLASS_NAME, "uk-text-right")
    retrieved_links_file = open('/Users/sunil.vaggannavar/project-appartment/retrieved_links.txt', 'r+')
    listOfLines = retrieved_links_file.readlines()
    for eachObject in list_of_results:
        tag = eachObject.find_element(By.TAG_NAME, 'a').get_attribute('href')
        if tag+'\n' not in listOfLines:
            retrieved_links_file.write(tag)
            retrieved_links_file.write("\n")
            listofnewresults.append(tag+'\n')
    retrieved_links_file.close()
    driver.close()
    if len(listofnewresults) > 0 : 
        client.create_notification(
            title="New listing is found",
            subtitle=''.join(listofnewresults)
        )

def fetchlinks_inberlin():
    listofnewresults=[]
    target_url = "https://inberlinwohnen.de/wohnungsfinder/"
    # Specify the path to the ChromeDriver executable and Chrome options
    driver = webdriver.Chrome( options=chrome_options)
    driver.get(target_url)
    list_of_results = driver.find_elements(By.CLASS_NAME, "org-but")
    retrieved_links_file = open('/Users/sunil.vaggannavar/project-appartment/retrieved_links.txt', 'r+')
    listOfLines = retrieved_links_file.readlines()
    for eachObject in list_of_results:
        if eachObject.get_attribute('href')+'\n' not in listOfLines:
            retrieved_links_file.write(eachObject.get_attribute('href'))
            retrieved_links_file.write("\n")
            listofnewresults.append(eachObject.get_attribute('href')+'\n')
    retrieved_links_file.close()
    driver.close()
    if len(listofnewresults) > 0 : 
        client.create_notification(
            title="New listing is found",
            subtitle=''.join(listofnewresults)
        )



#fetchlinks()
fetchlinks_heimstaden()
#fetchlinks_berlinhaus()
#fetchlinks_inberlin()
fetchlinks_livingInBerlin()
 

 
