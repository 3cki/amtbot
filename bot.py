# imports
import time
import telepot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

# enter your values
BOT_TOKEN = 'YOUR_BOT_TOKEN'
CHAT_ID = 99999999
MOVING_MONTH = "April"
MOVING_YEAR = 2022
MOVING_DAY = 10

# constants
URL = "https://service.berlin.de/dienstleistung/120686/"
FINDALL_TEXT = "Termin berlinweit suchen und buchen"
CALENDAR_CLASS = "calendar-table"
TIMEOUT_LIMIT = 10
WAIT_MINUTES = 1

# init bot
tg = telepot.Bot(BOT_TOKEN)

# open page for registering a flat
driver.get(URL)

# find button for appointment selection in total Berlin
link_findall = driver.find_element(by=By.LINK_TEXT, value=FINDALL_TEXT)
link_findall.click()

try:
    # wait for page to load
    calendar = WebDriverWait(driver, TIMEOUT_LIMIT).until(EC.presence_of_element_located((By.CLASS_NAME, CALENDAR_CLASS)))

    #next_href = driver.find_element(by=By.CLASS_NAME, value="next")
    #next_link = next_href.find_element(by=By.TAG_NAME, value="a")
    #next_link.click()

    # get all calendar dates
    test = 1
    while test == 1:
        month = driver.find_element(by=By.XPATH, value="//th[@class='month' and text()='" + MOVING_MONTH + " " + str(MOVING_YEAR) + "']")
        page = month.find_element(by=By.XPATH, value="../../..")
        dates = page.find_elements(by=By.TAG_NAME, value="td")
        for date in dates:
            if (date.text.isnumeric()):
                day = int(date.text)
                if day > MOVING_DAY:
                    if date.get_attribute("class") == "buchbar":
                        txt = "Am " + str(day) + ". " + MOVING_MONTH + " " + str(MOVING_YEAR) + " ist noch ein Termin frei! " + URL 
                        tg.sendMessage(CHAT_ID, txt)
                        break
                    else:
                        print("Kein freier Termin am " + str(day) + ". " + MOVING_MONTH + " " + str(MOVING_YEAR))
        time.sleep(WAIT_MINUTES * 60)
        driver.refresh()
except:
    tg.sendMessage(CHAT_ID, "Ich bin abgestürzt :(")
    driver.quit()