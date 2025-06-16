from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("headless")
chromeOptions.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chromeOptions)  # chrome driver initiation
driver.implicitly_wait(5)  # globally wait applied
driver.get("https://rahulshettyacademy.com/angularpractice/")  # testing rahul shetty practice page

print(driver.title)  # ProtoCommerce
