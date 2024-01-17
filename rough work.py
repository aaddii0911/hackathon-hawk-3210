from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_data(driver):
    date_ = []
    date_of_day = driver.find_elements(By.XPATH, "//span[@style = 'vertical-align: middle;']")
    for i in date_of_day:
        dates = i.text
        date_.append(dates)
    print(date_)

    table_title = []
    header = driver.find_elements(By.XPATH, "//div[@class = 'col-sm-12 px-sm-2 px-0']/table/thead/tr/th")
    for i in header:
        headers = i.text
        table_title.append(headers)
    print(table_title)

    data = []
    rows = driver.find_elements(By.XPATH, "//div[@class = 'col-sm-12 px-sm-2 px-0']/table/tbody/tr")
    for i in rows:
        row = i.text
        data.append(row)
    print(data)

url = "https://vegetablemarketprice.com/market/noida/today"
chrome_driver_path = "C:\\development\\chromedriver-win64\\chromedriver.exe"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url=url)

# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()

# Click on the previous month button 23 times
for _ in range(2):
    prev = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/thead/tr/th[1]")
    prev.click()
    time.sleep(1)

# Click on each day one by one and scrape data
days_to_click = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[@data-title='r0c3']")
days_to_click.click()
time.sleep(2)
scrape_data(driver)

# Click on the dropdown before clicking the next day
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(5)

days_to_click = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[@data-title='r0c4']")
days_to_click.click()
time.sleep(2)
scrape_data(driver)

# Click on the dropdown before clicking the next day
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(5)

days_to_click = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[@data-title='r0c5']")
days_to_click.click()
time.sleep(2)
scrape_data(driver)

# Close the browser
driver.quit()
