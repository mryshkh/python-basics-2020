#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

my_name = "Aleena"
my_location = "Lahore"
my_day = "08"
my_month = "05"
my_year = "1996"
my_hour = "10"
my_minute = "30"
my_meridian = "AM"

driver = webdriver.Chrome()
driver.get("https://astro-charts.com/")
time.sleep(5)

# name field
name = driver.find_element_by_name("name")
name.send_keys(my_name)

# location field
location = driver.find_element_by_class_name("form-control.input.geolocation.tt-input")
location.send_keys(my_location)
time.sleep(3)
location.send_keys(Keys.DOWN)
time.sleep(1)
location.send_keys(Keys.ENTER)

# DOB field
month = driver.find_element_by_class_name("form-control.input.month.center-align")
month.send_keys(my_month)
day = driver.find_element_by_class_name("form-control.input.day.center-align")
day.send_keys(my_day)
year = driver.find_element_by_class_name("form-control.input.year.center-align")
year.send_keys(my_year)

# Time field
hour = driver.find_element_by_class_name("form-control.input.hour.center-align")
hour.send_keys(my_hour)
minutes = driver.find_element_by_class_name("form-control.input.min.center-align")
minutes.send_keys(my_minute)

if my_meridian.upper() == "AM":
    meridian = driver.find_element_by_xpath("//*[@id='add_chart_form']/div[4]/div/div[2]/div[3]/label[1]/input")
else:
    # default is PM
    pass
meridian.send_keys(Keys.SPACE)

# Submit
create_chart = driver.find_element_by_class_name("btn.btn-primary.btn-hg.btn-submit") 
create_chart.click()

