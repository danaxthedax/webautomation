#Chat with sale

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://automationpractice.com/")
driver.maximize_window()

image_select = driver.find_elements("xpath", "//img[@src]")
image_select[0].click()
driver.implicitly_wait(2)
original_window = driver.current_window_handle

chat_with_sale = driver.find_elements("xpath", "//*[contains(@class, 'ppb-button') and contains(@class, 'btn-primary-chat') and contains(@class, 'chat-btn-popup')]")


for cla in chat_with_sale:
        print(cla)
        ActionChains(driver)\
                .scroll_to_element(cla) \
                .scroll_by_amount(0, 200) \
                .perform()
        cla.click()
        driver.switch_to.window(driver.window_handles[1])
        verify_chat = driver.find_element("xpath", "//*[contains(text(), 'Chat with Sales')]")
        if verify_chat != "":
            print("Passed")
        driver.close()
        driver.switch_to.window(original_window)


driver.close()






