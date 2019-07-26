# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:21:16 2019

@author: KS5046082
"""


import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import requests

import win32gui, win32con

import ctypes  # An included library with Python install.
 
def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd))) 


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def connect_home_url_in_loop():
    #connect_home_url_in_loop
    if response.status_code == 200:
        ### Login to Syntel portal automatically
        user = "KS5046082"
        pwd = "Jul2019$"
        
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
        print("Entering in loop of %s" %(url))
        time.sleep(5)
        print("status_code = ",response.status_code)
        driver = webdriver.Chrome(chrome_options=chrome_options)#,
                                      #desired_capabilities=capabilities)
        driver.implicitly_wait(15) # seconds
        driver.get("https://www.myatos-syntel.net")
        #print("Current session is {}".format(driver.session_id))
        for i in top_windows:
            #print (i)
            if "chromedriver" in i[1].lower():
                win32gui.ShowWindow(i[0], win32con.SW_HIDE)
                break 
         
            #print("driver.current_url = ",driver.current_url)
            #print("driver.page_source = ",driver.page_source)
            
        assert "Login" in driver.title
        elem = driver.find_element_by_id("_com_liferay_login_web_portlet_LoginPortlet_kpoUserName")
        elem.send_keys(user)
        elem = driver.find_element_by_id("_com_liferay_login_web_portlet_LoginPortlet_kpoPassword")
        elem.send_keys(pwd)
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
    
            #//*[@id="PlaceHolderLeftNavBarTop_Menu1_mnutaasdb"]/ul/li[5]/a
        driver.switch_to.frame("_com_liferay_iframe_web_portlet_IFramePortlet_INSTANCE_BGBP31ofSaoC_iframe")
        time.sleep(15)
    
        elem_leave_attendance_hrs = driver.find_element_by_xpath("//button[@id= 'PlaceHolderMain_myBtn']") 
        #elem_leave_attendance_hrs = driver.find_elements_by_xpath("//button[@id='PlaceHolderMain_myBtn']").click
        #print("elem_leave_attendance_hrs",elem_leave_attendance_hrs)
            
        actions_hrs=ActionChains(driver)
        actions_hrs.click(elem_leave_attendance_hrs)
        actions_hrs.perform()
        time.sleep(10)
            
        Hrs = driver.find_element_by_xpath("//span[@id = 'PlaceHolderMain_lblhrscount']").text 
        print("hours = ",Hrs)
        driver.delete_all_cookies()
        #print("driver.current_url = ",driver.current_url)
        driver.close()
        time.sleep(5)
        driver.quit()

        Mbox('Completed Hours', Hrs, 1)

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