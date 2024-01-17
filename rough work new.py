from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#
# def scrape_data(driver):
#     date_ = []
#     date_of_day = driver.find_elements(By.XPATH, "//span[@style = 'vertical-align: middle;']")
#     for i in date_of_day:
#         dates = i.text
#         date_.append(dates)
#     print(date_)
#
#     table_title = []
#     header = driver.find_elements(By.XPATH, "//div[@class = 'col-sm-12 px-sm-2 px-0']/table/thead/tr/th")
#     for i in header:
#         headers = i.text
#         table_title.append(headers)
#     print(table_title)
#
#     data = []
#     rows = driver.find_elements(By.XPATH, "//div[@class = 'col-sm-12 px-sm-2 px-0']/table/tbody/tr")
#     for i in rows:
#         row = i.text
#         data.append(row)
#     print(data)

url = "https://vegetablemarketprice.com/market/noida/today"
chrome_driver_path = "C:\\development\\chromedriver-win64\\chromedriver.exe"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url=url)

# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

# Click on the previous
for _ in range(2):
    prev = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/thead/tr/th[1]")
    prev.click()
    time.sleep(1)

# day1 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='1']")
# day1.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)
#
# day2 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='2']")
# day2.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)
#
# day3 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='3']")
# day3.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)
#
# day4 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='4']")
# day4.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)
#
# day5 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='5']")
# day5.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)
#
# day6 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='6']")
# day6.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)
#
# day7 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='7']")
# day7.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)
#
# day8 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='8']")
# day8.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)
#
# day9 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='9']")
# day9.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)
#
# day10 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='10']")
# day10.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)

# day11 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='11']")
# day11.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)

# day12 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='12']")
# day12.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)

# day13 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='13']")
# day13.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)
#
# day14 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='14']")
# day14.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)
#
# day15 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='15']")
# day15.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)
#
# day16 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='16']")
# day16.click()
# time.sleep(2)
# # Click on the dropdown
# drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
# drop_down.click()
# time.sleep(1)

day17 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='17']")
day17.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

day18 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='18']")
day18.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

day19 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='19']")
day19.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

day20 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='20']")
day20.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

day21 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='21']")
day21.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

day22 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='22']")
day22.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

day23 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='23']")
day23.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

day24 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='24']")
day24.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

day25 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='25']")
day25.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

day26 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='26']")
day26.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

day27 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='27']")
day27.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

day28 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='28']")
day28.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

day29 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='29']")
day29.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

day30 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='30']")
day30.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

day31 = driver.find_element(By.XPATH, "//div[@class='drp-calendar left single']/div/table/tbody/tr/td[normalize-space(text())='31']")
day31.click()
time.sleep(2)
# Click on the dropdown
drop_down = driver.find_element(By.XPATH, "//div[@class='svg-file-icon svg-file-calendar']")
drop_down.click()
time.sleep(1)

next = driver.find_element(By.XPATH, "//div[@class = 'calendar-table']/table/thead/tr/th[3]")
next.click()

# Close the browser
driver.quit()


