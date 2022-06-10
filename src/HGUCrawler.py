#!/usr/bin/env python
# coding: utf-8

import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time

class Crawler:
    def login(self, id: str, pw: str):
        hisnetURL ='https://hisnet.handong.edu/'
        id_input_path = '//*[@id="loginBoxBg"]/table[2]/tbody/tr/td[5]/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/span/input'
        password_input_path = '//*[@id="loginBoxBg"]/table[2]/tbody/tr/td[5]/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/input'
        login_button = '//*[@id="loginBoxBg"]/table[2]/tbody/tr/td[5]/form/table/tbody/tr[3]/td/table/tbody/tr/td[2]/input'
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(hisnetURL)
        time.sleep(5)
        driver.switch_to.frame("MainFrame")
        driver.find_element_by_name("id").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath(login_button).click()

        
        # 팝업창 요소 확인.
        time.sleep(5) #팝업창 로드 대기 5초 (매직 시간임. 네트워크 환경에 따라 충분하지 않을 수 있음)

        # 팝업창 종료
        main = driver.window_handles[0]
        pops = driver.window_handles[1:]
        for pop in pops:
            driver.switch_to.window(pop)
            driver.close()
        driver.switch_to.window(main)
        
        return driver
    
    def getCourseInfo(self, driver):
        driver.get('https://hisnet.handong.edu/haksa/record/HREC110M.php')
        source = driver.page_source
        soup = bs(source)
        
        semesters = soup.find_all('table', {'id': 'att_list'})
        semesters = semesters[2:]
        
        def trimWhiteSpace(rawText):
            return rawText.replace('\n', '').replace('\t', '').replace('\r', '')

        semesterYear = []
        colName = []
        data = []

        for index in semesters[0].find_all('tr')[1].find_all('td'):
            colName.append(trimWhiteSpace(index.getText()))

        for semester in semesters:
            semester = semester.find_all('tr')
            semesterYear.append(trimWhiteSpace(semester[0].getText()))
            courseInfo = []

            for rows in semester[2:]:
                t = rows.find_all('td')
                temp = []
                for r in rows.find_all('td'):
                    temp.append(trimWhiteSpace(r.getText()))
                courseInfo.append(temp)

            data.append(courseInfo)
            
        df = pd.DataFrame(columns = colName)
        for i in range(len(data)):
            for row in data[i]:
                df = df.append(pd.DataFrame([row], columns=colName), ignore_index=True)
        
        return df

