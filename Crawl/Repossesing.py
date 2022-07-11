# from lib2to3.pgen2 import driver
from pip import main
import pandas as pd
import csv 

def GopChuong():
    TongHop= pd.read_excel('vi_1000.xlsx', index_col=0)
    TongHopch= pd.read_excel('ch_1000.xlsx', index_col=0)
    for i in range(3401,3436,1):
        try:
            df = pd.read_excel('.\\1000Chuong35xong\\'+ str(i)+'_Viet.xlsx', index_col=0)
            dfch = pd.read_excel('.\\1000Chuong35xong\\'+ str(i)+'_Trung.xlsx', index_col=0)
        except:
            print(i)
            continue
        TongHop = pd.concat([TongHop,df], axis=0)
        TongHopch = pd.concat([TongHopch,dfch], axis=0)
    TongHop['Viet'].to_excel('vi_1000.xlsx')
    TongHopch['Trung'].to_excel('ch_1000.xlsx')
    return 0
    
    
def main():
    GopChuong()
    print('xong')

        
if __name__ =='__main__':
    main()