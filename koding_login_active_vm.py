from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

KODING_USERNAME = "<YOUR_USERNAME>"
KODING_PASSWORD = "<YOUR_PASSWORD>"
ACTIVE_VM_BUTTON_ID = 'kd-363'

def waitforever_vm_button_clickable(tries=10):
    try:
        wait = WebDriverWait(browser, 10)
        active_vm_button = wait.until(EC.element_to_be_clickable((By.ID, ACTIVE_VM_BUTTON_ID)))
        active_vm_button.click()
    except selenium.common.exceptions.TimeoutException:
        print "wait for more 10 sec"
        waitforever_vm_button_clickable()
    finally:
        browser.quit()

browser = webdriver.Firefox()
url = "https://koding.com/Login"
browser.get(url)

name_elem = browser.find_element_by_name('username')  
name_elem.send_keys(KODING_USERNAME)
password_elem = browser.find_element_by_name('password')  
password_elem.send_keys(KODING_PASSWORD + Keys.RETURN)

# check the button is displayed and enabled
waitforever_vm_button_clickable()



