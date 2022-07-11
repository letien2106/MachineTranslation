import time, requests
from bs4 import BeautifulSoup
import os
import pandas as pd
import re


def Craw1(a,b):
    for i in range (a,b):
        text = []
        t = []
        page = requests.get('https://truyendich.com/vu-luyen-dien-phong/chuong-'+str(i)+'/')
        soup = BeautifulSoup(page.text,'html.parser')   
        a = soup.find_all('div', {"class":"content-des-info fs20"})
        # b = []
        # for i in a:
        #     b.append(i.text)

        # print(b)
        b = BeautifulSoup(str(a), 'html.parser')
        for i in b.find_all('p'):
            j = str(i.text).split('.')
            # so khớp các ký tự khoảng trắng
            #pattern = 'xa0\b'

            # chuỗi rỗng
            #replace = ''

            #j = re.sub(pattern, replace, j)
            # try:
            #     j.remove('\xa0')
            #     j.remove('"\xa0')
            # except:
            #     print("x not in list")
            text.append(j)
        print(text)
        #data = pd.DataFrame({"Viet": text})
        #data.to_excel(str(i-1) + '_Viet.xlsx')
    return 0
    
    
def main():
    Craw1(4000,4002)
    
    
if __name__ == '__main__':
    main()

