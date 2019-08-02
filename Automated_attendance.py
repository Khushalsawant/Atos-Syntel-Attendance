# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:21:16 2019

@author: KS5046082
"""

#import os
#print(os.environ.get('user_name'))

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import requests
import re
from datetime import date
from datetime import datetime
import win32gui, win32con
import calendar 
from dateutil.relativedelta import relativedelta

import ctypes  # An included library with Python install.
 
def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd))) 


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def connect_home_url_in_loop():
    #connect_home_url_in_loop
    if response.status_code == 200:
        ### Login to Syntel portal automatically
        user_name = "######"
        user_password = "$$$$$$$$$"
        
        top_windows = []
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('start-maximized')
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
        chrome_options.add_argument('--no-sandbox') # # Bypass OS security model
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        #capabilities = chrome_options.to_capabilities()
        #driver = webdriver.Chrome("C:/Users/KS5046082/PyTutorial/chromedriver_win32/chromedriver.exe",chrome_options=chrome_options)
        #driver.maximize_window()
        #"C:/Users/KS5046082/PyTutorial/chromedriver_win32/chromedriver.exe",
        print("Entering into  %s" %(url))
        time.sleep(5)
        #print("status_code = ",response.status_code)
        driver = webdriver.Chrome(options=chrome_options)#,
                                      #desired_capabilities=capabilities)
        driver.implicitly_wait(15) # seconds
        driver.get("https://www.myatos-syntel.net")
        
        today = date.today()
        
        print("Today's date:", today)
        #print("Today's Week Number:", today.weekday())
        print("Today is ",calendar.day_name[today.weekday()])
        Total_Hrs_as_per_policy = int(today.weekday())*9 + 9
        print("Total_Hrs_as_per_policy =",Total_Hrs_as_per_policy)
        
        WebDriverWait(driver, 15)
        #print("Current session is {}".format(driver.session_id))
        for i in top_windows:
            #print (i)
            if "chromedriver" in i[1].lower():
                win32gui.ShowWindow(i[0], win32con.SW_HIDE)
                break 
         
            #print("driver.current_url = ",driver.current_url)
            #print("driver.page_source = ",driver.page_source)
        #my Atos Syntel - Login    
        #print("driver.title before = ",driver.title)
        assert "my Atos Syntel - Login" in driver.title
        #print("driver.title after = ",driver.title)
        elem = driver.find_element_by_id("_com_liferay_login_web_portlet_LoginPortlet_kpoUserName")
        elem.send_keys(user_name)
        elem = driver.find_element_by_id("_com_liferay_login_web_portlet_LoginPortlet_kpoPassword")
        elem.send_keys(user_password)
        elem.send_keys(Keys.RETURN)
        time.sleep(15)
            
        elem_my_image = driver.find_element_by_xpath("//*[@id='my_image']")
        actions=ActionChains(driver)
        actions.click(elem_my_image)
        actions.perform()
        time.sleep(15)
        
        elem_leave_attendance = driver.find_element_by_xpath("//*[@id='R2']/p/a/img")
        actions=ActionChains(driver)
        actions.click(elem_leave_attendance)
        actions.perform()
        time.sleep(15)
        
        #"//*[@id='PlaceHolderMain_grdToday']/tbody/tr[2]/td[2]"
    
        #//*[@id="PlaceHolderLeftNavBarTop_Menu1_mnutaasdb"]/ul/li[5]/a
        driver.switch_to.frame("_com_liferay_iframe_web_portlet_IFramePortlet_INSTANCE_BGBP31ofSaoC_iframe")
        time.sleep(15)
        
        try:
            elem_todays_in_time = driver.find_element_by_xpath("//*[@id='PlaceHolderMain_grdToday']/tbody/tr[2]/td[2]").text
            print("elem_todays_in_time = ",elem_todays_in_time)
            time.sleep(10)
        except NoSuchElementException:
            pass
            

        elem_leave_attendance_hrs = driver.find_element_by_xpath("//button[@id= 'PlaceHolderMain_myBtn']") 
        #elem_leave_attendance_hrs = driver.find_elements_by_xpath("//button[@id='PlaceHolderMain_myBtn']").click
        #print("elem_leave_attendance_hrs",elem_leave_attendance_hrs)
            
        actions_hrs=ActionChains(driver)
        actions_hrs.click(elem_leave_attendance_hrs)
        actions_hrs.perform()
        time.sleep(10)
            
        Hrs = driver.find_element_by_xpath("//span[@id = 'PlaceHolderMain_lblhrscount']").text 
        
        if Hrs !=  'Label':
            print("hours = ",Hrs)
            #print(" Type hrs=",type(Hrs))
            text_strng, time_field = Hrs.split(':')
            #print("time_field",time_field)
            time_hrs,time_mins = map(int, re.findall(r'\d+', time_field))
            Total_time_completed = str(time_hrs)+":"+str(time_mins)
            #Total_time_obj = datetime.strptime(Total_time_completed,'%H:%M').time()
            print("Total_time_completed =  ", Total_time_completed)
            
            remaining_hrs = Total_Hrs_as_per_policy - time_hrs -1
            remaining_mins = 60 - time_mins
            #Hrs_need_to_complete = datetime_obj_per_policy - Total_time_obj
            if remaining_hrs > 0:
                Hrs_need_to_complete = str(remaining_hrs) + " Hrs " + str(remaining_mins) + " Mins"
            #Hrs_need_to_complete = datetime.strptime('27:00', '%H:%M') - Total_time_obj
                print("Hrs need to complete for today",Hrs_need_to_complete)
                str_1 = "Hrs need to complete for today " + str(Hrs_need_to_complete)
            else:
                Hrs_need_to_complete =  str(remaining_hrs) + " Hrs " + str(remaining_mins) + " Mins"
                print("Hrs completed extra for today",Hrs_need_to_complete)
                str_1 = "Hrs completed extra for today " + str(Hrs_need_to_complete)
            final_OP = Hrs + "\n" + str_1
            Mbox('Automated Attendance Details', final_OP, 1)
        else:
            Mbox('Automated Attendance Details ', "Compeleted hours are not coming on portal", 1)
            print("Compeleted hours are not coming on portal")
        driver.delete_all_cookies()
        #print("driver.current_url = ",driver.current_url)
        driver.close()
        time.sleep(5)
        driver.quit()
    else:
        print("response.status_code = ",response.status_code)


if __name__ == '__main__':
    print("executed in existing file ")

    url = 'https://www.myatos-syntel.net'
    response = requests.get(url,verify=False)        # To execute get request 

    print("status_code = ",response.status_code) 

    connect_home_url_in_loop()
else:
    print("executed using import file ")

    url = 'https://www.myatos-syntel.net'
    response = requests.get(url,verify=False)        # To execute get request 

    print("status_code = ",response.status_code) 

    connect_home_url_in_loop()