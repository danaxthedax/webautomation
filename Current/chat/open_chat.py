#This test will open all chat buttons on the home page
#Fixa en bättre wait
#Få till pytest säger pass på testcases


from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import  ChromeDriverManager

options = Options()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) ,options=options)

driver.get("http://automationpractice.com/")
driver.maximize_window()

image_select = driver.find_elements("xpath", "//img[@src]")
image_select[0].click()
driver.implicitly_wait(2)
chat_text = driver.find_elements("xpath", "//*[contains(text(), 'Chat')]")

original_window = driver.current_window_handle

for cla in chat_text:
    if "Chat Now" in cla.get_attribute("innerHTML"):
        sleep(5)
        cla.click()
        sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        verify_chat = driver.find_element("xpath", "//*[contains(text(), 'Chat')]")
        if verify_chat != "":
            print("Passed")
        driver.close()
        driver.switch_to.window(original_window)

driver.close()






