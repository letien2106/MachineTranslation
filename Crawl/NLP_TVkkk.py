import time, requests
from bs4 import BeautifulSoup
import os
import pandas as pd


def Craw1(a,b):
    for i in range (a,b):
        text = []
        page = requests.get('https://truyendich.com/vu-luyen-dien-phong/chuong-'+str(i)+'/')
        soup = BeautifulSoup(page.text,'html.parser')   
        a = soup.find_all('div',{'id':'read-content'})
        a = soup.prettify(formatter="minimal")
        soup = BeautifulSoup(str(a), 'html.parser')
        for e in soup.select('p'):  
            text.append(e.text.replace('\n' , ' ').replace('           ' , '').replace('          ' , ''))
        data = pd.DataFrame({"Viet": text})
        data.to_excel(str(i) + '_Viet.xlsx')
    return 0
    
    
def main():
    Craw1(3950,6000)
    
    
if __name__ == '__main__':
    main()

