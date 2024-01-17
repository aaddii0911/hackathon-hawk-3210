from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

url = "https://vegetablemarketprice.com/market/noida/today"
chrome_driver_path = "C:\\development\\chromedriver-win64\\chromedriver.exe"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url=url)
drop_down = driver.find_element(By.XPATH, "//div[@class = 'svg-file-icon svg-file-calendar']")
drop_down.click()
for _ in range(23):
    prev = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/thead/tr/th[1]")
    prev.click()
    time.sleep(1)

days = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[@class = 'active start-date active end-date available']")
days.click()
time.sleep(2)

time.sleep(2)

# Close the browser
driver.quit()
