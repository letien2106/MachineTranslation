from lib2to3.pgen2 import driver
from pip import main
from selenium import webdriver
import os
import pandas as pd
import csv 
import time

def Craw_link():
    data =[]
    driver = webdriver.Edge(executable_path='.\msedgedriver.exe')
    driver.get("http://www.b520.cc/0_111/")
    time.sleep(10)
    for i in range(737,1011):
        texts = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div/dl/dd['+ str(i) +']/a[@href]')
        data.append(texts.get_attribute("href")+'\n')
    driver.close()
    return data

def Craw_content():
    links = Craw_link()
    #tren 10 dưới 0
    #0= chap 1
    count_1 = 727
    for i in links:
        count = 0
        driver = webdriver.Edge(executable_path='.\msedgedriver.exe')
        driver.get(i)
        texts = driver.find_elements_by_tag_name("p")
        data = pd.DataFrame(columns=['Trung'])
        for text in texts:
            if text.text == '*********' :
                break
            else:             
                data.loc[count] = [text.text]          
                count = count + 1       
        data.to_excel(str(count_1) + '_Trung.xlsx')
        count_1 = count_1 + 1 
        driver.close()   
    return data1
    
    
def main():
    Craw_content()

        
if __name__ =='__main__':
    main()