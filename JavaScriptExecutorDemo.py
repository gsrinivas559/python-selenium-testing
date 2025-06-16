import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # chrome driver initiation
driver.implicitly_wait(5)  # globally wait applied
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")  # testing rahul shetty practice page

# scroll to specific position of the page
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)  # To visually view the output

# scroll to bottom of the page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
time.sleep(2)  # To visually view the output

# scroll to Top of the page
driver.execute_script("document.documentElement.scrollTop = 0;")
time.sleep(2)  # To visually view the output

# to pass value on element
driver.execute_script("arguments[0].value='Srinivas';", driver.find_element(By.CSS_SELECTOR, "#name"))
time.sleep(2)  # To visually view the output

element = driver.find_element(By.CSS_SELECTOR, ".mouse-hover")
# scroll to specific element
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(2)  # To visually view the output

# scroll to specific element Top
driver.execute_script("arguments[0].scrollIntoView(false);", element)
time.sleep(2)  # To visually view the output

# scroll to specific element in line
driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", element)
time.sleep(2)  # To visually view the output

# to click on element
driver.execute_script("arguments[0].click();", element)
time.sleep(2)  # To visually view the output

driver.quit()
