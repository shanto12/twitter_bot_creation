from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

user_name = "shanto12@gmail.com"
password = "leeleelee1z"


chrome_driver_path = "C:/Data/Coding/Webdrivers/chromedriver.exe"

browser = webdriver.Chrome(executable_path=chrome_driver_path)
browser.get("https://www.twitter.com")


a = ActionChains(browser)
a.send_keys(user_name)
sleep(1)
a.key_down(Keys.TAB).key_up(Keys.TAB).perform()
a.send_keys(password)
sleep(1)
a.key_down(Keys.TAB).key_up(Keys.TAB).perform()
a.key_down(Keys.TAB).key_up(Keys.TAB).perform()
sleep(1)

el_text = browser.find_elements_by_link_text("login")
el_name = browser.find_elements_by_name("login")
el_tag = browser.find_elements_by_tag_name("login")

# a.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
# sleep(1)
# a.key_down(Keys.TAB).key_up(Keys.TAB).perform()

# elems = browser.find_elements_by_xpath('//*[@id="react-root"]')
#
# for el in elems:
#     if el.text == "Phone, email, or username":
#         print("sending keys for username")
#         el.send_keys("shanto12@gmail.com")
#     if el.text == "Password":
#         print("sending keys for Password")
#         el.send_keys("leeleelee1z")
#     if el.text == "Log in":
#         print("clicking login")
#         el.click()
#         break
#     print(el.text, el.id, el.tag_name, el.size, el.location)

print("DONE")