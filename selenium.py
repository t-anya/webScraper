# DEL -> BOM trip flights

#selenium for browser automation
from selenium import webdriver
import time

print("------Welcome to Coupon Hunters------")
chrome_path=r"C:\Users\user\Desktop\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)

print("------Accessing easemytrip.com------")

#easemyTrip flights url
driver.get('https://www.easemytrip.com/flights.html')

print("------Searching Flights from DEL -> BOM------")

time.sleep(4)
#click on the search button
driver.find_element_by_xpath("""/html/body/div[10]/div/div[3]/div[1]/div[6]/input""").click()

print("------Selecting specific flight from DEL -> BOM------")

#click on Book Now
time.sleep(4)
driver.find_element_by_xpath("""/html/body/form/div[9]/div[4]/div/div[2]/div[2]/div/div/div[3]/div[1]/div[1]/div[1]/div[6]/button""").click()

print("------Booking Flight from DEL -> BOM------")

#Book Now for specefic flight
time.sleep(4)

#Coupons available for trip
couponDivTxt=driver.find_element_by_xpath("""/html/body/form/div[10]/div[6]/div[1]/div[4]/div[3]/div/div[1]/div[1]/div[3]""").text
print("Coupons available for specefic trip.")
print(couponDivTxt)
print("----------------------------------------------------------------------")

#Flight details for trip
flightDetailTxt=driver.find_element_by_xpath("""/html/body/form/div[10]/div[6]/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div/div/div""").text
print("Flight details available for specefic trip.")
print(flightDetailTxt)
print("----------------------------------------------------------------------")

