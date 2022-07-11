from pip import main
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

# def Craw_link():
#     data =[]
#     driver = webdriver.Edge(executable_path='.\msedgedriver.exe')
#     driver.get("http://www.nettruyenmoi.com/truyen-tranh/tuyet-the-vo-than-149960")
    
#     # 3053,6067
#     for i in range(1,464):
#         texts = driver.find_element_by_xpath('//*[@id="nt_listchapter"]/nav/ul/li['+ str(i) +']/div[1]/a')
#         data.append(texts.get_attribute("href"))
#     driver.close()   
#     return data

# def Craw_content():
#     links = Craw_link()
#     driver = webdriver.Edge(executable_path='.\msedgedriver.exe')
#     driver.get(links[1])
#     time.sleep(20)
#     for i in range(len(links)-1, 0, -1):
#         driver.get(links[i])
#         time.sleep(1)
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(10)
#     driver.close() 
#     return 0
    # letien210601@gmail.com

    
def Craw_content(): 
 
    username = "letien210601@gmail.com"
    password = "272774545"
    
    driver = webdriver.Edge(executable_path='.\msedgedriver.exe')
    driver.get('http://www.nettruyenmoi.com/truyen-tranh/tren-nguoi-ta-co-mot-con-rong/chap-1-1/478406')


    elem = driver.find_element_by_xpath('//*[@id="header"]/div/div/ul/li[1]')
    actions = ActionChains(driver)
    actions.click(elem).perform()

    driver.find_element_by_xpath('//*[@id="ctl00_mainContent_login1_LoginCtrl_UserName"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="ctl00_mainContent_login1_LoginCtrl_Password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="ctl00_mainContent_login1_LoginCtrl_Login"]').click()

    for i in range(850):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        elem = driver.find_element_by_xpath('//*[@id="chapterNavBottom"]/a[2]')
        actions = ActionChains(driver)
        actions.click(elem).perform()

    driver.close() 


    return 0
    
def main():
    Craw_content()

        
if __name__ =='__main__':
    main()

# links = ['http1', 'http://tiendepz']
# for i in range(len(links)-1, 0, -1):
#     print(links[i])
