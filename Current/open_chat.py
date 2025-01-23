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

classes = driver.find_elements("xpath", "//a[@class]")


for cla in classes:
    if "Chat With Us" in cla.get_attribute("innerHTML"):
        cla.click()





